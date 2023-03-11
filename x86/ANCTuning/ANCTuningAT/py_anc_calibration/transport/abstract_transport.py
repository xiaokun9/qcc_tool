################################################################################
#
#  abstract_transport.py
#
#  Copyright (c) 2019 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
#  Abstract Transport
#
################################################################################
from abc import ABC, abstractmethod

class AbstractTransport(ABC):

    '''defines an abstract transport protocol'''

    @abstractmethod
    def connect(self, **settings):
        '''connect to the device'''

    @abstractmethod
    def disconnect(self):
        '''disconnect form the device'''

    @abstractmethod
    def execute(self, command):
        '''send a command to the device'''
