from PyQt5.QtWidgets import QApplication, QDialog
import sys

from gui.LoginDialog import LoginDialog
from gui.MainWindow import MainWindow
from config import  userData
from eBus import  request



class App(QApplication):
    def __init__(self, args):
        super(App, self).__init__(args)
        self.mainwindow = MainWindow()

    def showMainWindow(self):
        self.mainwindow.setUserName(userData.loginName)
        self.mainwindow.show()


    def showLoginDialog(self):
        dialog = LoginDialog()
        dialog.loginName = userData.loginName
        if (dialog.exec_() == QDialog.Accepted):
            loginName, pin = dialog.getInput()
            userData.loginName = loginName
            userData.sync()
            self.showMainWindow()
        else:
            sys.exit()