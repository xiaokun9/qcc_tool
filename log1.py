"""Desk based script for logging pydbg devices

The output to the console includes colour highlighting. This can be configured
by editing the list of calls to logger.add_highlight in this script.

Devices are configured in log_setup.py. You need to specify the devices connection
and the firmware files you are interested in.

Log files are created by default, timestamped at the time you start execution.
"""

import time
import colorama
import re
import sys
import bisect
import atexit
import os

from PyQt5 import QtWidgets

sys.path.append(r"../utils")

from csr.front_end.pydbg_front_end import PydbgFrontEndBase
from csr.transport.trbtrans import TrbErrorBridgeLinkIsDown, TrbErrorDriverIOFailed
from csr.dev.hw.port_connection import ReadFailureSubsystemInaccessible, ReadFailureDUTInaccessible, ReadFailureLinkInvalid, ReadFailureSubsystemInaccessible, ReadFailure
from csr.wheels.bitsandbobs import AnsiColourCodes
from datetime import datetime
from datetime import timedelta
   


os.environ["PYDBG_FIRMWARE_LOOKUP_DISABLED"] = "TRUE" 

device_options = [
    {
        'name' : "EB1",
        'name_color' : "brightblue",
        'default_color' : "brightgreen",
        'indent' : 4,
        'log': {'apps1'},
        'device_url' : 'trb:usb2trb:193661',
        'firmware_builds' : r'apps1:C:\Users\cx\Desktop\qcc\earbud.elf',
        'target' : None,
        'preload' : True
    },
    
]

def handle_arguments():
    import argparse
    global args

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--nolog', default = False, action = "store_true",
                        help="[Optional] Disable log file creation")
    args = parser.parse_args()

class Earbud(object):

    def __init__(self, chip):
        self._chip = chip

    def __setitem__(self, name, value):
        self.__dict__[name] = value

class EarbudsLogger(object):

    class EarbudFakeLogFile(object):
        """
        Class used to avoid conditionals for logging being supported.
        Implements just the write function. If any other file methods are used
        they will require suitable stubs.
        """

        def write(self, str):
            pass

    def _get_colour_attr(self, colour):
        colour = colour.lower()
        try:
            return self._colour.code[colour]
        except KeyError:
            raise AttributeError("Valid colours are: %s" % self._colour.names)

    def _resync_time(self):
        # Read Scarlet timestamp so we can adjust timestamps between multiple Scarlets
        for eb in self.earbuds:
            eb.start_time = eb.trb_log.stream.read_dongle_register(0, 0x1200)
        for eb in self.earbuds:
            eb.base_timestamp = eb.trb_log.stream.read_dongle_register(0, 0x1204) * (2 ** 32)
            eb.start_time += eb.base_timestamp
            eb.datetime = datetime.now()

    def _enable_trb(self, eb):
        try:
            for en in eb.trb_log_enable:
                en.value = 1
        except:
            pass

    def _log_filename_on_exit(self):
        print("Logfile is {filename:s}".format(filename=self._filename))

    def __init__(self, dev_opts, file_logging):
        self._dev_opts = dev_opts
        self.earbuds = []
        self.highlights = []
        self._colour_dict = dict()
        self._colour = AnsiColourCodes()
        self._log_list = []
        self._timestamp_list = []
        self._filename = None
        if file_logging:
            now = datetime.now()
            self._filename = "live_log_py_{:04}{:02}{:02}_{:02}{:02}{:02}.log".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
            self._logfile = open(self._filename,"w")
            atexit.register(self._log_filename_on_exit)
        else:
            self._logfile = self.EarbudFakeLogFile()

        for dev_opt in self._dev_opts:
            # trb logging differs in pylib versions
            log_started = False

            print(colorama.Style.RESET_ALL + self._get_colour_attr('brightyellow') + "Initialising logging on " + dev_opt['name'] + "..." + colorama.Style.RESET_ALL)
            device, trans = PydbgFrontEndBase.attach(dev_opt)
            eb = Earbud(device.chip)
            eb.apps1 = device.chip.apps_subsystem.p1
            eb.apps0 = device.chip.apps_subsystem.p0
            #eb.audio1 = device.chips[0].audio_subsystem.p1
            #eb.audio0 = device.chips[0].audio_subsystem.p0
            eb.curator = device.chip.curator_subsystem.core
            #eb.bt = device.chip.bt_subsystem.core
            eb.name = dev_opt['name']
            eb.name_color = self._get_colour_attr(dev_opt['name_color'])
            eb.default_color = colorama.Style.RESET_ALL + self._get_colour_attr(dev_opt['default_color'])
            eb.indent = dev_opt['indent']
            eb.trb_log = device.chips[0].trb_log
            eb.trb_log_enable = []
            eb.last_timestamp = 0
            eb.last_timestamp_high = 0
            eb.prim_log_file = open(eb.name +"_primlog_{:04}{:02}{:02}_{:02}{:02}{:02}.log".format(now.year, now.month, now.day, now.hour, now.minute, now.second), "w")
            eb.apps1.log_level(4)
            for subsys in dev_opt['log']:
                print(colorama.Style.RESET_ALL + self._get_colour_attr('brightyellow') + "Enabling " + subsys + " logging on " + dev_opt['name'] + "..." + colorama.Style.RESET_ALL)
                en = eval("eb." + subsys + ".fw.gbl.hydra_log_trb_cfg.enable")
                eb.trb_log_enable.append(en)
                eb.log_started = False
                try:
                    eb.trb_log.start(core_nicknames=subsys)
                    eb.log_started = True
                # core_nicknames not supported
                except TypeError:
                    # try core_nickname instead...
                    eb.trb_log.start(core_nickname=subsys)
                    eb.log_started = True
                    pass

            self.earbuds.append(eb)

        self._resync_time()
        print(colorama.Style.RESET_ALL + self._get_colour_attr('brightyellow') + "Logging started at " + str(datetime.now()))
        self._logfile.write("Logging started at " + str(datetime.now()) + "\n")


    def add_highlight(self, regex, color):
        self.highlights.append((re.compile(regex), self._get_colour_attr(color)))

    def log_message(self,mess):
        message = "\n{:s} : {:s}\n".format(time.ctime(),mess)
        sys.stdout.write(message)
        self._logfile.write(message)
    def stop_log(self):
        for eb in self.earbuds:
            #eb.trb_log.start(core_nicknames='apps1')
            eb.trb_log.stop(core_nicknames='apps1')
            eb.log_started = True

    def log(self):

        # Record highest insertion position of log list
        top_insert_pos = -1

        for eb in self.earbuds:
            try:
                prim_log_data = eb.apps1.fw.prim_log.generate_decoded_event_report(return_str=True)
                if len(prim_log_data) > 0:
                    eb.prim_log_file.write(str(datetime.now()) + "\n")
                eb.prim_log_file.write(prim_log_data)

                eb.trb_log.sort(app_decode=True)
                if not eb.log_started:
                    print(colorama.Style.RESET_ALL + self._get_colour_attr('brightyellow') + eb.name + " " + str(datetime.now()) + (" " * eb.indent) + " TRB link is up")
                    self._logfile.write(eb.name + " " + str(datetime.now()) + (" " * eb.indent) + " TRB link is up" + "\n")
                    eb.log_started = True

                # Check if any log entries
                if len(eb.trb_log.tr_log) > 0:
                    # Go through each entry highlighting matching words
                    while eb.trb_log.tr_log:
                        log_entry = eb.trb_log.tr_log.pop(0)
                        text_line = log_entry[1]
                        line = text_line
                        for hl in self.highlights:
                            newline = ""
                            i = 0
                            for m in hl[0].finditer(line):
                                newline += line[i:m.start()] + hl[1] + line[m.start():m.end()] +  eb.default_color
                                i = m.end()
                            line = newline + line[i:]

                        # merge line into global list
                        time = (log_entry[0] + eb.base_timestamp) - eb.start_time
                        pos = bisect.bisect(self._timestamp_list, time)
                        self._timestamp_list.insert(pos, time)
                        self._log_list.insert(pos, (eb, line, text_line))
                        if pos > top_insert_pos:
                            top_insert_pos = pos

                        # check if timestamp has wrapped
                        if log_entry[0] < eb.last_timestamp:
                            print(eb.name_color + eb.name + eb.default_color + " " + str(datetime.now()) + (" " * eb.indent) + " TRB timestamp wrap")
                            self._logfile.write(eb.name + " " + str(datetime.now()) + (" " * eb.indent) + " TRB timestamp wrap" + "\n")
                        eb.last_timestamp = log_entry[0]

                    eb.trb_log.clear()
                else:
                    # No log entries, enable logging just incase a reset has turned it off
                    self._enable_trb(eb)
                    eb.base_timestamp = eb.trb_log.stream.read_dongle_register(0, 0x1204) * (2 ** 32)

            except (TrbErrorDriverIOFailed, TrbErrorBridgeLinkIsDown, ReadFailureDUTInaccessible, ReadFailureLinkInvalid, ReadFailureSubsystemInaccessible, ReadFailure) as e:
                if eb.log_started:
                    print(colorama.Style.RESET_ALL + self._get_colour_attr('brightyellow') + eb.name + " " + str(datetime.now()) + (" " * eb.indent) + " TRB link is down")
                    self._logfile.write(eb.name + " " + str(datetime.now()) + (" " * eb.indent) + " TRB link is down" + "\n")
                    eb.log_started = False

        if top_insert_pos < 0:
            top_insert_pos = len(self._log_list)

        for _ in range(top_insert_pos):
            eb,log_entry,clean_log = self._log_list.pop(0)
            time = self._timestamp_list.pop(0)
            dt = eb.datetime + timedelta(microseconds = time / 10)
            #print(eb.name_color + eb.name +  eb.default_color + " " + str(dt) + (" " * eb.indent) + " " + log_entry)
            self._logfile.write(eb.name + " " + str(dt) + (" " * eb.indent) + " " + clean_log + "\n")

# colorama.init(convert=True)

# handle_arguments()
#
# logger = EarbudsLogger(device_options, not args.nolog)
#logger.add_highlight("appConManager\w+", "yellow")
#logger.add_highlight("appAvrcp\w+", "green")
#logger.add_highlight("appAvAvrcp\w+", "green")
#logger.add_highlight("appAvHandleAvrcp\w+", "green")
#logger.add_highlight("appA2dp\w+", "cyan")
#logger.add_highlight("appHandsetSig\w+", "red")
#logger.add_highlight("appPeerSig\w+", "red")
#logger.add_highlight("appSm\w+", "blue")
#logger.add_highlight("appConnRules\w+", "blue")
#logger.add_highlight("rule\w+", "magenta")
#logger.add_highlight("appTest\w+", "yellow")
#logger.add_highlight("appLinkPolicy\w+", "red")
#logger.add_highlight("hdma\w+", "red")
#logger.add_highlight("twsTopology\w+", "red")
#logger.add_highlight("appSm\w+", "green")
#logger.add_highlight("mirrorProfile\w+", "red")
#logger.add_highlight("MirrorProfile\w+", "red")
#logger.add_highlight("UpgradePeerSetIgnorePeer", "red")




logging_restarts = 0
last_restart = time.time()

# while True:
#     try:
#         logger.log()
#     # We get UnboundLocalError from a KeyboardInterrupt (within pydbg)
#     except UnboundLocalError as ule:
#         if "local variable '_wrapped'" in str(ule):
#             logger.log_message("Clean test exit (Keyboard)")
#             sys.exit(0)
#         raise
#     except (KeyboardInterrupt, SystemExit):
#         logger.log_message("Clean test exit")
#         sys.exit(0)
#     # Separate the exceptions. Developers may wish to change the raise to a pass
#     except Exception as e:
#         logger.log_message("Pydbg problem. "+str(type(e)))
#         raise
#     except:
#         logger.log_message("Dirty exit. Not an Exception ?")
#         raise

