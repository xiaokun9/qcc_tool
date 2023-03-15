# 先导入生成的Ui界面模块
from PyQt5.QtWidgets import QMainWindow, QAction,QLabel

from qcc_ui import Ui_MainWindow
from TestEngineAPI import TestEngine
import os,sys,re


# 继承
class ChildUiClass(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(ChildUiClass, self).__init__(parent=parent)
        self.setupUi(self)
        _DIRNAME = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
        exe_path = os.path.join(_DIRNAME, "x86", "TestEngine.dll")
        self.myDll = TestEngine(exe_path)
        retval, versionStr = self.myDll.teGetVersion()
        #self.statusBar.showMessage("DLL version:"+versionStr)

        #trans_list = trans.split(',')
        self.port_info = {}
        self.cur_port1 = None
        #self.cur_port2 = None
        self.handle1 = None
        #self.handle2 = None
        self.port_dataRate = 0 #Defines the baud rate to be used (for UART connections only).
        self.port_retryTimeOut =5000 #5000ms
        self.port_usbTimeout = 1000 #1000ms
        self.statusBar_label = QLabel()
        self.statusBar.addWidget(self.statusBar_label)
        #self.statusBar_label.setText("DLL version:"+versionStr)
        self.statusBar_label.setText('<font color="blue">DLL version:{st1}</font>'.format(st1=versionStr))

        self.statusBar_label_permanent  = QLabel()
        self.statusBar_label_permanent.setText("<a href=\"https://github.com/xiaokun9/qcc_tool/wiki\">github wiki</a>")
        self.statusBar_label_permanent.setOpenExternalLinks(True)
        self.statusBar.addPermanentWidget(self.statusBar_label_permanent)

        self.comboBox_1.activated.connect(self.port_status_change1)

        self.pushButton_1_read.clicked.connect(self.port_read_addr_name_1)
        self.pushButton_1_write.clicked.connect(self.port_write_addr_name_1)
        self.pushButton_app_psk_read.clicked.connect(self.app_psk_read_func)
        self.pushButton_app_psk_write.clicked.connect(self.app_psk_write_func)
        self.pushButton_audio_psk_read.clicked.connect(self.audio_psk_read_func)
        self.pushButton_aduio_psk_write.clicked.connect(self.audio_psk_write_func)
        #self.menu_2.triggered.connect(self.refresh_port)
        #self.menu_2.menuAction().triggered.connect(self.refresh_port)
        #add action
        self.refresh_port_action = QAction(self)
        self.refresh_port_action.setCheckable(False)
        self.refresh_port_action.setObjectName('refresh_port')
        self.refresh_port_action.triggered.connect(self.refresh_port)
        self.refresh_port_action.setText('刷新端口')
        self.menubar.addAction(self.refresh_port_action)
        self.refresh_port_action.setStatusTip('刷新端口')

        #Apps keys
        self.refresh_app_ps_action = QAction(self)
        self.refresh_app_ps_action.setCheckable(False)
        self.refresh_app_ps_action.setObjectName('refresh_app_ps_key')
        self.refresh_app_ps_action.triggered.connect(self.refresh_app_psk)
        self.refresh_app_ps_action.setText('读取app psk')
        self.menubar.addAction(self.refresh_app_ps_action)
        self.refresh_app_ps_action.setStatusTip('读取app psk')

        #Audio keys
        self.refresh_audio_psk_action = QAction(self)
        self.refresh_audio_psk_action.setCheckable(False)
        self.refresh_audio_psk_action.setObjectName('refresh_audio_ps_key')
        self.refresh_audio_psk_action.triggered.connect(self.refresh_audio_psk)
        self.refresh_audio_psk_action.setText('读取audio psk')
        self.menubar.addAction(self.refresh_audio_psk_action)
        self.refresh_audio_psk_action.setStatusTip('读取audio psk')

    def refresh_port(self,checked):
        #print(self.sender().text())
        #print(checked)
        self.comboBox_1.clear()
        #self.comboBox_2.clear()
        retval, maxLen, ports, trans, count = self.myDll.teGetAvailableDebugPorts(256)
        ports_list = ports.split(',')
        for index in range(count):
            self.port_info[ports_list[index]] = ports_list[index].replace(' ', '').replace('(', '').replace(')', '')
            self.comboBox_1.addItem(ports_list[index])
            #self.comboBox_2.addItem(ports_list[index])
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
                #self.cur_port2 = ports_list[index]
                pass
            #self.port_info[ports_list[index]] = trans_list[index]
            #print(ports_list[index].replace(' ','').replace('(','').replace(')',''))
        self.statusBar_label.setText('<font color="blue">端口刷新完成</font>')
    def refresh_app_psk(self, checked):
        #print("refresh_app_psk")
        self.app_psk_id.clear()
        resetSearch = 1
        while True:
            retval, keyId, endOfStore = self.myDll.tePsGetNextKeyId(self.handle1, 0, resetSearch)
            #print(retval, keyId, endOfStore)
            if retval == 1 and endOfStore == 0:
                resetSearch = 0
                self.app_psk_id.addItem(str(hex(keyId)))
            else:
                break

    def refresh_audio_psk(self, checked):
        #print("refresh_audio_psk")
        self.audio_psk_id.clear()
        resetSearch = 1
        while True:
            retval, keyId, endOfStore = self.myDll.tePsGetNextKeyId(self.handle1, 1, resetSearch)
            #print(retval, keyId, endOfStore)
            if retval == 1 and endOfStore == 0:
                resetSearch = 0
                self.audio_psk_id.addItem(str(hex(keyId)))
            else:
                break
    def port_status_change1(self):
        self.cur_port1 = self.comboBox_1.currentText()
        if self.handle1 != None:
            retval = self.myDll.closeTestEngine(self.handle1)#close handle
            #print("closeTestEngine:" + retval)
        self.handle1 = None
        self.port1_open()
        #print(self.cur_port1)
    def port_status_change2(self):
        #self.cur_port2 = self.comboBox_2.currentText()
        #print(self.cur_port2)
        pass
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
            #self.statusBar.showMessage(self.cur_port1 + " open fail,handle:" + str(self.handle1))
            self.statusBar_label.setText('<font color="red">{port}open fail,handle:{hand}</font>'.format(port=self.cur_port1,hand=self.handle1))
            #print(port_device + " open fail,handle:"+ self.handle1)
            #self.textBrowser.setText(port_device + " open fail,handle:" + str(self.handle1))
        else:
            #print("port1_open succeed")
            self.statusBar.showMessage(self.cur_port1 + " open succeed,handle:" + str(self.handle1))
            self.statusBar_label.setText('<font color="blue">{port}open succeed,handle:{hand}</font>'.format(port=self.cur_port1,hand=self.handle1))
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
            #self.statusBar.showMessage("ConfigCacheInit Succeed")
            self.statusBar_label.setText('<font color="blue">ConfigCacheInit Succeed</font>')
        else:
            #self.statusBar.showMessage("ConfigCacheInit Fail,please retry!!!")
            self.statusBar_label.setText('<font color="red">ConfigCacheInit Fail,please retry!!!</font>')
            return
        #print(retval)

        retval = self.myDll.teConfigCacheRead(self.handle1, None, 0) #None:read for device
        if retval == self.myDll.TE_OK:
            #self.statusBar.showMessage("ConfigCacheRead Succeed")
            self.statusBar_label.setText('<font color="blue">ConfigCacheRead Succeed</font>')
        else:
            #self.statusBar.showMessage("ConfigCacheRead Fail,please retry!!!")
            self.statusBar_label.setText('<font color="red">ConfigCacheRead Fail,please retry!!!</font>')
            return
        #print(retval)
        retval, value, maxLen = self.myDll.teConfigCacheReadItem(self.handle1, key='bt2:BD_ADDRESS', maxLen=100)
        self.addr1_arry = value.replace('[','').replace(']','').strip().split(' ')#array
        addr1_str = ''
        for index in range(6):
            temp = 5 - index
            addr1_str = addr1_str + self.addr1_arry[temp]
            if temp == 4:
                addr1_str += ':'
            elif temp == 3:
                addr1_str += ':'
            #print(addr1_str)
        self.lineEdit_1_BD_addr.setText(addr1_str)#bd addr
        #print(retval, value, maxLen)
        retval, value, maxLen = self.myDll.teConfigCacheReadItem(self.handle1, key='app5:DeviceName',maxLen=100)
        value = value.replace('"','')
        #print(retval, value, maxLen)
        self.lineEdit_1_name.setText(value)#bt name
        if retval != self.myDll.TE_OK:
            #self.statusBar.showMessage("Cache Read Fail,please retry!!!")
            self.statusBar_label.setText('<font color="red">Cache Read Fail,please retry!!!</font>')
        else:
            #self.statusBar.showMessage("Cache Read Succeed")
            self.statusBar_label.setText('<font color="blue">Cache Read Succeed</font>')
    def port_write_addr_name_1(self):
        #step 1 ->teConfigCacheInit
        if self.lineEdit_1_name.text() == '' or self.lineEdit_1_BD_addr.text() == '':
            return
        if self.handle1 == self.myDll.TE_INVALID_HANDLE_VALUE or self.handle1 == None:
            return
        retval = self.myDll.teConfigCacheInit(self.handle1, configDb='config\hydracore_config.sdb:QCC517X_CONFIG')
        if retval == self.myDll.TE_OK:
            #self.statusBar.showMessage("ConfigCacheInit Succeed")
            self.statusBar_label.setText('<font color="blue">ConfigCacheInit Succeed</font>')
        else:
            #self.statusBar.showMessage("ConfigCacheInit Fail,please retry!!!")
            self.statusBar_label.setText('<font color="red">ConfigCacheInit Fail,please retry!!!</font>')
            return
        #step 2 ->teConfigCacheRead
        retval = self.myDll.teConfigCacheRead(self.handle1, None, 0) #None:read for device
        if retval == self.myDll.TE_OK:
            #self.statusBar.showMessage("ConfigCacheRead Succeed")
            self.statusBar_label.setText('<font color="blue">ConfigCacheRead Succeed</font>')
        else:
            #self.statusBar.showMessage("ConfigCacheRead Fail,please retry!!!")
            self.statusBar_label.setText('<font color="red">ConfigCacheRead Fail,please retry!!!</font>')
            return
        #step 3 ->teConfigCacheWriteItem (addr)

        res = re.findall(r'.{2}', self.lineEdit_1_BD_addr.text().replace(':',''))
        str = ""
        for index in range(6):
            str += res[5 - index]
        str_w='[{str1}]'.format(str1=str)
        retval = self.myDll.teConfigCacheWriteItem(self.handle1, 'bt2:BD_ADDRESS', str_w)
        if retval != self.myDll.TE_OK:
            #self.statusBar.showMessage("BD Addr Write Cache Fail,please retry!!!")
            self.statusBar_label.setText('<font color="red">BD Addr Write Cache Fail,please retry!!!</font>')
        #step 4 ->teConfigCacheWriteItem (name)
        str_w='"{str1}"'.format(str1=self.lineEdit_1_name.text())
        retval = self.myDll.teConfigCacheWriteItem(self.handle1, 'app5:DeviceName', str_w)
        if retval != self.myDll.TE_OK:
            #self.statusBar.showMessage("BD Name Write Cache Fail,please retry!!!")
            self.statusBar_label.setText('<font color="red">BD Name Write Cache Fail,please retry!!!</font>')
        #step 5 ->teConfigCacheWrite
        retval = self.myDll.teConfigCacheWrite(self.handle1, None, reserved=0)# reserved:Currently unused, should be set to 0.
        if retval != self.myDll.TE_OK:
            #self.statusBar.showMessage("Cache Write Fail,please retry!!!")
            self.statusBar_label.setText('<font color="red">Cache Write Fail,please retry!!!</font>')
        else:
            #self.statusBar.showMessage("Cache Write Succeed")
            self.statusBar_label.setText('<font color="blue">Cache Write Succeed</font>')

    def app_psk_read_func(self):
        #print("app_psk_read_func")
        str_value = self.app_psk_id.currentText()
        if str_value == '':
            return
        psk_id = eval(str_value)
        retval, value, readLen = self.myDll.tePsRead(self.handle1, psk_id, 64, value=None)  # 16bit,分层ps 不能用此api 读取，用cacae config
        #print(retval, value, readLen)
        if retval != self.myDll.TE_OK:
            self.statusBar_label.setText('<font color="red">App psk id read Fail</font>')
            return
        show_value = ""
        for index in range(readLen):
            str_index = "".join(f"{value[index]:04x}")
            #print(str_index)
            show_value += str_index[2:] + " " + str_index[:2] + " "
        #print(show_value.upper().rstrip())
        self.lineEdit_app_psk_value.setText(show_value.upper().rstrip())
        self.statusBar_label.setText('<font color="blue">App psk id read succeed</font>')
    def app_psk_write_func(self):
        #print("app_psk_write_func")
        str_value = self.app_psk_id.currentText()
        if str_value == '':
            self.statusBar_label.setText('<font color="red">App psk id is NULL</font>')
            return
        psk_id = eval(str_value)
        value_list = self.lineEdit_app_psk_value.text().split(' ')
        data_len = len(value_list)
        value=[]
        for index in range(0, data_len, 2):
            #print(int(value_list[index], 16) + (int(value_list[index + 1], 16) << 8))
            value.append(int(value_list[index], 16) + (int(value_list[index + 1], 16) << 8))
        retval = self.myDll.tePsWrite(self.handle1, psk_id, int(data_len/2), value)
        if retval != self.myDll.TE_OK:
            self.statusBar_label.setText('<font color="red">App psk id write Fail</font>')
        else:
            self.statusBar_label.setText('<font color="blue">App psk id write Succeed</font>')
    def audio_psk_read_func(self):
        #print("audio_psk_read_func")
        str_value = self.audio_psk_id.currentText()
        if str_value == '':
            return
        psk_id = eval(str_value)
        retval, value, readLen = self.myDll.tePsAudioRead(self.handle1, psk_id, 64, value=None)  # 16bit,分层ps 不能用此api 读取，用cacae config
        #print(retval, value, readLen)
        if retval != self.myDll.TE_OK:
            self.statusBar_label.setText('<font color="red">Audio psk id read Fail</font>')
            return
        show_value = ""
        for index in range(readLen):
            str_index = "".join(f"{value[index]:04x}")
            #print(str_index)
            show_value += str_index[2:] + " " + str_index[:2] + " "
        #print(show_value.upper().rstrip())
        self.lineEdit_audio_psk_value.setText(show_value.upper().rstrip())
        self.statusBar_label.setText('<font color="blue">Audio psk id read succeed</font>')
    def audio_psk_write_func(self):
        #print("audio_psk_write_func")
        str_value = self.audio_psk_id.currentText()
        if str_value == '':
            self.statusBar_label.setText('<font color="red">Audio psk id is NULL</font>')
            return
        psk_id = eval(str_value)
        value_list = self.lineEdit_audio_psk_value.text().split(' ')
        data_len = len(value_list)
        value=[]
        for index in range(0, data_len, 2):
            #print(int(value_list[index], 16) + (int(value_list[index + 1], 16) << 8))
            value.append(int(value_list[index], 16) + (int(value_list[index + 1], 16) << 8))
        retval = self.myDll.tePsAudioWrite(self.handle1, psk_id, int(data_len/2), value)
        if retval != self.myDll.TE_OK:
            self.statusBar_label.setText('<font color="red">audio psk id write Fail</font>')
        else:
            self.statusBar_label.setText('<font color="blue">audio psk id write Succeed</font>')





# 在main函数中调用
if __name__ == '__main__':
    app = QApplication(sys.argv)
    child_dlg = ChildUiClass()
    # 例如下面这一行信号与槽的调用其他界面显示
    # About_dlg = ABout()
    # child_dlg .softversion.triggered.connect(About_dlg.show)
    child_dlg.show()
    sys.exit(app.exec_())