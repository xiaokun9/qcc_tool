################################################################################
#
#  at_anc_commands.py
#
#  Copyright (c) 2020 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
#  AT Commands
#
################################################################################
class ATCommand:
    '''defines a AT command'''

    def __init__(self, command: str):
        self.command = command
        self.prefix = '\r'
        self.postfix = '\r\n'


    def __str__(self):
        '''returns a plain text of the command'''
        return self.prefix + str(self.command) + self.postfix


class ATCommands:

    @staticmethod
    def at_ancdisable():
        return ATCommand('AT+ANCDISABLE')

    @staticmethod
    def at_ancenable(mode: int):
        return ATCommand('AT+ANCENABLE=' + str(mode))

    @staticmethod
    def at_ancreadfinegain(mode: int, gainpath: int):
        return ATCommand('AT+ANCREADFINEGAIN=' + str(mode) + ',' + str(gainpath))

    @staticmethod
    def at_ancsetfinegain(mode: int, gainpath: int, gainvalue: int):
        return ATCommand('AT+ANCSETFINEGAIN=' + str(mode) + ',' + str(gainpath) + ',' + str(gainvalue))

    @staticmethod
    def at_ancwritefinegain(mode: int, gainpath: int, gainvalue: int):
        return ATCommand('AT+ANCWRITEFINEGAIN=' + str(mode) + ',' + str(gainpath) + ',' + str(gainvalue))

    @staticmethod
    def at_authdisable():
        return ATCommand('AT+AUTHDISABLE')

    @staticmethod
    def at_authresp(response):
        return ATCommand('AT+AUTHRESP=' + str(response))

    @staticmethod
    def at_authstart():
        return ATCommand('AT+AUTHSTART')

    @staticmethod
    def at_dtsendtesting(reboot: int):
        return ATCommand('AT+DTSENDTESTING=' + str(reboot))

    @staticmethod
    def at_dtssettestmode(testmode: int):
        return ATCommand('AT+DTSSETTESTMODE=' + str(testmode))

    @staticmethod
    def at_dtstestmode_():
        return ATCommand('AT+DTSTESTMODE?')

    @staticmethod
    def at_localbdaddr_():
        return ATCommand('AT+LOCALBDADDR?')

