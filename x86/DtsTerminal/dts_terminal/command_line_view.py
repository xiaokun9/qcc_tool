################################################################################
#
#  command_line_view.py
#
#  Copyright (c) 2021 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
#  Showing/requesting information to/from the user using console
#
################################################################################
import sys


class CommandLineView():

    '''defines a command line interface for AT commands'''

    def start(self):
        '''show welcome message'''
        welcome_message = '\n=============================================\n' \
                          '+++++++++++ENTER AT COMMANDS BELOW+++++++++++\n' \
                          '=============================================\n'
        sys.stdout.write(welcome_message)

    def end(self):
        '''show goodbye message'''
        end_message = '\n==============================================\n' \
                      '++++++++++++++++++++GOODBYE+++++++++++++++++++\n' \
                      '==============================================\n'
        sys.stdout.write(end_message)

    def show_message(self, message):
        '''show message to the user'''
        sys.stdout.write(message + '\n')

    def request_data_from_user(self, message):
        '''show message and get user input

        :arg message (str): message to show user
        '''
        user_response = input(message + ': ')
        return str(user_response)
