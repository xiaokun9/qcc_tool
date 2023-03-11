################################################################################
#
#  test_command_line_view.py
#
#  Copyright (c) 2019 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
#
################################################################################

from py_anc_calibration.views.command_line_view import CommandLineView


def test_comand_line_view_can_ask_user_for_input():
    clv = CommandLineView()

    def mock_input(text):
        global console_text
        console_text = text
        return '12'

    clv._request_data = mock_input
    user_response = clv.request_data_from_user('Papers please')
    global console_text
    assert console_text == 'Papers please: '
    assert user_response == '12'




