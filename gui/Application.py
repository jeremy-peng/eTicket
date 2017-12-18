import logging
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QSplashScreen
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
            userData.loginName,  userData.customerId, userData.keyCode = dialog.getLoginInfo()
            #re check login info
            if not request.validateUserData(userData.loginName, userData.customerId, userData.keyCode):
                logging.info("Login successful: %s,%s,%s" % (userData.loginName, userData.customerId, userData.keyCode))
                self.showLoginDialog()
                userData.sync()
            else:
                self.showMainWindow()
        else:
            sys.exit()

    def login(self):
        splash = QSplashScreen()
        splash.setPixmap(QPixmap(":/image/bus.png"))
        splash.showMessage("Login in...")
        splash.show()
        if request.validateUserData(userData.loginName, userData.customerId, userData.keyCode):
            logging.info("Login successful: %s,%s,%s" % (userData.loginName, userData.customerId, userData.keyCode))
            self.showMainWindow()
        else:
            self.showLoginDialog()