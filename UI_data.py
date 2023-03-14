# 先导入生成的Ui界面模块
from PyQt5.QtWidgets import QMainWindow

from qcc_ui import Ui_MainWindow
from TestEngineAPI import TestEngine
import os,sys


# 继承
class ChildUiClass(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(ChildUiClass, self).__init__(parent=parent)
        self.setupUi(self)
        _DIRNAME = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
        exe_path = os.path.join(_DIRNAME, "x86", "TestEngine.dll")
        self.myDll = TestEngine(exe_path)
        retval, versionStr = self.myDll.teGetVersion()
        self.statusBar.showMessage("DLL version:"+versionStr)

        retval, maxLen, ports, trans, count = self.myDll.teGetAvailableDebugPorts(256)
        ports_list = ports.split(',')
        #trans_list = trans.split(',')
        self.port_info = {}
        self.cur_port1 = None
        self.cur_port2 = None
        self.handle1 = None
        self.handle2 = None
        self.port_dataRate = 0 #Defines the baud rate to be used (for UART connections only).
        self.port_retryTimeOut =5000 #5000ms
        self.port_usbTimeout = 1000 #1000ms
        for index in range(count):
            self.port_info[ports_list[index]] = ports_list[index].replace(' ', '').replace('(', '').replace(')', '')
            if index == 0:
                self.cur_port1 = ports_list[index]
                port_device = self.port_info[self.cur_port1]
                parm1 = None
                if port_device[:6] == 'USBDBG':
                    parm1 = self.myDll.USBDBG
                elif port_device[:6] == 'USBTRB':
                    parm1 = self.myDll.TRB
                # parm 2
                parm2 = port_device[6:]
                self.handle1 = self.myDll.openTestEngine(parm1, parm2, self.port_dataRate, self.port_retryTimeOut,
                                                         self.port_usbTimeout)
            elif index == 1:
                self.cur_port2 = ports_list[index]
            #self.port_info[ports_list[index]] = trans_list[index]
            #print(ports_list[index].replace(' ','').replace('(','').replace(')',''))
            self.comboBox_1.addItem(ports_list[index])
            self.comboBox_2.addItem(ports_list[index])
        self.comboBox_1.activated.connect(self.port_status_change1)
        self.comboBox_2.activated.connect(self.port_status_change2)
        self.pushButton_1_read.clicked.connect(self.port_read_addr_name_1)

    def port_status_change1(self):
        self.cur_port1 = self.comboBox_1.currentText()
        if self.handle1 != None:
            retval = self.myDll.closeTestEngine(self.handle1)#close handle
            #print("closeTestEngine:" + retval)
        self.handle1 = None
        self.port1_open()
        #print(self.cur_port1)
    def port_status_change2(self):
        self.cur_port2 = self.comboBox_2.currentText()
        #print(self.cur_port2)
    def port1_open(self):
        port_device=self.port_info[self.cur_port1]
        #parm 1
        parm1 = None
        if port_device[:6] == 'USBDBG':
            parm1 = self.myDll.USBDBG
        elif port_device[:6] == 'USBTRB':
            parm1 = self.myDll.TRB
        #parm 2
        parm2 = port_device[6:]
        self.handle1 = self.myDll.openTestEngine(parm1,parm2,self.port_dataRate,self.port_retryTimeOut,self.port_usbTimeout)
        #print(self.handle1)
        if self.handle1 == self.myDll.TE_INVALID_HANDLE_VALUE:
            #print("port1_open fail ")
            self.statusBar.showMessage(self.cur_port1 + " open fail,handle:" + str(self.handle1))
            #print(port_device + " open fail,handle:"+ self.handle1)
            #self.textBrowser.setText(port_device + " open fail,handle:" + str(self.handle1))
        else:
            #print("port1_open succeed")
            self.statusBar.showMessage(self.cur_port1 + " open succeed,handle:" + str(self.handle1))
            #print(port_device + " open succeed,handle:"+ self.handle1)
            #self.textBrowser.setText(port_device + " open succeed,handle:" + str(self.handle1))

    def port_read_addr_name_1(self):
        if self.handle1 == self.myDll.TE_INVALID_HANDLE_VALUE or self.handle1 == None:
            return
        #retval, bdAddr = self.myDll.hciReadBdAddr(self.handle1)
        #if retval != self.myDll.TE_OK:
            #self.statusBar.showMessage("device 1 read BDaddr fail")
            #return
        retval = self.myDll.teConfigCacheInit(self.handle1, configDb='config\hydracore_config.sdb:QCC517X_CONFIG')
        if retval == self.myDll.TE_OK:
            self.statusBar.showMessage("ConfigCacheInit Succeed")
        else:
            self.statusBar.showMessage("ConfigCacheInit Fail,please retry!!!")
            return
        print(retval)

        retval = self.myDll.teConfigCacheRead(self.handle1, None, 0) #None:read for device
        if retval == self.myDll.TE_OK:
            self.statusBar.showMessage("ConfigCacheRead Succeed")
        else:
            self.statusBar.showMessage("ConfigCacheRead Fail,please retry!!!")
            return
        print(retval)
        retval, value, maxLen = self.myDll.teConfigCacheReadItem(self.handle1, key='bt2:BD_ADDRESS', maxLen=100)
        value = value.replace('[','').replace(']','').strip().replace(' ',':')#反转？
        self.lineEdit_1_BD_addr.setText(value)#bd addr
        print(retval, value, maxLen)
        retval, value, maxLen = self.myDll.teConfigCacheReadItem(self.handle1, key='app5:DeviceName',maxLen=100)
        value = value.replace('"','')
        print(retval, value, maxLen)
        self.lineEdit_1_name.setText(value)#bt name
        #self.myDll.teConfigCacheWrite()
        print("button")




# 在main函数中调用
if __name__ == '__main__':
    app = QApplication(sys.argv)
    child_dlg = ChildUiClass()
    # 例如下面这一行信号与槽的调用其他界面显示
    # About_dlg = ABout()
    # child_dlg .softversion.triggered.connect(About_dlg.show)
    child_dlg.show()
    sys.exit(app.exec_())