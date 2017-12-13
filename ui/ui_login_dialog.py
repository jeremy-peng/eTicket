# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_login_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(221, 128)
        self.verticalLayout = QtWidgets.QVBoxLayout(LoginDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(LoginDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.textPhoneNum = QtWidgets.QLineEdit(LoginDialog)
        self.textPhoneNum.setObjectName("textPhoneNum")
        self.horizontalLayout.addWidget(self.textPhoneNum)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(LoginDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.textPhonePin = QtWidgets.QLineEdit(LoginDialog)
        self.textPhonePin.setText("")
        self.textPhonePin.setObjectName("textPhonePin")
        self.horizontalLayout_2.addWidget(self.textPhonePin)
        self.btnSendPinCode = QtWidgets.QPushButton(LoginDialog)
        self.btnSendPinCode.setObjectName("btnSendPinCode")
        self.horizontalLayout_2.addWidget(self.btnSendPinCode)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(LoginDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(LoginDialog)
        self.buttonBox.accepted.connect(LoginDialog.accept)
        self.buttonBox.rejected.connect(LoginDialog.reject)
        self.btnSendPinCode.clicked.connect(LoginDialog.onBtnSendPinClicked)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Login"))
        self.label.setText(_translate("LoginDialog", "Phone:"))
        self.label_2.setText(_translate("LoginDialog", "Pin:"))
        self.btnSendPinCode.setText(_translate("LoginDialog", "Send Pin"))

