import os
import sys
import ctypes
#from TestEngineAPI import TestEngine
from TestEngineAPI import TestEngine
from PyQt5 import QtWidgets

if __name__ == '__main__':
    _DIRNAME = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
    exe_path = os.path.join(_DIRNAME, "x86", "TestEngine.dll")
    #_dll = ctypes.windll.LoadLibrary(exe_path)
    #myDll = TestEngine(exe_path)
    #handle = myDll.openTestEngine(myDll.USBDBG, '104', 0, 5000, 1000)
    #retval, lap, uap, nap = myDll.psReadBdAddr(handle)
    #print(retval, lap, uap, nap)
    a = '77 66 55 44 33 22'.split(' ')
    print(a[0])
    print(a[1])
    str = ''
    for index in range(6):
        temp = 5-index
        str = str+a[temp]
        if temp == 4:
            str+=':'
        elif temp == 3:
            str+=':'
        print(str)


    #print(handle)
    #print(os.getcwd()+'\config\hydracore_config.sdb:QCC517X_CONFIG')
    #retval = myDll.teConfigCacheInit(handle, configDb='config\hydracore_config.sdb:QCC517X_CONFIG')
    #print(retval)
    #retval = myDll.teConfigCacheRead(handle,None,0)
    #print(retval)
    #retval, value, maxLen = myDll.teConfigCacheReadItem(handle, key='bt2:BD_ADDRESS',maxLen=100)
    #print(retval, value, maxLen)



