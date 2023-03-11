import os
import sys
import ctypes
from TestEngineAPI import *
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    _DIRNAME = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
    exe_path = os.path.join(_DIRNAME, "x86", "TestEngine.dll")
    #_dll = ctypes.windll.LoadLibrary(exe_path)
    mydll = TestEngine(exe_path)
    retval, versionStr = mydll.teGetVersion()
    print(11)
   # mydll = TestEngine(os.getcwd())
