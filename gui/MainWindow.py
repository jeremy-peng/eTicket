from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import QMainWindow
from ui.ui_mainwindow import Ui_MainWindow
from PyQt5.QtGui import QTextCharFormat, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



    def setUserName(self, name):
        self.ui.labelUserName.setText(name)