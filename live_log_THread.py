import os
import signal
import sys

import colorama
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal

from log1 import handle_arguments, device_options, EarbudsLogger

colorama.init(convert=True)

class live_log_Thread(QThread):
    is_init = False
    def __int__(self):
        super().__int__()

    def set_logger_init(self,port:str,elf:str):
        if self.is_init == False:
            self.is_init = True
            device_options[0]['device_url']='trb:usb2trb:'+port
            device_options[0]['firmware_builds'] = 'apps1:'+elf
            self.logger = EarbudsLogger(device_options, True)
    def set_runing_flag(self,flag:int):
        self.runing = flag

    # def live_log_init(self):
    #     colorama.init(convert=True)
    #     self.logger = EarbudsLogger(device_options, True)
    def kill_thread(self):
        #os.kill(signal.CTRL_C_EVENT, 0)
        self.logger.stop_log()
    def run(self) -> None:
        #handle_arguments()
        while True:
            try:
                self.logger.log()
            # We get UnboundLocalError from a KeyboardInterrupt (within pydbg)
            except UnboundLocalError as ule:
                if "local variable '_wrapped'" in str(ule):
                    self.logger.log_message("Clean test exit (Keyboard)")
                    sys.exit(0)
                raise
            except (KeyboardInterrupt, SystemExit):
                self.logger.log_message("Clean test exit")
                sys.exit(0)
            # Separate the exceptions. Developers may wish to change the raise to a pass
            except Exception as e:
                self.logger.log_message("Pydbg problem. " + str(type(e)))
                raise
            except:
                self.logger.log_message("Dirty exit. Not an Exception ?")
                raise
            # if self.runing == False:
            #
            #     break