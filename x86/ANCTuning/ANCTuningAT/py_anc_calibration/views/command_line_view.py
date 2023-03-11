################################################################################
#
#  command_live_view.py
#
#  Copyright (c) 2019 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
#  Showing/requesting information to/from the user using console
#
################################################################################
import sys

from py_anc_calibration.views.abstract_view import AbstractView


class CommandLineView(AbstractView):

    '''defines a command line interface for ANC calibration'''

    def __init__(self):
        self._output = sys.stdout.write
        self._request_data = input

    def start(self):
        '''show welcome message'''
        welcome_message = '\n=============================================\n' \
                          '++++++++++++++++ANC CALIBRATION++++++++++++++\n' \
                          '=============================================\n'

        instructions_message = '\nFollow instructions below to calibrate device.\n' \
                               'Otherwise press \'Ctrl+C\' to leave at any moment\n\n'
        self._output(welcome_message)
        self._output(instructions_message)

    def end(self):
        '''show goodbye message'''
        end_message = '\n==============================================\n' \
                      '++++++++++++ANC CALIBRATION GOODBYE+++++++++++\n' \
                      '==============================================\n'
        self._output(end_message)

    def show_message(self, message):
        '''show message to the user'''
        self._output(message + '\n')

    def request_data_from_user(self, message, validator=None, if_canceled_callback=None):
        '''show message and get user input

        :arg message (str): message to show user
             validator (AbstractInputValidator): validator for input,
                                                 if None no input validation will be done
             if_canceled_callback (callable): callback to be executed if user cancel operation,
                                              if None 'exit' input will be treated as general input
        '''
        if if_canceled_callback is not None:
            message = message + '(or type \'exit\' to leave) '
        while True:
            user_response = self._request_data(message + ': ')
            if if_canceled_callback is not None and user_response in ('exit'):
                return if_canceled_callback()
            if validator is None or validator.is_valid(str(user_response).lower().strip()):
                return str(user_response).lower().strip()
            self._output('ERROR! Wrong input. Expected: ' + validator.expected_input +
                         '. Got: ' + str(user_response) + '\nTry Again.\n')
