################################################################################
#
#  serial_transport.py
#
#  Copyright (c) 2019-2020 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
#  Sending data to device using serial port
#
################################################################################
import logging
import time
import serial

from . import abstract_transport

VALID_RESPONSES = ('OK', 'ERROR', 'AT+OK', 'AT+ERROR')

class SerialTransport(abstract_transport.AbstractTransport):

    '''connect to the device via serial port'''

    def __init__(self):
        self.serial = None

    def connect(self, **settings):
        '''connect to the serial port
        :Args:
            **settings (dict): key-value pair of settings
            Must include 'com_port' property
        :raise:
            KeyError: if 'com_port' is not provided in **settings
        '''
        if 'com_port' not in settings:
            raise KeyError("Expected 'com_port' in settings. Please provide com_port in settings")
        com_port = str(settings.pop('com_port'))
        baudrate = int(settings.pop('baudrate', 115200))
        timeout = int(settings.pop('timeout', 1))
        logging.info('Connecting to serial port on com port {}, '
                     'baudrate is {} and timeout is {}'.format(com_port, baudrate, timeout))
        self.serial = serial.Serial(com_port, baudrate=baudrate, timeout=timeout, **settings)

    def disconnect(self):
        '''disconnect from serial device'''
        if self.serial is None:
            raise RuntimeError('You first must connect to serial device')
        self.serial.close()

    def execute(self, command):
        '''execute command to calibrate anc
        command must be a concrete implementation of AbstractANCCommand

        :return  payload (dict) empty dict if not payload
                 success (bool) whether device returned error or ok code
        '''
        if self.serial is None:
            raise RuntimeError('You must first connect to the device')
        self.serial.reset_input_buffer()
        logging.debug('Sending command to device \"{}\"'.format(str(command).strip()))
        self.serial.write(str(command).encode('utf-8'))
        payload, success = self.parse_response(
            self.get_response_from_the_device())
        return payload, success

    def is_connected(self):
        '''True if device is successfully connected False otherwise'''
        return self.serial.is_open

    def get_response_from_the_device(self, timeout=3):
        '''get output from serial device
        read input stream until eof character or timeout
        :arg
            eof (list of str): end of file (response) characters
            timeout (int): timeout in minutes
        :return
            list of string: input buffer
        :raise TimeoutError if no line with eof was read
        '''
        start_time = time.time()
        lines = []
        while True:
            if self.serial.in_waiting:
                line = self.serial.readline()
                if isinstance(line, (bytes, bytearray)):
                    line = line.decode('utf-8')
                logging.debug('Line read from device: \"{}\"'.format(line.strip()))
                if any(c.isalpha() for c in line):
                    lines.append(line)
                if any(response in line for response in VALID_RESPONSES):
                    return lines
            time_passed = time.time() - start_time
            if time_passed >= timeout:
                raise TimeoutError('No responses got. Timeout time {} sec'.format(timeout))
            time.sleep(0.015)

    @staticmethod
    def parse_response(std_out: list):
        '''parse response from the device
        :arg std_out (list of str): list of text returned by device,
        new line equals new list index
        :returns payload (dict) if any
                 success (bool) whether device returned OK or ERROR code
        '''
        if not std_out:
            raise RuntimeError('No data to parse')
        response_code = std_out.pop(-1).strip()
        if response_code not in VALID_RESPONSES:
            raise RuntimeError('Response code expected to be AT+OK/AT+ERROR or OK/ERROR. Got: '
                               + response_code)
        success = bool(response_code == 'OK' or response_code == 'AT+OK')
        payload = SerialTransport.get_payload_from_std_out(std_out) if std_out else None
        return payload, success

    @staticmethod
    def get_payload_from_std_out(std_out: list):
        '''
        parse list of str with key_value pairs returned by device into dict
        :param std_out list of str: list of strings in format +key:value
        :return: dict of key value pairs
        '''
        payload = {}
        for line in std_out:
            line = str(line)
            if line.isspace():
                continue
            if ':' not in line:
                raise ValueError("Expected key-value lines and \':\' as separator. Got: " + line)
            key_value_pair = line.split(':')
            payload[key_value_pair[0].strip()] = key_value_pair[1].strip()
        return payload
