import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from test import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog


class MenuController(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(self).int()
        self.setupUi(self)

    def pushButton_click(self):
        self.showText.setText()
        dir_path=QFileDialog.getExistingDirectory(self,)
        self.showText.setText(dir_path)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())
