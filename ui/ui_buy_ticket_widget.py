# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_buy_ticket_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BuyTicketWidget(object):
    def setupUi(self, BuyTicketWidget):
        BuyTicketWidget.setObjectName("BuyTicketWidget")
        BuyTicketWidget.resize(740, 436)
        self.verticalLayout = QtWidgets.QVBoxLayout(BuyTicketWidget)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_5 = QtWidgets.QGroupBox(BuyTicketWidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.groupBox_5)
        self.calendarWidget.setObjectName("calendarWidget")
        self.horizontalLayout_7.addWidget(self.calendarWidget)
        self.listWidget_4 = QtWidgets.QListWidget(self.groupBox_5)
        self.listWidget_4.setObjectName("listWidget_4")
        self.horizontalLayout_7.addWidget(self.listWidget_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_6.addWidget(self.checkBox)
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_6.addWidget(self.lineEdit_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addWidget(self.groupBox_5)

        self.retranslateUi(BuyTicketWidget)
        QtCore.QMetaObject.connectSlotsByName(BuyTicketWidget)

    def retranslateUi(self, BuyTicketWidget):
        _translate = QtCore.QCoreApplication.translate
        BuyTicketWidget.setWindowTitle(_translate("BuyTicketWidget", "Form"))
        self.groupBox_5.setTitle(_translate("BuyTicketWidget", "购票"))
        self.pushButton.setText(_translate("BuyTicketWidget", "购票"))
        self.checkBox.setText(_translate("BuyTicketWidget", "自动刷票"))
        self.label_3.setText(_translate("BuyTicketWidget", "间隔(s):"))

