################################################################################
#
#  test_calibrator.py
#
#  Copyright (c) 2019-2020 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
#
################################################################################
import pytest
from mock import MagicMock, Mock

from py_anc_calibration.calibrator import ANCCalibrator, ANCTuneProperties


@pytest.fixture
def session():
    fake_session = MagicMock()
    yield fake_session
    fake_session.reset_mock()


def test_anc_is_enabled_is_none_by_default(session):
    '''we cannot grantee whether ANC is ON/OFF when we start calibrating ANC'''
    calibrator = ANCCalibrator(session)
    assert calibrator.device_anc_tune_data.anc_is_enabled is None


def test_calibrator_tries_to_get_device_gain_value_for_given_mode_and_path_shows_error_if_device_returns_error(session):
    session.view.show_message = MagicMock()
    session.transport.execute = MagicMock(return_value = (None, False))
    calibrator = ANCCalibrator(session)
    calibrator.read_fine_gain_for_current_mode_and_path()
    assert 'error' in  session.view.show_message.call_args_list[0][0][0].lower()

def test_calibrator_tries_to_get_device_gain_value_for_given_mode_and_path_than_current_anc_gain_value_updates_if_device_return_ok_code(session):
    session.transport.execute = MagicMock(return_value=({'+ANCREADFINEGAIN':122}, True))
    calibrator = ANCCalibrator(session)

    calibrator.read_fine_gain_for_current_mode_and_path()
    assert calibrator.device_anc_tune_data.gain == 122

def test_calibrator_tries_to_enable_anc_for_given_mode_and_path_shows_error_if_device_returns_error(session):
    session.view.show_message = MagicMock()
    session.transport.execute = MagicMock(return_value = (None, False))
    calibrator = ANCCalibrator(session)

    calibrator.enable_anc_for_current_anc_mode()
    assert 'error' in  session.view.show_message.call_args_list[0][0][0].lower()

def test_calibrator_tries_to_enable_anc_for_given_mode_than_current_anc_enable_anc_field_is_true_if_device_return_ok_code(session):
    session.transport.execute = MagicMock(return_value=(None, True))
    calibrator = ANCCalibrator(session)

    calibrator.enable_anc_for_current_anc_mode()
    assert calibrator.device_anc_tune_data.anc_is_enabled

def test_calibrator_tries_to_disable_anc_shows_error_if_device_returns_error(session):
    session.view.show_message = MagicMock()
    session.transport.execute = MagicMock(return_value = (None, False))
    calibrator = ANCCalibrator(session)

    calibrator.disable_anc()
    assert 'error' in  session.view.show_message.call_args_list[0][0][0].lower()

def test_calibrator_tries_to_disable_anc_than_current_anc_enable_anc_field_is_false_if_device_return_ok_code(session):
    session.transport.execute = MagicMock(return_value=(None, True))
    calibrator = ANCCalibrator(session)

    calibrator.disable_anc()
    assert not calibrator.device_anc_tune_data.anc_is_enabled

def test_calibrator_tries_set_fine_gain_for_given_mode_and_path_shows_error_if_device_returns_error(session):
    session.view.show_message = MagicMock()
    session.transport.execute = MagicMock(return_value=(None, False))
    calibrator = ANCCalibrator(session)

    calibrator.set_fine_grain(12)
    assert 'error' in session.view.show_message.call_args_list[0][0][0].lower()


def test_calibrator_tries_to_set_fine_gain_than_current_set_fine_gain_value_field_is_updated_if_device_return_ok_code(session):
    session.transport.execute = MagicMock(return_value=(None, True))
    calibrator = ANCCalibrator(session)

    calibrator.set_fine_grain(25)
    assert calibrator.device_anc_tune_data.gain == 25


def test_calibrator_show_current_mode_path_and_gain_value_as_unknown_if_gain_value_is_not_provided(session):
    session.view.show_message = MagicMock()
    calibrator = ANCCalibrator(session)
    calibrator.device_anc_tune_data = ANCTuneProperties(mode=1, path=3)
    calibrator.show_current_anc_tune_data()
    assert 'gain:unknown' in session.view.show_message.call_args_list[0][0][0].lower()


def test_calibrator_show_current_mode_path_and_gain_value(session):
    session.view.show_message = MagicMock()
    calibrator = ANCCalibrator(session)
    calibrator.device_anc_tune_data = ANCTuneProperties(mode=1, path=3, gain=24)
    calibrator.show_current_anc_tune_data()
    assert 'gain:24' in session.view.show_message.call_args_list[0][0][0].lower()

def test_write_fine_gain_values_shows_error_if_current_tune_data_is_none(session):
    session.view.show_message = MagicMock()
    calibrator = ANCCalibrator(session)
    calibrator.device_anc_tune_data.anc_is_enabled = True
    calibrator.write_audio_key()
    assert 'error' in session.view.show_message.call_args_list[0][0][0].lower()

def test_write_fine_gain_values_shows_error_if_device_return_error(session):
    session.view.show_message = MagicMock()
    session.transport.execute = MagicMock(return_value=(None, False))
    calibrator = ANCCalibrator(session)

    calibrator.write_audio_key()
    assert 'error' in session.view.show_message.call_args_list[0][0][0].lower()

def test_write_fine_gain_values_returns_true_if_device_return_success_response(session):
    session.view.show_message = MagicMock()
    session.transport.execute = MagicMock(return_value=(None, True))
    calibrator = ANCCalibrator(session)
    calibrator.device_anc_tune_data.anc_is_enabled = True
    calibrator.device_anc_tune_data.gain = 12

    assert calibrator.write_audio_key()


def test_that_if_user_select_change_mode_and_current_fine_gain_value_is_not_none_write_anc_data_call_will_be_made(session):
    session.view.request_data_from_user = Mock(side_effect=('m', '2'))
    session.transport.execute = MagicMock(return_value=({'+ANCREADFINEGAIN':122}, True))

    calibrator = ANCCalibrator(session)
    calibrator.device_anc_tune_data.gain = 12
    calibrator.write_audio_key = MagicMock()

    calibrator.start_main_calibration_loop()
    calibrator.write_audio_key.assert_called_once()


def test_that_if_user_selects_change_mode_and_current_fine_gain_value_is_none_write_anc_data_call_will_not_be_made(session):
    session.view.request_data_from_user = Mock(side_effect=('m', '2'))
    session.transport.execute = MagicMock(return_value=({'+ANCREADFINEGAIN': 122}, True))

    calibrator = ANCCalibrator(session)
    calibrator.device_anc_tune_data.gain = None
    calibrator.write_audio_key = MagicMock()

    calibrator.start_main_calibration_loop()
    calibrator.write_audio_key.assert_not_called()

def test_that_if_user_changes_path_and_read_gain_value_fails_than_current_gain_value_is_none(session):
    session.view.request_data_from_user = Mock(side_effect=('p', '2'))
    session.transport.execute = MagicMock(return_value=(None, False))

    calibrator = ANCCalibrator(session)
    calibrator.device_anc_tune_data.gain = None
    calibrator.write_audio_key = MagicMock()

    calibrator.start_main_calibration_loop()
    calibrator.write_audio_key.assert_not_called()
    session.transport.execute.assert_called()

    assert calibrator.device_anc_tune_data.gain is None
    assert calibrator.device_anc_tune_data.path == 2

def test_that_if_user_changes_mode_and_read_gain_value_fails_than_current_gain_value_is_none(session):
    session.view.request_data_from_user = Mock(side_effect=('m', '7'))
    session.transport.execute = MagicMock(return_value=(None, False))

    calibrator = ANCCalibrator(session)
    calibrator.device_anc_tune_data.gain = None
    calibrator.write_audio_key = MagicMock()

    calibrator.start_main_calibration_loop()
    calibrator.write_audio_key.assert_not_called()
    session.transport.execute.assert_called()

    assert calibrator.device_anc_tune_data.gain is None
    assert calibrator.device_anc_tune_data.mode == 7

def test_anc_mode_is_printed_nicely_when_anc_propertis_are_printed():
    anc_properties = ANCTuneProperties()
    assert 'ANC Enabled:UNKNOWN' in str(anc_properties)
    anc_properties.anc_is_enabled = True
    assert 'ANC Enabled:ON' in str(anc_properties)
    anc_properties.anc_is_enabled = False
    assert 'ANC Enabled:OFF' in str(anc_properties)

def test_if_user_exits_calibration_loop_disable_anc_functionality_function_will_be_called(session):
    calibrator = ANCCalibrator(session)
    calibrator.authenticate_device = Mock()
    calibrator.read_fine_gain_for_current_mode_and_path = Mock()
    calibrator.disable_anc_calibration = MagicMock()
    session.view.request_data_from_user = Mock(return_value='x')
    calibrator.calibrate()

    calibrator.disable_anc_calibration.assert_called()

def test_if_user_types_number_from_0_to_255_while_in_calibration_loop_the_set_function_will_be_called_with_typed_number(session):
    calibrator = ANCCalibrator(session)
    session.view.request_data_from_user = Mock(return_value='15')
    calibrator.set_fine_grain = MagicMock()
    calibrator.start_main_calibration_loop()
    calibrator.set_fine_grain.assert_called_once_with('15')

def test_that_if_anc_is_disabled_and_user_sets_fine_gain_value_anc_enable_function_will_be_called(session):
    calibrator = ANCCalibrator(session)
    calibrator.device_anc_tune_data.anc_is_enabled = False
    calibrator.enable_anc_for_current_anc_mode = MagicMock()
    session.transport.execute = MagicMock(return_value=(None, False))

    calibrator.set_fine_grain(15)
    calibrator.enable_anc_for_current_anc_mode.assert_called_once_with()

def test_that_if_anc_is_disabled_and_user_write_data_to_device_memory_anc_enable_function_will_be_called(session):
    calibrator = ANCCalibrator(session)
    calibrator.device_anc_tune_data.anc_is_enabled = False
    calibrator.enable_anc_for_current_anc_mode = MagicMock()
    session.transport.execute = MagicMock(return_value=(None, False))

    calibrator.write_audio_key()
    calibrator.enable_anc_for_current_anc_mode.assert_called_once_with()

def test_that_if_mode_is_changed_read_fine_gain_value_will_be_called_iff_enable_anc_for_new_call_will_be_made(session):
    calibrator = ANCCalibrator(session)
    session.transport.execute = MagicMock(side_effect=((None, True), ({'+ANCREADFINEGAIN':122}, True)))
    session.view.request_data_from_user = Mock(return_value='7')
    calibrator.set_new_anc_mode()

    assert calibrator.device_anc_tune_data.anc_is_enabled is True

def test_that_if_mode_is_path_read_fine_gain_value_will_be_called_iff_enable_anc_for_new_call_will_be_made(session):
    calibrator = ANCCalibrator(session)
    session.transport.execute = MagicMock(side_effect=((None, True), ({'+ANCREADFINEGAIN':122}, True)))
    session.view.request_data_from_user = Mock(return_value='2')
    calibrator.set_gain_path()

    assert calibrator.device_anc_tune_data.anc_is_enabled is True
