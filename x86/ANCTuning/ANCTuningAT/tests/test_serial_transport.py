################################################################################
#
#  test_serial_transport.py
#
#  Copyright (c) 2019-2020 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
#
################################################################################
import pytest
from mock import patch, MagicMock, PropertyMock

from py_anc_calibration.transport import serial_transport
from py_anc_calibration.transport.serial_transport import SerialTransport

@pytest.fixture
def serial():
    with patch.object(serial_transport, 'serial') as serial_mock:
        serial_mock.serial_for_url = MagicMock()
        yield serial_mock

def test_serial_device_cannot_not_be_connectd_if_com_port_is_not_provided(serial):
    serial_transport = SerialTransport()
    with pytest.raises(KeyError):
        serial_transport.connect()
    with pytest.raises(KeyError):
        serial_transport.connect(baudrate=2000, timeout=100)
    with pytest.raises(KeyError):
        serial_transport.connect(**{'com':'key must be com_port'})

def test_serial_transport_can_connect_to_serial_device(serial):
    serial_transport = SerialTransport()
    serial_transport.connect(**{'com_port': 'com1'})
    serial.Serial.assert_called_with('com1', baudrate=115200, timeout=1)
    serial.reset_mock()
    serial_transport.connect(**{'com_port': 'three', 'baudrate': 12, 'timeout': 200})
    serial.Serial.assert_called_with('three', baudrate=12, timeout=200)

def test_disconnect_will_fail_if_no_device_connected(serial):
    serial_transport = SerialTransport()
    with pytest.raises(RuntimeError):
        serial_transport.disconnect()

def test_disconnect_will_work_if_there_is_a_connected_device(serial):
    serial.Serial.return_value = MagicMock()
    serial_transport = SerialTransport()
    serial_transport.connect(**{'com_port': 'sss'})
    serial_transport.disconnect()

def test_serial_can_get_simple_ok_response_from_the_device():
    OK_RESPONSE = b'AT+OK\r'
    serial_transport = SerialTransport()

    serial_transport.serial = MagicMock()
    type(serial_transport.serial).in_waiting = PropertyMock(side_effect=(True, False))
    serial_transport.serial.readline = MagicMock(return_value=OK_RESPONSE)

    response_lines = serial_transport.get_response_from_the_device(['OK', 'ERROR'])
    assert response_lines
    ok_line = [line for line in response_lines if 'OK' in line][0]
    assert 'OK' in ok_line

def test_serial_can_get_simple_error_response_from_the_device():
    ERROR_RESPONSE = b'\r\nERROR\r\n'
    serial_transport = SerialTransport()

    serial_transport.serial = MagicMock()
    type(serial_transport.serial).in_waiting = PropertyMock(side_effect=(True, False))
    serial_transport.serial.readline = MagicMock(return_value=ERROR_RESPONSE)

    response_lines = serial_transport.get_response_from_the_device(['OK', 'ERROR'])
    assert response_lines
    ok_line = [line for line in response_lines if 'ERROR' in line][0]
    assert 'ERROR' in ok_line

def test_serial_can_get_payload_and_ok_code_from_device():
    BLANK_LINE = '\n'
    PAYLOAD = '\r+ANCREADFINEGAIN:10\r\n'
    OK_RESPONSE = '\r\nOK\r\n'
    serial_transport = SerialTransport()

    serial_transport.serial = MagicMock()
    type(serial_transport.serial).in_waiting = PropertyMock(side_effect=(True, True, True, False))
    serial_transport.serial.readline = MagicMock(side_effect=(BLANK_LINE, PAYLOAD, OK_RESPONSE))

    response_lines = serial_transport.get_response_from_the_device()
    assert response_lines
    assert '+ANCREADFINEGAIN:10' in response_lines[0]
    assert 'OK' in response_lines[1]

def test_serial_will_wait_for_timeout_and_then_raise_timeout_error():
    # TO DO: add timeout support
    serial_transport = SerialTransport()

    serial_transport.serial = MagicMock()
    type(serial_transport.serial).in_waiting = PropertyMock(return_value=True)
    serial_transport.serial.readline = MagicMock(return_value=' ')
    with pytest.raises(TimeoutError):
        serial_transport.get_response_from_the_device(timeout=0.4)

def test_response_parser_got_only_ok_response_code():
    serial_transport = SerialTransport()
    device_response = ['\r\nOK\r\n']
    payload, success = serial_transport.parse_response(device_response)
    assert payload is None
    assert success is True

def test_response_parser_got_only_at_ok_response_code():
    serial_transport = SerialTransport()
    device_response = ['\r\nAT+OK\r\n']
    payload, success = serial_transport.parse_response(device_response)
    assert payload is None
    assert success is True

def test_response_parser_got_only_error_response_code():
    serial_transport = SerialTransport()
    device_response = ['ERROR\r']
    payload, success = serial_transport.parse_response(device_response)
    assert payload is None
    assert success is False

def test_response_parser_got_at_error_response():
    serial_transport = SerialTransport()
    device_response = ['AT+ERROR\r']
    payload, success = serial_transport.parse_response(device_response)
    assert payload is None
    assert success is False

def test_response_parser_got_ok_response_code_and_payload():
    serial_transport = SerialTransport()
    device_response = ['\r\n+ANCREADFINEGAIN:15\n\r','OK\r']
    payload, success = serial_transport.parse_response(device_response)
    assert payload == {'+ANCREADFINEGAIN':'15'}
    assert success is True


def test_response_parser_got_at_ok_response_code_and_payload():
    serial_transport = SerialTransport()
    device_response = ['\r\n+ANCREADFINEGAIN:15\n\r','AT+OK\r']
    payload, success = serial_transport.parse_response(device_response)
    assert payload == {'+ANCREADFINEGAIN':'15'}
    assert success is True

def test_response_parser_got_error_response_code_and_payload():
    '''probably impossible scenario but test anyway'''
    serial_transport = SerialTransport()
    device_response = ['+ANCREADFINEGAIN:15','ERROR']
    payload, success = serial_transport.parse_response(device_response)
    assert payload == {'+ANCREADFINEGAIN':'15'}
    assert success is False

def test_response_parser_got_at_error_response_code_and_payload():
    '''probably impossible scenario but test anyway'''
    serial_transport = SerialTransport()
    device_response = ['+ANCREADFINEGAIN:15','AT+ERROR']
    payload, success = serial_transport.parse_response(device_response)
    assert payload == {'+ANCREADFINEGAIN':'15'}
    assert success is False

def test_response_parser_returns_error_if_response_is_not_valid_0():
    serial_transport = SerialTransport()
    device_response = ['AT+ERRORish\r']
    with pytest.raises(RuntimeError):
       serial_transport.parse_response(device_response)

def test_response_parser_returns_error_if_response_is_not_valid_1():
    serial_transport = SerialTransport()
    device_response = ['OKish\r']
    with pytest.raises(RuntimeError):
       serial_transport.parse_response(device_response)


def test_payload_parser_ignores_white_spaces():
    serial_transport = SerialTransport()
    payload =  serial_transport.get_payload_from_std_out(['\n'])
    assert  payload == {}
