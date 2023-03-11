################################################################################
#
#  test_sending_at_command_over_serial.py
#
#  Copyright (c) 2019-2020 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
#
################################################################################
import pytest
from mock import MagicMock

from py_anc_calibration.anc_commands.at_anc_commands import ATCommands, ATCommand
from py_anc_calibration.transport.serial_transport import SerialTransport

@pytest.fixture
def serial():
    serial_transport = SerialTransport()
    serial_transport.serial = MagicMock()
    serial_transport.serial.write = MagicMock()
    # assume device happy with the commands
    serial_transport.get_response_from_the_device = MagicMock(return_value=['OK'])
    yield serial_transport


def test_sending_at_anc_enable_command(serial):
    mode = 7
    expected_call = '\rAT+ANCENABLE=' + str(mode) + '\r\n'
    at_command = ATCommands.at_ancenable(mode)
    serial.execute(at_command)
    # must be encoded into binary
    serial.serial.write.assert_called_with(expected_call.encode('utf-8'))

def test_sending_at_anc_disable_command(serial):
    expected_call = '\rAT+ANCDISABLE' + '\r\n'
    at_command = ATCommands.at_ancdisable()
    serial.execute(at_command)
    # must be encoded into binary
    serial.serial.write.assert_called_with(expected_call.encode('utf-8'))

def test_sending_at_anc_read_audio_key_command(serial):
    gain_path = 2
    mode = 7
    expected_call = '\rAT+ANCREADFINEGAIN=' +  str(mode) + ',' + str(gain_path) + '\r\n'
    at_command = ATCommands.at_ancreadfinegain(mode, gain_path)
    serial.execute(at_command)
    # must be encoded into binary
    serial.serial.write.assert_called_with(expected_call.encode('utf-8'))

def test_sending_at_set_fain_fine_fb(serial):
    mode = 5
    gain_path = 3 # given in requirements specification
    gain_value = 0
    expected_call = '\rAT+ANCSETFINEGAIN=' + str(mode) + ',' + str(gain_path) + ',' + str(gain_value) + '\r\n'
    at_command = ATCommands.at_ancsetfinegain(mode, gain_path, gain_value)
    serial.execute(at_command)
    # must be encoded into binary
    serial.serial.write.assert_called_with(expected_call.encode('utf-8'))

def test_sending_at_write_audio_key(serial):
    gain_path = 2
    mode = 6
    gain_value = 124
    expected_call = '\rAT+ANCWRITEFINEGAIN=' + str(mode) + ',' + str(gain_path) + ',' + str(gain_value) + '\r\n'
    at_command = ATCommands.at_ancwritefinegain(mode, gain_path, gain_value)
    serial.execute(at_command)
    # must be encoded into binary
    serial.serial.write.assert_called_with(expected_call.encode('utf-8'))

def test_at_command_must_be_prefixed_and_suffixed(serial):
    generic_at_command = ATCommand('AT+Generic')
    expected_call = '\rAT+Generic\r\n'
    serial.execute(generic_at_command)
    serial.serial.write.assert_called_with(expected_call.encode('utf-8'))
