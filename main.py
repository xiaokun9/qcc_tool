import os
import sys
import ctypes
from TestEngineAPI import *
from qcc_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from UI_data import ChildUiClass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #_DIRNAME = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
    #exe_path = os.path.join(_DIRNAME, "x86", "TestEngine.dll")
    #_dll = ctypes.windll.LoadLibrary(exe_path)
    #mydll = TestEngine(exe_path)
    # mydll = TestEngine(os.getcwd())
    #retval, versionStr = mydll.teGetVersion()
    app = QtWidgets.QApplication(sys.argv) #app

    child_dlg = ChildUiClass()
    child_dlg.show()
    #MainWindow = QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    #MainWindow.show()
    sys.exit(app.exec_())

