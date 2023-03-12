# 先导入生成的Ui界面模块
from PyQt5.QtWidgets import QMainWindow

from qcc_ui import Ui_MainWindow


# 继承
class ChildUiClass(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(ChildUiClass, self).__init__(parent=parent)
        self.setupUi(self)




# 在main函数中调用
if __name__ == '__main__':
    app = QApplication(sys.argv)
    child_dlg = ChildUiClass()
    # 例如下面这一行信号与槽的调用其他界面显示
    # About_dlg = ABout()
    # child_dlg .softversion.triggered.connect(About_dlg.show)
    child_dlg.show()
    sys.exit(app.exec_())