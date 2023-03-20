from PyQt5.QtCore import QThread
from csr.dev.hw.port_connection import ReadFailureDUTInaccessible, ReadFailureLinkInvalid, \
    ReadFailureSubsystemInaccessible, ReadFailure
from csr.front_end.pydbg_front_end import PydbgFrontEndBase
from csr.transport.trbtrans import TrbErrorDriverIOFailed, TrbErrorBridgeLinkIsDown

from log1 import Earbud

evice_options = [
    {
        'name': "EB1",
        'name_color': "brightblue",
        'default_color': "brightgreen",
        'indent': 4,
        'log': {'apps1'},
        'device_url': 'trb:usb2trb:193663',
        'firmware_builds': r'apps1:C:\Users\cx\Desktop\qcc\earbud.elf',
        'target': None,
        'preload': True
    },

]

class py_dbg(QThread):

    def __init__(self):
        super().__init__()
        self.earbuds = None
        self.py_dbg_init_state = False

    def py_dbg_init(self):
        print('')
        if self.py_dbg_init_state == False:
            self.py_dbg_init_state = True
            self.earbuds = []
            for dev_opt in evice_options:
                device, trans = PydbgFrontEndBase.attach(dev_opt)
                eb = Earbud(device.chip)
                eb.apps1 = device.chip.apps_subsystem.p1
                eb.apps0 = device.chip.apps_subsystem.p0
                # eb.audio1 = device.chips[0].audio_subsystem.p1
                # eb.audio0 = device.chips[0].audio_subsystem.p0
                eb.curator = device.chip.curator_subsystem.core
                # eb.bt = device.chip.bt_subsystem.core
                self.earbuds.append(eb)
    def pydbg_open_case(self):
        for eb in self.earbuds:
            try:
                eb.apps1.fw.call.appTestCaseLidOpenEvent()#call func
            except (TrbErrorDriverIOFailed, TrbErrorBridgeLinkIsDown, ReadFailureDUTInaccessible, ReadFailureLinkInvalid) as e:
                return
    def pydbg_set_op_type(self,op:int):
        self.op = op
    def run(self) -> None:
        while True:
            if self.op == 1:
                self.pydbg_open_case()
            break