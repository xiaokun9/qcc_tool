################################################################################
#
#  __main__.py
#
#  Copyright (c) 2019 Qualcomm Technologies International, Ltd.
#  All Rights Reserved.
#  Qualcomm Technologies International, Ltd. Confidential and Proprietary.
#
#  Entry point for py_anc_calibration
#
################################################################################
import argparse
import logging
import os
import sys

from py_anc_calibration.calibrator import ANCCalibrator
from py_anc_calibration.session import ANCSessionBuilder


def start_calibration(session, **settings) -> int:
    """Invoke the calibration api with supplied session and command line
    arguments.
    """
    session.connect_device(**settings)
    # to do add check whether connection is established
    anc_calibrator = ANCCalibrator(session)
    anc_calibrator.calibrate()
    return 0


def create_anc_tuning_session():
    '''Create anc session.

    User must specify device properties that are required to connect to the device.
    '''
    session_builder = ANCSessionBuilder()
    args = parse_args(sys.argv[1:])
    session_builder.add_transport(args.transport)
    session_builder.add_anc_commands(args.commands)
    session_builder.add_user_gateway(args.view)
    session = session_builder.get_session()
    device_settings = dict(args.settings)
    if args.logs:
        logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))
    return session, device_settings


def parse_args(args) -> argparse.ArgumentParser:
    """Parses the command line arguments, returning a ArgumentParser object.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--transport", help='transport to be used. Options: '
                        + str(ANCSessionBuilder.get_available_transport()), dest='transport',
                        default='serial')
    parser.add_argument("--anc_commands", help='set of commands to calibrate ANC. Options:'
                        + str(ANCSessionBuilder.get_available_anc_commands()),
                        dest='commands', default='at')
    parser.add_argument("--view", help='user view. Options:'
                        + str(ANCSessionBuilder.get_available_views()), dest='view', default='cli')
    parser.add_argument("--device_settings", nargs='+', required=True,
                        type=lambda kv: kv.split("=", 1), dest='settings')
    parser.add_argument("--v", '-verbose', required=False,action='store_true',
                        help='enable logs', dest='logs')

    parsed_args = parser.parse_args(args)
    if any(len(setting_key_value_pair) < 2 for setting_key_value_pair in parsed_args.settings):
        raise ValueError('Values for device_settings must be given in the form "KEY=VALUE"')
    return parsed_args


def main() -> int:
    """Command line entry point.
    """
    session, device_settings = create_anc_tuning_session()
    return start_calibration(session, **device_settings)


if __name__ == '__main__':
    sys.exit(main())
