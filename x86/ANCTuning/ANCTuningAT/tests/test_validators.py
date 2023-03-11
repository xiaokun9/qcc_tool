################################################################################
#
#  test_validators.py
#
#  Copyright (c) 2019 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
#
################################################################################
from py_anc_calibration.input_validators import Key32BitValidator, ANCModeValidator, GainPathValidator, \
    GainValueValidator, YesNoResponseValidator, CalibrationActionsValidator


def test_32_bit_key_validator():
    valid_input_1 = '00001111222233334444555566667777'
    valid_input_2 = '12345678901234567890123456789012'
    invalid_input_1 = 'o0001111222233334444555566667777'
    invalid_input_2 = '1234567890123456789012345678901'

    validator = Key32BitValidator()
    assert validator.is_valid(valid_input_1)
    assert validator.is_valid(valid_input_2)
    assert not validator.is_valid(invalid_input_1)
    assert not validator.is_valid(invalid_input_2)

def test_anc_mode_validator():
    validator = ANCModeValidator()

    valid_input_1 = '1'
    valid_input_2 = 7
    valid_input_3 = 1
    valid_input_4 = '10'

    invalid_input_1 = 0
    invalid_input_2 = '11'
    invalid_input_3 = ['7']
    invalid_input_4 = object()
    invalid_input_5 = 'one'

    assert validator.is_valid(valid_input_1)
    assert validator.is_valid(valid_input_2)
    assert validator.is_valid(valid_input_3)
    assert validator.is_valid(valid_input_4)

    assert not validator.is_valid(invalid_input_1)
    assert not validator.is_valid(invalid_input_2)
    assert not validator.is_valid(invalid_input_3)
    assert not validator.is_valid(invalid_input_4)
    assert not validator.is_valid(invalid_input_5)

def test_gain_path_validator():
    validator = GainPathValidator()

    valid_input_1 = '1'
    valid_input_2 = 2
    valid_input_3 = 3
    valid_input_4 = '3'

    invalid_input_1 = 0
    invalid_input_2 = '4'
    invalid_input_3 = ['2']
    invalid_input_4 = object()
    invalid_input_5 = 'four'

    assert validator.is_valid(valid_input_1)
    assert validator.is_valid(valid_input_2)
    assert validator.is_valid(valid_input_3)
    assert validator.is_valid(valid_input_4)

    assert not validator.is_valid(invalid_input_1)
    assert not validator.is_valid(invalid_input_2)
    assert not validator.is_valid(invalid_input_3)
    assert not validator.is_valid(invalid_input_4)
    assert not validator.is_valid(invalid_input_5)

def test_gain_value_validator():
    validator = GainValueValidator()

    valid_input_1 = '0'
    valid_input_2 = 255
    valid_input_3 = 174
    valid_input_4 = '11'

    invalid_input_1 = -1
    invalid_input_2 = '256'
    invalid_input_3 = ['17']
    invalid_input_4 = object()
    invalid_input_5 = 'twelve'

    assert validator.is_valid(valid_input_1)
    assert validator.is_valid(valid_input_2)
    assert validator.is_valid(valid_input_3)
    assert validator.is_valid(valid_input_4)

    assert not validator.is_valid(invalid_input_1)
    assert not validator.is_valid(invalid_input_2)
    assert not validator.is_valid(invalid_input_3)
    assert not validator.is_valid(invalid_input_4)
    assert not validator.is_valid(invalid_input_5)


def test_yes_no_response_validator():

    validator = YesNoResponseValidator()

    valid_input_0 = 'yes'
    valid_input_1 = 'Yes'
    valid_input_2 = 'Y'
    valid_input_3 = 'Yep'
    valid_input_4 = 'No'
    valid_input_5 = 'Nope'
    valid_input_6 = 'n'

    invalid_input_0 = '25'
    invalid_input_1 = 25
    invalid_input_2 = 'Nes'
    invalid_input_3 = 1

    assert validator.is_valid(valid_input_0)
    assert validator.is_valid(valid_input_1)
    assert validator.is_valid(valid_input_2)
    assert validator.is_valid(valid_input_3)
    assert validator.is_valid(valid_input_4)
    assert validator.is_valid(valid_input_5)
    assert validator.is_valid(valid_input_6)

    assert not validator.is_valid(invalid_input_0)
    assert not validator.is_valid(invalid_input_1)
    assert not validator.is_valid(invalid_input_2)
    assert not validator.is_valid(invalid_input_3)

def test_main_calibration_loop_calibrator():

    validator = CalibrationActionsValidator()

    valid_input_1 = 'M'
    valid_input_2 = 'm' # means enable
    valid_input_3 = 'd'
    valid_input_4 = 'D'
    valid_input_5 = 'P'
    valid_input_6 = 'p'
    valid_input_7 = 'X'
    valid_input_8 = 'x'
    valid_input_9 = 'E'
    valid_input_10 = 'e'
    valid_input_11 = '0'
    valid_input_12 = '255'
    valid_input_13 = 0
    valid_input_14 = 255
    valid_input_15 = '25'


    invalid_input_1 = '256'
    invalid_input_2 = 256
    invalid_input_3 = 'H'
    invalid_input_4 = 'quit'

    assert validator.is_valid(valid_input_1)
    assert validator.is_valid(valid_input_2)
    assert validator.is_valid(valid_input_3)
    assert validator.is_valid(valid_input_4)
    assert validator.is_valid(valid_input_5)
    assert validator.is_valid(valid_input_6)
    assert validator.is_valid(valid_input_7)
    assert validator.is_valid(valid_input_8)
    assert validator.is_valid(valid_input_9)
    assert validator.is_valid(valid_input_10)
    assert validator.is_valid(valid_input_11)
    assert validator.is_valid(valid_input_12)
    assert validator.is_valid(valid_input_13)
    assert validator.is_valid(valid_input_14)
    assert validator.is_valid(valid_input_15)

    assert not validator.is_valid(invalid_input_1)
    assert not validator.is_valid(invalid_input_2)
    assert not validator.is_valid(invalid_input_3)
    assert not validator.is_valid(invalid_input_4)
