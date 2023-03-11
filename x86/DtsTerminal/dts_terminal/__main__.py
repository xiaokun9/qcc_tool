################################################################################
#
#  __main__.py
#
#  Copyright (c) 2021 Qualcomm Technologies International, Ltd.
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
import asyncio

from .dts_at_terminal import ATCommandTest


async def async_main():
    """Command line entry point.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--comport", help='Serial comport', dest='comport', required=True)
    parser.add_argument("--command", '-c', help='Serial comport', dest='command', required=False, default='')
    parser.add_argument("--v", '-verbose', required=False,action='store_true',
                        help='enable logs', dest='logs')
    parsed_args = parser.parse_args(sys.argv[1:])
    if parsed_args.logs:
        logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))

    at_command_shell = ATCommandTest(parsed_args.comport)
    if parsed_args.command:
        at_command_shell.send_one_at_command(parsed_args.command)
        return
    loop = asyncio.get_event_loop()
    await asyncio.gather(at_command_shell.async_send_at_commands(),
                        at_command_shell.transport.async_check_for_device_responses())


def main():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(async_main())
    except (KeyboardInterrupt):
       print("Exiting... Press Enter to quit")




if __name__ == '__main__':
    main()



