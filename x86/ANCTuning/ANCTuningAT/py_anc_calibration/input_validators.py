################################################################################
#
#  input_validators.py
#
#  Copyright (c) 2019 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
#  Validators to validate user-provided data.
#
################################################################################
# Python imports
from abc import ABC, abstractmethod

from doc_inherit import class_doc_inherit


class AbstractInputValidator(ABC):
    """Base ABC for all validators.
    """

    @property
    @abstractmethod
    def expected_input(self):
        '''Return a string description of an expected input.
        '''

    @abstractmethod
    def is_valid(self, data_input):
        '''Return True if data_input is valid, otherwise False.
        '''


@class_doc_inherit
class Key32BitValidator(AbstractInputValidator):
    """Validate a 32-bit auth key.
    """

    @property
    def expected_input(self):
        '''A 32-bit digit only key.
        '''
        return '32-bit digit only key'

    def is_valid(self, data_input: str):
        if data_input.isdigit() and len(data_input) == 32:
            return True
        return False


@class_doc_inherit
class ANCModeValidator(AbstractInputValidator):
    """The ANC mode value validator.
    """

    @property
    def expected_input(self):  # docstring is for docs purpose
        '''The ANC modes range from 1 to 10.
        '''
        return 'ANC modes ranging from 1 to 10'

    def is_valid(self, data_input):
        if not isinstance(data_input, (int, str)):
            return False
        if isinstance(data_input, str) and not data_input.isdigit():
            return False
        data_input = int(data_input)
        return bool(data_input in range(1, 10 + 1))  # 10 is valid, 11 not


@class_doc_inherit
class GainPathValidator(AbstractInputValidator):
    """A Gain path valdiator.
    """

    @property
    def expected_input(self):  # docstring is for docs purpose
        '''FFA (value 1), FFB (value 2) or FB (value 3).
        '''
        return 'FFA=1 FFB=2 and FB=3 '

    def is_valid(self, data_input):
        if not isinstance(data_input, (int, str)):
            return False
        if isinstance(data_input, str) and not data_input.isdigit():
            return False
        data_input = int(data_input)
        return bool(data_input in range(1, 3 + 1))  # 3 is valid, 4 not


@class_doc_inherit
class GainValueValidator(AbstractInputValidator):
    """A Gain Value validator.
    """

    @property
    def expected_input(self):  # docstring is for docs purpose
        '''A Value ranging from 0 to 255.
        '''
        return 'Gain value ranging from 0 to 255'

    def is_valid(self, data_input):
        if not isinstance(data_input, (int, str)):
            return False
        if isinstance(data_input, str) and not data_input.isdigit():
            return False
        data_input = int(data_input)
        return bool(data_input in range(0, 255 + 1))  # 255 is valid, 256 not


@class_doc_inherit
class YesNoResponseValidator(AbstractInputValidator):
    '''Yes/No response validator
    '''

    @property
    def yes_responses(self):
        '''
        list of lowercase yes responses
        '''
        return ['yes', 'y', 'yeah', 'yep']

    @property
    def no_responses(self):
        '''
        list of lowercase no responses
        '''
        return ['no', 'n', 'nope']

    @property
    def expected_input(self):
        '''Yes/y/yep/yes/yeah for yes.
        No/no/n/nope for no
        '''
        return 'Yes/y/yep/yes/yeah for yes. No/no/n/nope for no'

    def is_valid(self, data_input: str):
        if not isinstance(data_input, str):
            return False
        if data_input.lower() in self.yes_responses or data_input.lower() in self.no_responses:
            return True
        return False


@class_doc_inherit
class CalibrationActionsValidator(AbstractInputValidator):
    """A calibration action validator.
    """


    @property
    def expected_input(self):
        return '\'M\' to change ANC mode; \'P\' to change fine gain path;' \
               '\'E\' to enable ANC; \'D\' to disable ANC; \'X\' to exit calibration loop; ' \
               'Or number in range 0-255 to set fine gain value;'



    def is_valid(self, data_input):
        data_input = str(data_input).lower()
        valid_responses = ['m', 'p', 'e', 'd', 'x']
        fine_gain_numbers_validator = GainValueValidator()

        return bool(data_input in valid_responses or
                    fine_gain_numbers_validator.is_valid(data_input))
