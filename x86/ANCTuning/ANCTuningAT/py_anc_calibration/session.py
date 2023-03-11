################################################################################
#
#  session.py
#
#  Copyright (c) 2019-2020 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
#  Session properties for calibration.
#
################################################################################
from abc import ABC, abstractmethod

from py_anc_calibration.anc_commands.at_anc_commands import ATCommands
from py_anc_calibration.transport.serial_transport import SerialTransport
from py_anc_calibration.views.command_line_view import CommandLineView


class ANCCalibrationSession():

    '''holds properties of the session. E.g. what transport is used'''

    def __init__(self):
        self.transport = None
        self.anc_commands = None
        self.view = None

    def connect_device(self, **settings):
        '''connect to the device'''
        if not self.is_ready():
            raise RuntimeError('ANC Session is not fully configured. '
                               'Missing parameters: ' + str(self.undefined_attributes))
        self.transport.connect(**settings)

    @property
    def undefined_attributes(self):
        '''return list of attributes that are not defined yet'''
        return [name for name, value in vars(self).items() if value is None]

    def is_ready(self):
        '''return true if all properties are set False otherwise'''
        return all(self.__dict__.values())


class AbstractANCSessionBuilder(ABC):

    '''abstact interface for defining a calibration session with different parameters'''

    def __init__(self):
        self._session = ANCCalibrationSession()

    AVAILABLE_TRANSPORT = {}

    AVAILABLE_ANC_COMMANDS = {}

    AVAILABLE_USER_VIEW = {}

    @abstractmethod
    def add_transport(self, transport):
        '''add concrete transport to session object'''

    @abstractmethod
    def add_anc_commands(self, anc_commands):
        '''add concrete set of anc commands to session object'''

    @abstractmethod
    def add_user_gateway(self, user_view):
        '''add concrete user view to session object'''

    def get_session(self):
        '''return session object
        :raise RuntimeError if some properties of session object were not set
        '''
        if not self._session.is_ready():
            raise RuntimeError('Not all parameters have been provided.'
                               'Please add information for ' +
                               str(self._session.undefined_attributes))
        return self._session

    @classmethod
    def get_available_transport(cls):
        '''return list of available transports'''
        return cls.AVAILABLE_TRANSPORT.keys()

    @classmethod
    def get_available_anc_commands(cls):
        '''return list of available anc commands set'''
        return cls.AVAILABLE_ANC_COMMANDS.keys()

    @classmethod
    def get_available_views(cls):
        '''return list of available user views'''
        return cls.AVAILABLE_USER_VIEW.keys()


class ANCSessionBuilder(AbstractANCSessionBuilder):

    '''builds a session with different parameters'''

    AVAILABLE_TRANSPORT = {
        'serial': SerialTransport
    }

    AVAILABLE_ANC_COMMANDS = {
        'at': ATCommands
    }

    AVAILABLE_USER_VIEW = {
        'cli': CommandLineView
    }

    def add_transport(self, transport: str):
        '''add concrete transport mean to the session object
        :arg transport (str): transport name
        :raise KeyError if given transport is unknown
        '''
        if transport not in self.get_available_transport():
            raise KeyError('Unknown transport. Expected: ' + str(self.get_available_transport()) +
                           ' .Got: ' + str(transport))
        self._session.transport = ANCSessionBuilder.AVAILABLE_TRANSPORT[transport]()

    def add_anc_commands(self, anc_commands: str):
        '''add concrete set of anc commands to session object
        :arg anc_commands (str): anc_commands set name
        :raise KeyError if given anc_commands is unknown
        '''
        if anc_commands not in self.get_available_anc_commands():
            raise KeyError('Unknown set of ANC commands. Expected: ' +
                           str(self.get_available_anc_commands()) +
                           ' .Got: ' + str(anc_commands))
        self._session.anc_commands = ANCSessionBuilder.AVAILABLE_ANC_COMMANDS[anc_commands]()

    def add_user_gateway(self, user_view: str):
        '''add concrete user view to session object
        :arg user_view (str): view name
        :raise KeyError if given view is unknown
        '''
        if user_view not in self.get_available_views():
            raise KeyError('Unknown view. Expected: ' + str(self.get_available_views()) +
                           ' .Got: ' + str(user_view))
        self._session.view = ANCSessionBuilder.AVAILABLE_USER_VIEW[user_view]()
