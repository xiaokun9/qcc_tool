################################################################################
#
#  test_connected_serial_device.py
#
#  Copyright (c) 2019-2020 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
# This test requires connected serial device
# You must modify COM_PORT value to the right one
# Check Windows Device Manager to find COM port associated with your test device
#
################################################################################
import pytest

from py_anc_calibration.anc_commands.at_anc_commands import ATCommands
from py_anc_calibration.transport.serial_transport import SerialTransport

COM_PORT = 'COM5' # Your COM_PORT might be different

'''THE DEVICE MUST BE AUTHENTICATED'''

@pytest.fixture
def serial_device():
    serial_device = SerialTransport()
    try:
        serial_device.connect(**{'com_port': COM_PORT})
        yield serial_device
        serial_device.disconnect()
    except Exception as e:
        print('Error connecting to the device. Check com port')
        raise e

def test_send_anc_enable_command(serial_device):
    MODE = '7'  # THIS MUST BE CHANGED
    at_command_anc_enable = ATCommands.at_ancenable(MODE)
    payload, success = serial_device.execute(at_command_anc_enable)
    assert  success

def test_reading_fine_gain_value(serial_device):
    PATH = '1' # THIS MUST BE CHANGED
    MODE = '2' # THIS MUST BE CHANGED
    at_read_audio_key = ATCommands.at_ancreadfinegain(MODE, PATH)
    payload, success = serial_device.execute(at_read_audio_key)
    assert success
    print(payload)

def test_anc_disable(serial_device):
    at_command_anc_disable = ATCommands.at_ancdisable()
    payload, success = serial_device.execute(at_command_anc_disable)
    assert success

def test_set_gain_fine(serial_device):
    MODE = '1'
    PATH = '2'
    GAIN = '100'
    # ANC MUST BE ON
    at_command_anc_enable = ATCommands.at_ancenable(MODE)
    payload, success = serial_device.execute(at_command_anc_enable)
    assert success
    #####
    at_command_anc_set_fine_gain = ATCommands.at_ancsetfinegain(MODE, PATH, GAIN)
    payload, success = serial_device.execute(at_command_anc_set_fine_gain)
    assert success

def test_write_audio_key(serial_device):
    MODE = '1'
    PATH = '2'
    GAIN = '100'
    # ANC MUST BE ON
    at_command_anc_enable = ATCommands.at_ancenable(MODE)
    payload, success = serial_device.execute(at_command_anc_enable)
    assert success
    #####
    at_command_write_audio_key = ATCommands.at_ancwritefinegain(MODE, PATH, GAIN)
    payload, success = serial_device.execute(at_command_write_audio_key)
    assert success

def Xtest_disable_anc_calibration_key(serial_device):
    at_disable_anc_calibration = ATCommands.at_authdisable()
    payload, success = serial_device.execute(at_disable_anc_calibration)
    assert success