################################################################################
#
#  test_serial_transport.py
#
#  Copyright (c) 2019-2021 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
#
################################################################################
import pytest
from mock import patch, MagicMock, PropertyMock

from dts_terminal import serial_transport
from dts_terminal.serial_transport import SerialTransport

@pytest.fixture
def serial():
    with patch.object(serial_transport, 'serial') as serial_mock:
        serial_mock.serial_for_url = MagicMock()
        yield serial_mock

def test_serial_can_get_simple_ok_response_from_the_device(serial):
    OK_RESPONSE = b'AT+OK\r'
    serial_transport = SerialTransport("com1")

    type(serial_transport.serial).in_waiting = PropertyMock(side_effect=(True, False))
    serial_transport.serial.readline = MagicMock(return_value=OK_RESPONSE)

    response_lines = serial_transport.get_response_from_the_device(['OK', 'ERROR'])
    assert response_lines
    ok_line = [line for line in response_lines if 'OK' in line][0]
    assert 'OK' in ok_line

def test_serial_can_get_simple_error_response_from_the_device(serial):
    ERROR_RESPONSE = b'\r\nERROR\r\n'
    serial_transport = SerialTransport("com1")

    type(serial_transport.serial).in_waiting = PropertyMock(side_effect=(True, False))
    serial_transport.serial.readline = MagicMock(return_value=ERROR_RESPONSE)

    response_lines = serial_transport.get_response_from_the_device(['OK', 'ERROR'])
    assert response_lines
    ok_line = [line for line in response_lines if 'ERROR' in line][0]
    assert 'ERROR' in ok_line

def test_serial_can_get_payload_and_ok_code_from_device(serial):
    BLANK_LINE = '\n'
    PAYLOAD = '\r+ANCREADFINEGAIN:10\r\n'
    OK_RESPONSE = '\r\nOK\r\n'
    serial_transport = SerialTransport("com1")
    type(serial_transport.serial).in_waiting = PropertyMock(side_effect=(True, True, True, False))
    serial_transport.serial.readline = MagicMock(side_effect=(BLANK_LINE, PAYLOAD, OK_RESPONSE))

    response_lines = serial_transport.get_response_from_the_device()
    assert response_lines
    assert '+ANCREADFINEGAIN:10' in response_lines[0]
    assert 'OK' in response_lines[1]


def test_response_parser_got_only_ok_response_code(serial):
    serial_transport = SerialTransport("com1")
    device_response = ['\r\nOK\r\n']
    payload, success = serial_transport.parse_response(device_response)
    assert payload is None
    assert success == "OK"

def test_response_parser_got_only_at_ok_response_code(serial):
    serial_transport = SerialTransport("com1")
    device_response = ['\r\nAT+OK\r\n']
    payload, success = serial_transport.parse_response(device_response)
    assert payload is None
    assert success == "AT+OK"

def test_response_parser_got_only_error_response_code(serial):
    serial_transport = SerialTransport("com1")
    device_response = ['ERROR\r']
    payload, success = serial_transport.parse_response(device_response)
    assert payload is None
    assert success == "ERROR"

def test_response_parser_got_at_error_response(serial):
    serial_transport = SerialTransport("com1")
    device_response = ['AT+ERROR\r']
    payload, success = serial_transport.parse_response(device_response)
    assert payload is None
    assert success == "AT+ERROR"

def test_response_parser_got_ok_response_code_and_payload(serial):
    serial_transport = SerialTransport("com1")
    device_response = ['\r\n+ANCREADFINEGAIN:15\n\r','OK\r']
    payload, success = serial_transport.parse_response(device_response)
    assert payload == {'+ANCREADFINEGAIN':'15'}
    assert success == "OK"


def test_response_parser_got_at_ok_response_code_and_payload(serial):
    serial_transport = SerialTransport("com1")
    device_response = ['\r\n+ANCREADFINEGAIN:15\n\r','AT+OK\r']
    payload, success = serial_transport.parse_response(device_response)
    assert payload == {'+ANCREADFINEGAIN':'15'}
    assert success == "AT+OK"

def test_response_parser_got_error_response_code_and_payload(serial):
    '''probably impossible scenario but test anyway'''
    serial_transport = SerialTransport("com1")
    device_response = ['+ANCREADFINEGAIN:15','ERROR']
    payload, success = serial_transport.parse_response(device_response)
    assert payload == {'+ANCREADFINEGAIN':'15'}
    assert success == "ERROR"

def test_response_parser_got_at_error_response_code_and_payload(serial):
    '''probably impossible scenario but test anyway'''
    serial_transport = SerialTransport("com1")
    device_response = ['+ANCREADFINEGAIN:15','AT+ERROR']
    payload, success = serial_transport.parse_response(device_response)
    assert payload == {'+ANCREADFINEGAIN':'15'}
    assert success == "AT+ERROR"

def test_response_parser_returns_error_if_response_is_not_valid_0(serial):
    serial_transport = SerialTransport("com1")
    device_response = ['AT+ERRORish\r']
    with pytest.raises(RuntimeError):
       serial_transport.parse_response(device_response)

def test_response_parser_returns_error_if_response_is_not_valid_1(serial):
    serial_transport = SerialTransport("com1")
    device_response = ['OKish\r']
    with pytest.raises(RuntimeError):
       serial_transport.parse_response(device_response)


def test_payload_parser_ignores_white_spaces(serial):
    serial_transport = SerialTransport("com1")
    payload =  serial_transport.get_payload_from_std_out(['\n'])
    assert  payload == {}
