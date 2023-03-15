import os
import sys
import ctypes
#from TestEngineAPI import TestEngine
from TestEngineAPI import TestEngine
from PyQt5 import QtWidgets
from TestFlashAPI import TestFlash

import time
import re
KEY_BD_ADDRESS = "bt2:BD_ADDRESS"
KEY_DEVICE_NAME = "app5:DeviceName"
TTT = "audio:0x205C80"

if __name__ == '__main__':
    # _DIRNAME = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
    # exe_path = os.path.join(_DIRNAME, "x86", "TestEngine.dll")
    # #_dll = ctypes.windll.LoadLibrary(exe_path)
    # myDll = TestEngine(exe_path)
    # handle = myDll.openTestEngine(myDll.USBDBG, '104', 0, 5000, 1000)
    # ports = 'USB TRB(193555), USB TRB(193663), USBDBG(104), USBDBG(105)'
    # trans = 'SPITRANS=TRB SPIPORT=1,SPITRANS=TRB SPIPORT=2,SPITRANS=USBDBG SPIPORT=1,SPITRANS=USBDBG SPIPORT=2'
    # count = 4
    # ss = trans.split(',')
    # tran_port = []
    # print(ss)
    # for index in range(count):
    #     tran_port.append(int(ss[index][-1:]))
    # print(tran_port)

    _DIRNAME = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
    exe_path = os.path.join(_DIRNAME, "x86", "TestFlash.dll")
    #_dll = ctypes.windll.LoadLibrary(exe_path)
    myDll = TestFlash(exe_path)
    #retval, transOut, device = myDll.flmConvertPort(transIn='SPITRANS=USBDBG SPIPORT=1')
    #print(retval, transOut, device)
    retval = myDll.flmOpenTrans(deviceMask=1, trans='SPITRANS=USBDBG', xtal=26)
    print(retval)
    retval = myDll.flmSetFlashType(deviceMask=1, type=2)
    print("flmSetFlashType"+str(retval))
    retval = myDll.flmSetSubsysChipSel(deviceMask=1, subSys=4, chipSel=0)
    print("flmSetSubsysChipSel:"+str(retval))
    retval = myDll.flmEraseSpawn(deviceMask=1)
    print("flmEraseSpawn"+str(retval))
    while True:
        retval = myDll.flmGetDeviceProgress(device=1)
        if retval == 100:
            break
        time.sleep(1)
    retval = myDll.flmGetLastError()
    print(retval)
    #flmGetLastError/flmGetBitErrorField/flmClose
    """
    retval = myDll.flOpen(port=104, xtal=26, delays=0, transport=4)
    if retval != myDll.TFL_OK:
        print("flOpen fail")
    retval = myDll.flSetFlashType(type=2)
    print(retval)
    retval = myDll.flSetSubsysChipSel(subSys=4, chipSel=0)
    print(retval)
    retval = myDll.flErase()
    print(retval)
    """
    # retval = myFlashDll.flmOpen(1, 0x1a, myFlashDll.TFL_USBDBG)
    # print(retval)
    # retval = myFlashDll.flmEraseSpawn(1)
    # print(retval)
    # if retval == 0:#擦除线程启动成功
    #     retval = myFlashDll.flmGetDeviceError(1)
    #     print(retval)
    #     print("123")
    #     while True:
    #         retval = myFlashDll.flmGetDeviceProgress(1)
    #         print(retval)
    #         if retval <= 0 or retval == 100:
    #             retval = myFlashDll.flmGetDeviceError(1)
    #             print(retval)
    #             print("3333")
    #             break
    #         print("222")
    #         time.sleep(1)
    # print("444")
    # retval = myFlashDll.flmClose(1)
    # print("111")
    # print(retval)






