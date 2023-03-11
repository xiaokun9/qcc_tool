###############################################################################
#
#  serial_transport.py
#
#  Copyright (c) 2019-2021 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
#  Sending data to device using serial port
#
################################################################################
import asyncio
import logging
import time
import serial

from aioconsole import aprint


VALID_RESPONSES = ('OK', 'ERROR', 'AT+OK', 'AT+ERROR')

class SerialTransport():

    '''connect to the device via serial port'''

    def __init__(self, comport):
        logging.info('Connecting to serial port on com port {}'.format(comport))
        self.in_progress = True
        self.serial = serial.Serial(comport, baudrate=115200, writeTimeout=3)

    def is_connected(self):
        '''True if device is successfully connected False otherwise'''
        return self.serial.is_open

    def send_and_wait_response(self, at_command):
        '''send AT command and wait for the device response,
        if device has not respond within Timeout, error is raised

        :return  payload (dict) empty dict if not payload
                 success (bool) whether device returned error or ok code
        '''
        self.send(at_command)
        logging.debug('Sending command to device \"{}\"'.format(at_command.command.strip()))
        payload, code = self.parse_response(
            self.get_response_from_the_device())
        return payload, code

    def send(self, at_command):
        '''send one AT command to the device'''
        self.serial.reset_input_buffer()
        try:
            self.serial.write(at_command.command.encode('utf-8'))
        except serial.SerialTimeoutException:
            print("Failed to send AT Command to the device")


    async def async_check_for_device_responses(self):
        '''asynchronously check for any messages coming from the device.
        any response from the device will be printed to the console.
        '''
        while self.in_progress:
            if not self.is_connected:
                break
            if self.serial.in_waiting:
                line = self.serial.readline()
                if isinstance(line, (bytes, bytearray)):
                    line = line.decode('utf-8')
                print(line.rstrip())
            await asyncio.sleep(0.1)


    def get_response_from_the_device(self, timeout=4):
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
                return [f'Device did not respond: Timeout time {timeout} sec', 'ERROR']
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
        payload = SerialTransport.get_payload_from_std_out(std_out) if std_out else None
        return payload, response_code

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
