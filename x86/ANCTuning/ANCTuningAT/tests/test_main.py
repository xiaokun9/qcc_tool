################################################################################
#
#  test_main.py
#
#  Copyright (c) 2019-2020 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
#
################################################################################
from mock import patch
from py_anc_calibration import __main__
from py_anc_calibration.anc_commands.at_anc_commands import ATCommands
from py_anc_calibration.transport.serial_transport import SerialTransport
from py_anc_calibration.views.command_line_view import CommandLineView


def test_com_port_value_can_be_provided_from_command_as_a_command_line_argument():
    with patch.object(__main__, 'sys') as cla_mock:
        # ignore first list member as it is script name
        cla_mock.argv = ['main.py', '--device_settings', 'com_port=COM3']
        _, device_setting = __main__.create_anc_tuning_session()
        assert device_setting['com_port'] == 'COM3'


def test_multiple_device_settings_can_be_provided_as_a_command_line_argmunet():
    with patch.object(__main__, 'sys') as cla_mock:
        # ignore first list member as it is script name
        cla_mock.argv = ['main.py', '--device_settings', 'com_port=COM9', 'rate=200', 'set=5']
        _, device_setting = __main__.create_anc_tuning_session()
        assert device_setting['com_port'] == 'COM9'
        assert device_setting['rate'] == '200'
        assert device_setting['set'] == '5'

def test_transport_device_setting_at_commands_and_view_can_be_provided_as_a_command_line_argument():
    with patch.object(__main__, 'sys') as cla_mock:
        # ignore first list member as it is script name
        cla_mock.argv = ['main.py',
                         '--transport', 'serial',
                         '--anc_commands', 'at',
                         '--view', 'cli',
                         '--device_settings', 'com_port=COM9', 'rate=200', 'set=5']
        session, device_setting = __main__.create_anc_tuning_session()

        assert isinstance(session.transport, SerialTransport)
        assert isinstance(session.anc_commands, ATCommands)
        assert isinstance(session.view, CommandLineView)
        assert device_setting['com_port'] == 'COM9'
        assert device_setting['rate'] == '200'
        assert device_setting['set'] == '5'

