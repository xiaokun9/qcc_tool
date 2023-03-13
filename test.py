import os
import sys
import ctypes
#from TestEngineAPI import TestEngine
from TestEngineAPI import TestEngine

if __name__ == '__main__':
    _DIRNAME = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
    exe_path = os.path.join(_DIRNAME, "x86", "TestEngine.dll")
    _dll = ctypes.windll.LoadLibrary(exe_path)
    mydll = TestEngine(exe_path)

    retval, versionStr = mydll.teGetVersion()
    print(retval)
    print(versionStr)