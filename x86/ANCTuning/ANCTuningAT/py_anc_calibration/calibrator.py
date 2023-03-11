################################################################################
#
#  calibrator.py
#
#  Copyright (c) 2019-2021 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
#  ANC CALIBRATION
#
################################################################################
import binascii
import codecs
import sys

from CryptoPlus.Cipher import python_AES as AES
from pathlib import Path

from .input_validators import ANCModeValidator, YesNoResponseValidator
from .input_validators import GainPathValidator, GainValueValidator, CalibrationActionsValidator
from .session import ANCCalibrationSession

KEY_FILE_PATH = str(Path(__file__).parent / "unlock.key")


class ANCTuneProperties():

    '''Represents current ANC calibration properties'''

    def __init__(self, mode=1, path=1, gain=None):
        self.mode = mode
        self.path = path
        self.gain = gain
        self.anc_is_enabled = None

    def gain_value_to_human_readable(self):
        '''convert gain value to nice human readable format'''
        return 'UNKNOWN' if self.gain is None else self.gain

    def anc_from_bool_to_human(self) -> str:
        '''convert bool to human readable on/off text'''
        if self.anc_is_enabled is None:
            return 'UNKNOWN'
        if self.anc_is_enabled:
            return 'ON'
        return 'OFF'

    def reset_gain_value_and_anc_status(self):
        '''reset gan and anc enable status to None,
        the function is called whenever mode/path is changed
        '''
        self.gain = None
        self.anc_is_enabled = None

    def __str__(self):
        gain = self.gain_value_to_human_readable()
        anc_enabled = self.anc_from_bool_to_human()
        return 'Current State: Mode:{} Path:{} Gain:{} ANC Enabled:{}'.format(
            str(self.mode), str(self.path), gain, anc_enabled)


class ANCCalibrator():
    """This class is the primary class for initiating the Calibration of
    the last few gain parameters of a QCC device.

    The user is asked for various values if these are not
    provided. The view provides the abstraction of how the user
    interaction is performed.
    """
    def __init__(self, session: ANCCalibrationSession):
        self.transport = session.transport
        self.anc_command = session.anc_commands
        self.view = session.view
        self.device_anc_tune_data = ANCTuneProperties()

    def calibrate(self):
        """Starts ANC calibration process for the connected device.
        """
        self.view.start()
        self.show_instructions()
        try:
            self.view.show_message('Authenticating the device...')
            device_authenticated = self.authenticate_device()
            if not device_authenticated:
                sys.exit(-1)
            self.view.show_message('Getting device values...')
            self.read_fine_gain_for_current_mode_and_path()
            self.show_current_anc_tune_data()
            user_stopped_calibration = False
            while not user_stopped_calibration:
                user_stopped_calibration = self.start_main_calibration_loop()
                self.show_current_anc_tune_data()
            self.disable_anc_calibration()
        except KeyboardInterrupt:
            self.view.show_message('\n\nKeyboard Interrupt – You might have unsaved changes')
        except TimeoutError as error:
            self.view.show_message('\n\nTimeout Error – ' + str(error))
        finally:
            self.transport.disconnect()
            self.view.end()

    def get_key(self):
        """retrieve key from unlock.key file"""
        key_file = open(KEY_FILE_PATH, "rb")
        for line in key_file.readlines():
            str_line = line.decode("utf-8")
            if "#" in str_line or len(line.strip()) == 0:
                # comment or empty line
                continue
            # assume this is the key
            return binascii.unhexlify(line)
        raise RuntimeError(f"Failed to retrieve key from '{KEY_FILE_PATH}' file")

    def authenticate_device(self):
        key = self.get_key()
        self.aes = AES.new(key, AES.MODE_CMAC)
        response, success = self.transport.execute(self.anc_command.at_authstart())
        if not success:
            self.view.show_message('Failed to authenticate device. Check KEY')
            return False
        random = response['+AUTHSTART']
        random = codecs.decode(random, 'hex')
        enc = self.aes.encrypt(random)
        enc_str = codecs.encode(enc, "hex")
        response_command = self.anc_command.at_authresp(enc_str.decode('utf-8').upper())
        _, success = self.transport.execute(response_command)
        if not success:
            self.view.show_message('Failed to authenticate device')
            return False
        return True

    def start_main_calibration_loop(self) -> bool:
        """Main Calibration loop where user choose the next action to execute.
        The loop continues until the user chooses to exit this process.
        """
        validator = CalibrationActionsValidator()

        action = self.view.request_data_from_user(
            message='What would you like to do? \n'
                    'Change (M)ode, Change (P)ath, Change Gain (0-255), '
                    '(E)nable ANC, (D)isable ANC, e(X)it?',
            validator=validator)
        action = action.lower()
        if action.isdigit():
            self.set_fine_grain(action)
            return False

        if self.device_anc_tune_data.gain is not None:
            # if we change properties and gain is not None, we save gain to device flash memory
            write_was_successful = self.write_audio_key()
            if not write_was_successful:
                self.view.show_message('The action is not possible, '
                                       'because previous data was not saved')
                return False

        if action == 'x':
            self.view.show_message('Exiting calibration loop')
            return True
        elif action == 'm':
            self.set_new_anc_mode()
        elif action == 'e':
            self.enable_anc_for_current_anc_mode()
        elif action == 'd':
            self.disable_anc()
        elif action == 'p':
            self.set_gain_path()
        return False

    def enable_anc_for_current_anc_mode(self)  -> bool:
        """Enables ANC  for a current selected mode.

        If device returns error, error message will be displayed to user.

        :returns: True if ANC is already enabled or was enabled successfully, False otherwise.
        """
        if self.device_anc_tune_data.anc_is_enabled is True:
            return True
        current_anc_mode = self.device_anc_tune_data.mode
        command = self.anc_command.at_ancenable(current_anc_mode)
        _, success = self.transport.execute(command)
        if success:
            self.view.show_message('Success! '
                                   'ANC for mode {} is Enabled'.format(str(current_anc_mode)))
            self.device_anc_tune_data.anc_is_enabled = True
            return True
        self.view.show_message(
            'Error! Device returned error code, '
            'when tried to enable ANC for mode {} '.format(str(current_anc_mode)))
        return False

    def disable_anc(self):
        """Disables ANC.

        If device returns error, error message will be displayed to user.
        """
        command = self.anc_command.at_ancdisable()
        _, success = self.transport.execute(command)
        if success:
            self.view.show_message('Success! ANC is disabled!')
            self.device_anc_tune_data.anc_is_enabled = False
            return
        self.view.show_message('Error! Device returned error code, '
                               'when tried to disable ANC')

    def read_fine_gain_for_current_mode_and_path(self) -> None:
        """Read the fine gain from device persistence for specified mode and
        path (FFA, FFB or FB).

        If request is successful local fine gain value will be updated.

        If device returns error, error message will be displayed to user
        """
        if not self.enable_anc_for_current_anc_mode():
            return
        mode = self.device_anc_tune_data.mode
        fine_gain_path = self.device_anc_tune_data.path
        command = self.anc_command.at_ancreadfinegain(mode, fine_gain_path)
        payload, success = self.transport.execute(command)
        if success:
            gain = int(payload['+ANCREADFINEGAIN'])
            self.device_anc_tune_data.gain = gain
            return
        self.view.show_message(
            'Error! Device returned error code, '
            'when tried to get fine gain value '
            'for mode {} and path {}'.format(str(mode), str(fine_gain_path)))

    def set_fine_grain(self, gain_value):
        """Set the fine gain in DSP/AudioSubsystem for selected mode and path.

        :param gain_value: new gain value (0-255)

        Note: ANC must be enabled to perform this request.

        If device returns error, error message will be displayed to user.
        """
        if not self.enable_anc_for_current_anc_mode():
            return
        current_gain_path = self.device_anc_tune_data.path
        mode = self.device_anc_tune_data.mode
        command = self.anc_command.at_ancsetfinegain(mode, str(current_gain_path), str(gain_value))
        _, success = self.transport.execute(command)
        if success:
            self.view.show_message(
                'Success! Fine Gain at path {} is set to value {}'.format(str(current_gain_path),
                                                                          str(gain_value)))
            value = int(gain_value)
            self.device_anc_tune_data.gain = value
            return
        self.view.show_message(
            'Error! Device returned error code, '
            'when tried to set fine gain value to {}, '
            'for mode {} and path {}'.format(
                str(gain_value), str(self.device_anc_tune_data.mode), str(current_gain_path)))

    def write_audio_key(self) -> bool:
        """Save the fine gain value to device persistence memory for current mode and path.

        Note: ANC must be enabled to perform this request

        If device returns error, error message will be displayed to user
        If fine gain value is not set , error message will be displayed to user
        """
        if not self.enable_anc_for_current_anc_mode():
            return False
        mode = self.device_anc_tune_data.mode
        gain_path = self.device_anc_tune_data.path
        gain_value = self.device_anc_tune_data.gain
        if gain_value is None:
            self.view.show_message('Error. The fine gain value is not set yet. '
                                   'Please set the fine gain value first')
            return False
        command = self.anc_command.at_ancwritefinegain(mode, gain_path, gain_value)
        _, success = self.transport.execute(command)
        if success:
            return True
        self.view.show_message('Error writing data to memory. You might have unsaved changes.')
        return False

    def disable_anc_calibration(self):
        '''Permanently disables ANC calibration capabilities.

        NOTE: This is a mandatory step after calibration.
        '''
        validator = YesNoResponseValidator()
        while True:
            disable_anc_calibration_mode = self.view.request_data_from_user(
                message='Would you like to permanently disable ANC calibration mode?'
                'WARNING!: This is a mandatory step after completing calibration.',
                validator=validator)
            if disable_anc_calibration_mode.lower() in validator.yes_responses:
                _, success = self.transport.execute(self.anc_command.at_dtssettestmode(0))
                if success:
                    self.view.show_message("Successfully disabled ANC Calibration Mode")
                    return
                self.view.show_message('Error! Device returned error code. ')
            else:
                self.view.show_message("You refused to permanently disable ANC calibration mode")
                return

    def set_gain_path(self):
        '''Sets new calibration gain path.

        Note: this action has no effect on device side (i.e no message is sent)
        '''
        gain_path = self.view.request_data_from_user(message='Please specify gain path '
                                                             '[FFA=1 FFB=2 FB=3]',
                                                     validator=GainPathValidator())
        self.device_anc_tune_data.path = int(gain_path)
        self.device_anc_tune_data.reset_gain_value_and_anc_status()
        self.read_fine_gain_for_current_mode_and_path()

    def set_new_anc_mode(self):
        '''Set new calibration anc mode.

        Note: this action has no effect on device side (i.e no message is sent)
        '''
        anc_mode = self.view.request_data_from_user(
            message='Please specify ANC Enable Mode [1-10]',
            validator=ANCModeValidator())
        self.device_anc_tune_data.mode = int(anc_mode)
        self.device_anc_tune_data.reset_gain_value_and_anc_status()
        self.read_fine_gain_for_current_mode_and_path()

    def show_current_anc_tune_data(self):
        '''shows current calibration parameters'''
        return self.view.show_message('\n### ' + str(self.device_anc_tune_data) + ' ###\n')

    def show_instructions(self):
        '''Shows user friendly instructions for calibration'''
        valid_anc_modes = ANCModeValidator().expected_input
        valid_path = GainPathValidator().expected_input
        valid_gain_values = GainValueValidator().expected_input
        text = valid_anc_modes + '\n' + valid_path + '\n' + valid_gain_values + '\n'
        self.view.show_message(text)
