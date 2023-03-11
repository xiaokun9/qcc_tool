################################################################################
#
#  abstract_view.py
#
#  Copyright (c) 2019 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
#  Abstract View
#
################################################################################
from abc import ABC, abstractmethod


class AbstractView(ABC):
    '''defines set of Abstract View properties'''

    @abstractmethod
    def start(self):
        '''start view. E.g show welcome message'''

    @abstractmethod
    def end(self):
        '''end view. Make a cleanup and show goodbye message'''

    @abstractmethod
    def request_data_from_user(self, message, validator=None, if_canceled_callback=None):
        '''show message and get user input

        :arg message (str): message to show user
             validator (AbstractInputValidator): validator for input,
                                                 if None no input validation will be done
             if_canceled_callback (callable): callback to be executed if user cancel operation,
                                              if None cancel option should not be provided to user
        '''

    @abstractmethod
    def show_message(self, message):
        '''show message to user'''
