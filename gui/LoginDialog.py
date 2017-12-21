#!/usr/bin/python3
# -*- coding: utf-8 -*-

from ui.ui_login_dialog import Ui_LoginDialog
from PyQt5.QtWidgets import QDialog, QMessageBox
from eBus import  request

class LoginDialog(QDialog):

    def __init__(self):
        super(LoginDialog, self).__init__()
        self.loginName = ""
        self.initUI()
        self.keyCode = ''
        self.customerId = ''


    def initUI(self):
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)


    def getLoginInfo(self):
        return self.ui.textPhoneNum.text(), self.customerId, self.keyCode

    def accept(self):
        phoneNum = self.ui.textPhoneNum.text()
        pinCode = self.ui.textPhonePin.text()
        if phoneNum == "" or pinCode == "":
            QMessageBox.critical(self, "Error", "Input can't be empty")
            return
        customerId, keyCode = request.requireLogin(phoneNum, pinCode)
        if (keyCode == '' or customerId == ''):
            QMessageBox.critical(self, "Error", "Pin code isn't correct.")
            return
        self.keyCode = keyCode
        self.customerId = customerId
        super(LoginDialog, self).accept()

    def reject(self):
        super(LoginDialog, self).reject()

    def showEvent(self, QShowEvent):
        self.ui.textPhoneNum.setText(self.loginName)

    def onBtnSendPinClicked(self):
        phoneNum = self.ui.textPhoneNum.text()
        if len(phoneNum) != 11 :
            QMessageBox.critical(self, "Error", "Phone number must be 11 digit.")
            return
        if request.requestSendPinCode(phoneNum):
            QMessageBox.information(self, "Info", "Send phone pin successfully..")







