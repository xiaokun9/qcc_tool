################################################################################
#
#  test_session.py
#
#  Copyright (c) 2019-2020 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
#
################################################################################
import pytest

from py_anc_calibration.anc_commands.at_anc_commands import ATCommands
from py_anc_calibration.session import ANCSessionBuilder
from py_anc_calibration.transport.serial_transport import SerialTransport
from py_anc_calibration.views.command_line_view import CommandLineView


def test_create_session_with_serial_transport():
    session_builder = ANCSessionBuilder()
    session_builder.add_transport('serial')

    assert isinstance(session_builder._session.transport, SerialTransport)

def test_create_session_with_unknown_transport_will_raise_error():
    session_builder = ANCSessionBuilder()
    with pytest.raises(KeyError):
        session_builder.add_transport('unknown')

def test_create_session_with_at_commands():
    session_builder = ANCSessionBuilder()
    session_builder.add_anc_commands('at')

    assert  isinstance(session_builder._session.anc_commands, ATCommands)

def test_create_session_with_unknown_anc_commands_will_raise_error():
    session_builder = ANCSessionBuilder()
    with pytest.raises(KeyError):
        session_builder.add_anc_commands('unknown')


def test_create_session_with_command_line_interface():
    session_builder = ANCSessionBuilder()
    session_builder.add_user_gateway('cli')

    assert isinstance(session_builder._session.view, CommandLineView)

def test_create_session_with_unknow_interface_will_raise_error():
    session_builder = ANCSessionBuilder()
    with pytest.raises(KeyError):
        session_builder.add_user_gateway('unknown')

def test_session_can_not_be_created_without_specifying_all_parameters():
    session_builder = ANCSessionBuilder()
    with pytest.raises(RuntimeError):
        session_builder.get_session()

    session_builder.add_user_gateway('cli')
    with pytest.raises(RuntimeError):
        session_builder.get_session()

    session_builder.add_transport('serial')
    with pytest.raises(RuntimeError):
        session_builder.get_session()

    session_builder.add_anc_commands('at')
    session_builder.get_session()
