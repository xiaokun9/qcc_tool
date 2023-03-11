################################################################################
#
#  dts_at_terminal.py
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
from collections import namedtuple


from CryptoPlus.Cipher import python_AES as AES
from pathlib import Path

from .command_line_view import CommandLineView
from .serial_transport import SerialTransport


AT_COMMAND_POSTFIX = '\r\n'

from aioconsole import ainput
ATCommand = namedtuple("ATCommand", "command")

KEY_FILE_PATH = str(Path(__file__).parent / "unlock.key")

class ATCommandTest():
    """This class sends AT Command to the device and reports
    the results
    """
    def __init__(self, comport: str):
        self.view = CommandLineView()
        try:
            self.transport = SerialTransport(comport)
        except Exception as e:
            self.view.show_message("Failed connect to the device")
            self.view.show_message(str(e))
            sys.exit(0)

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
        """authenticates connected device"""
        key = self.get_key()
        self.aes = AES.new(key, AES.MODE_CMAC)
        at_auth_start = ATCommand('AT+AUTHSTART' + AT_COMMAND_POSTFIX)
        response, success = self.transport.send_and_wait_response(at_auth_start)
        if success != "OK":
            return False
        random = response['+AUTHSTART']
        random = codecs.decode(random, 'hex')
        enc = self.aes.encrypt(random)
        enc_str = codecs.encode(enc, "hex")
        auth_resp = ATCommand('AT+AUTHRESP=' + enc_str.decode('utf-8').upper() +  AT_COMMAND_POSTFIX)
        _, success = self.transport.send_and_wait_response(auth_resp)
        if  success != "OK":
            return False
        return True


    def send_one_at_command(self, at_command: str):
        """Starts at command testing
        """
        if not self.authenticate_device():
            self.view.show_message('Failed to authenticate device; (Try to change key)')
            return
        at_command = ATCommand(at_command + AT_COMMAND_POSTFIX)
        response, response_code = self.transport.send_and_wait_response(at_command)
        self.view.show_message("Response Code: {}, "
                               "Response values: {}".format(response_code, response))

    async def async_send_at_commands(self):
        '''sends commands typed by the user in the terminal.Non-blocking'''
        self.view.show_message("Authenticating the device...")
        is_authenticated = self.authenticate_device()
        if not is_authenticated:
            self.view.show_message('Failed to authenticate device; (Try to change key)')
            self.transport.in_progress = False
            return

        self.view.show_message("Success!")
        self.view.start()
        self.view.show_message("type 'exit' to exit")
        while self.transport.is_connected():
            # await ainput("") is non-blocking operation
            # if user is inactive async will jump to another async func in the loop
            user_command = await ainput("")
            if not user_command:
                continue
            if user_command == "exit":
                self.transport.in_progress = False
                break
            at_command = ATCommand(user_command + AT_COMMAND_POSTFIX)
            self.transport.send(at_command)
