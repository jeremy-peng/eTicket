# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1043, 891)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.labelUserName = QtWidgets.QLabel(self.centralwidget)
        self.labelUserName.setObjectName("labelUserName")
        self.horizontalLayout_2.addWidget(self.labelUserName)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabTicket = QtWidgets.QWidget()
        self.tabTicket.setObjectName("tabTicket")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tabTicket)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchBusWidget = SearchBusWidget(self.tabTicket)
        self.searchBusWidget.setObjectName("searchBusWidget")
        self.horizontalLayout.addWidget(self.searchBusWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.remainTicketWidget = RemindTicketWidget(self.tabTicket)
        self.remainTicketWidget.setObjectName("remainTicketWidget")
        self.verticalLayout.addWidget(self.remainTicketWidget)
        self.buyTicketWidget = BuyTicketWidget(self.tabTicket)
        self.buyTicketWidget.setObjectName("buyTicketWidget")
        self.verticalLayout.addWidget(self.buyTicketWidget)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tabTicket, "")
        self.tabOrder = QtWidgets.QWidget()
        self.tabOrder.setObjectName("tabOrder")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabOrder)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btnRefreshOrders = QtWidgets.QPushButton(self.tabOrder)
        self.btnRefreshOrders.setObjectName("btnRefreshOrders")
        self.horizontalLayout_6.addWidget(self.btnRefreshOrders)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.groupBox = QtWidgets.QGroupBox(self.tabOrder)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.imcompleteOrderWidget = TicketOrderWidget(self.groupBox)
        self.imcompleteOrderWidget.setObjectName("imcompleteOrderWidget")
        self.horizontalLayout_4.addWidget(self.imcompleteOrderWidget)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tabOrder)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.completeOrderWidget = TicketOrderWidget(self.groupBox_2)
        self.completeOrderWidget.setObjectName("completeOrderWidget")
        self.horizontalLayout_5.addWidget(self.completeOrderWidget)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)
        self.tabWidget.addTab(self.tabOrder, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1043, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "你好:"))
        self.labelUserName.setText(_translate("MainWindow", "UserName"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTicket), _translate("MainWindow", "查询购票"))
        self.btnRefreshOrders.setText(_translate("MainWindow", "刷新"))
        self.groupBox.setTitle(_translate("MainWindow", "未完成订单"))
        self.groupBox_2.setTitle(_translate("MainWindow", "已完成订单"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabOrder), _translate("MainWindow", "订单"))

from gui.BuyTicketWidget import BuyTicketWidget
from gui.RemainTicketWidget import RemindTicketWidget
from gui.SearchBusWidget import SearchBusWidget
from gui.TicketOrderWidget import TicketOrderWidget
