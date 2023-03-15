import os
import sys
import ctypes
#from TestEngineAPI import TestEngine
from TestEngineAPI import TestEngine
from PyQt5 import QtWidgets
import re
KEY_BD_ADDRESS = "bt2:BD_ADDRESS"
KEY_DEVICE_NAME = "app5:DeviceName"
TTT = "audio:0x205C80"

if __name__ == '__main__':
    _DIRNAME = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
    exe_path = os.path.join(_DIRNAME, "x86", "TestEngine.dll")
    #_dll = ctypes.windll.LoadLibrary(exe_path)
    myDll = TestEngine(exe_path)
    handle = myDll.openTestEngine(myDll.USBDBG, '104', 0, 5000, 1000)
    """
    15 00 FF FF 49 E3 DF 10 66 54 06 F8 74 79 4B 3C C5 9C 7A 21 B8 E1 0F 21 DA 63 4D 76 34 1E C9 0E B7 C5 1B 37 00 00 00 00 01 00 46 1D B1 B8 EE 19 F4 58 4E 06 28 D6 D2 F7 DA 9D 00 00
    """
    # res =[
    #     21, 65535, 58185, 4319, 21606, 63494, 31092, 15435, 40133, 8570, 57784, 8463, 25562, 30285, 7732, 3785, 50615, 14107, 0, 0, 1, 7494, 47281, 6638, 22772, 1614, 54824, 63442, 40410, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # len =30
    str = "15 00 FF FF 49 E3 DF 10 66 54 06 F8 74 79 4B 3C C5 9C 7A 21 B8 E1 0F 21 DA 63 4D 76 34 1E C9 0E B7 C5 1B 37 00 00 00 00 01 00 46 1D B1 B8 EE 19 F4 58 4E 06 28 D6 D2 F7 DA 9D 00 00"

    show_value=""
    for index in range(0,len(show_value),2):
        print(index)
    print(int(len(show_value)/2))
    # for index in range(len):
    #     str_index = "".join(f"{res[index]:04x}")
    #     print(str_index)
    #     num1 = str_index[:2]
    #     num2 = str_index[2:]
    #     show_value+=str_index[2:]+" "+str_index[:2]+" "
    # print(show_value.upper().rstrip())
    # retval, lap, uap, nap = myDll.psReadBdAddr(handle)
    # print(retval, lap, uap, nap)
    # resetSearch = 1
    # while True:
    #     retval, keyId, endOfStore = myDll.tePsGetNextKeyId(handle, 0, resetSearch)
    #     print(retval, keyId, endOfStore)
    #     if retval == 1 and endOfStore == 0:
    #         resetSearch = 0
    #     else:
    #         break
    # print("------------------------------")
    # resetSearch = 1
    # while True:
    #     retval, keyId, endOfStore = myDll.tePsGetNextKeyId(handle, 1, resetSearch)
    #     print(retval, keyId, endOfStore)
    #     if retval == 1 and endOfStore == 0:
    #         resetSearch = 0
    #     else:
    #         break
    # retval, value, readLen = myDll.tePsRead(handle, 1024, 64, value=None)#16bit,分层ps 不能用此api 读取，用cacae config
    # print(retval, value, readLen)
    # print(handle)
    # print(os.getcwd()+'\config\hydracore_config.sdb:QCC517X_CONFIG')
    # retval = myDll.teConfigCacheInit(handle, configDb='config\hydracore_config.sdb:QCC517X_CONFIG')
    # print("teConfigCacheInit:" + str(retval))
    # retval = myDll.teConfigCacheRead(handle,None,0)
    # print("teConfigCacheRead:" + str(retval))
    # #retval, value, maxLen = myDll.teConfigCacheReadItem(handle, TTT, maxLen=100)
    # #print("teConfigCacheReadItem" + str(value))
    # retval = myDll.teConfigCacheMerge(handle,"aec_reference_config.htf")
    # print(retval)
    # str1 = "kun1"
    # str2 = '"{str1}"'.format(str1=str1)
    # retval = myDll.teConfigCacheWriteItem(handle, KEY_DEVICE_NAME, str2)
    # print("teConfigCacheWriteItem:" + str(retval))
    # retval = myDll.teConfigCacheWrite(handle, None,reserved=0)  # reserved:Currently unused, should be set to 0.
    # print("teConfigCacheWrite:" + str(retval))
    # retval, value, maxLen = myDll.teConfigCacheReadItem(handle, KEY_DEVICE_NAME,maxLen=100)
    # print(retval, value, maxLen)



