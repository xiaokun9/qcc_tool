import time

from PyQt5.QtCore import QThread, pyqtSignal


class opera_flash_Thread(QThread):

    opera_erase_flsh = 1
    opera_burn_flsh = 2
    opera_verify_flsh = 3

    signal_erase_process = pyqtSignal(int)
    signal_erase_finished = pyqtSignal(bool)
    signal_burn_process = pyqtSignal(int)
    signal_burn_finished = pyqtSignal(bool)
    def __int__(self):
        super.__init__()

    def Erase_flash_set_info(self,flashDll,port:int,transport:int,op:int):
        self.flashDll = flashDll
        self.port = port
        self.transport = transport
        self.op = op
    def Erase_flash(self):
        retval = self.flashDll.flOpen(port=self.port, xtal=26, delays=0, transport=self.transport)
        if retval != self.flashDll.TFL_OK:
            self.signal_erase_finished.emit(False)
            return
        retval = self.flashDll.flSetFlashType(type=self.flashDll.TFL_TYPE_SQIF)
        if retval != self.flashDll.TFL_OK:
            self.signal_erase_finished.emit(False)
            return
        retval = self.flashDll.flSetSubsysChipSel(subSys=4, chipSel=0)
        if retval != self.flashDll.TFL_OK:
            self.signal_erase_finished.emit(False)
            return
        retval = self.flashDll.flErase()
        if retval != self.flashDll.TFL_OK:
            self.signal_erase_finished.emit(False)
            return
        self.flashDll.flClose()
        self.signal_erase_finished.emit(True)
        """
        #下面的方法同时擦除多个设备的方法,
        port_info = self.tran_port[self.cur_port1]
        print(port_info)
        retval, transOut, device = self.FlashDll.flmConvertPort(transIn=port_info)
        if retval != self.FlashDll.TFL_OK:
            self.statusBar_label.setText('<font color="red">flmConvertPort fail</font>')
            return
        device_mask = int(port_info[-1:])
        retval = self.FlashDll.flmOpenTrans(deviceMask=device_mask, trans=transOut, xtal=26)#26M
        if retval != self.FlashDll.TFL_OK:
            self.statusBar_label.setText('<font color="red">flmOpenTrans fail</font>')
            return
        retval = self.FlashDll.flmSetFlashType(deviceMask=device_mask, type=self.FlashDll.TFL_TYPE_SQIF)
        if retval != self.FlashDll.TFL_OK:
            self.statusBar_label.setText('<font color="red">flmSetFlashType fail</font>')
            return
        retval = self.FlashDll.flmSetSubsysChipSel(deviceMask=device_mask, subSys=4, chipSel=0)#4 = Application
        if retval != self.FlashDll.TFL_OK:
            self.statusBar_label.setText('<font color="red">flmSetSubsysChipSel fail</font>')
            return
        retval = self.FlashDll.flmEraseSpawn(deviceMask=device_mask)
        if retval != self.FlashDll.TFL_OK:
            self.statusBar_label.setText('<font color="red">flmSetSubsysChipSel fail</font>')
            return
        while True:
            retval = self.FlashDll.flmGetDeviceProgress(device=0)
            if retval == 100:
                self.statusBar_label.setText('<font color="blue">flmGetDeviceProgress succeed</font>')
                break
            else:
                self.statusBar_label.setText('<font color="red">flmGetDeviceProgress fail</font>')
            time.sleep(1)
        retval = self.FlashDll.flmGetLastError()
        if retval == self.FlashDll.TFL_OK:
            self.statusBar_label.setText('<font color="blue">擦除成功！！！ </font>')
        else:
            self.statusBar_label.setText('<font color="blue">擦除失败，请重试，错误码：{nu}</font>'.format(nu=retval))
        # flmGetLastError/flmGetBitErrorField/flmClose
        self.FlashDll.flmClose(device_mask)
        """
    def Burn_flash_set_info(self,flashDll,port:int,transport:int,op:int,fileName:str):
        self.flashDll = flashDll
        self.port = port
        self.transport = transport
        self.op = op
        self.burn_fileName = fileName
    def Burn_flash(self):
        retval = self.flashDll.flOpen(port=self.port, xtal=26, delays=0, transport=self.transport)
        if retval != self.flashDll.TFL_OK:
            self.signal_burn_finished.emit(False)
            return
        retval = self.flashDll.flReadProgramFiles(fileName=self.burn_fileName)
        if retval != self.flashDll.TFL_OK:
            self.signal_burn_finished.emit(False)
            return
        retval = self.flashDll.flSetFlashType(type=self.flashDll.TFL_TYPE_SQIF)
        if retval != self.flashDll.TFL_OK:
            self.signal_burn_finished.emit(False)
            return
        retval = self.flashDll.flSetSubsysChipSel(subSys=4, chipSel=0)
        if retval != self.flashDll.TFL_OK:
            self.signal_burn_finished.emit(False)
            return
        retval = self.flashDll.flProgramSpawn()
        if retval != self.flashDll.TFL_OK:
            self.signal_burn_finished.emit(False)
            return
        while True:
            time.sleep(1)
            retval = self.flashDll.flGetProgress()
            self.signal_burn_process.emit(retval)
            #print(retval)
            if retval >= 100:
                break
        #flGetLastError
        self.flashDll.flClose()
        #retval = self.flashDll.flResetAndStart()
        #print(retval)
        self.signal_burn_finished.emit(True)
    def run(self):
        if self.op == self.opera_erase_flsh:
            self.Erase_flash()
        elif self.op == self.opera_burn_flsh:
            self.Burn_flash()
    """
    myDll = TestFlash(exe_path)
    retval = myDll.flOpen(port=104, xtal=26, delays=0, transport=4)
    print(retval)
    #myDll.flSetFlashType(type=2)
    myDll.flSetSubsysChipSel(subSys=4, chipSel=0)
    retval, sectors, sizeMbits, manId, devId = myDll.flGetFlashInfoEx()
    print(retval, sectors, sizeMbits, manId, devId)
    retval = myDll.flGetChipId()
    """