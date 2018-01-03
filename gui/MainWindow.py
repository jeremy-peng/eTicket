#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from ui.ui_mainwindow import Ui_MainWindow
import  logging
import ui.eTicket
from eBus import request
from config import userData


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initSignals()
        self.initUI()


    def setUserName(self, name):
        self.ui.labelUserName.setText(name)


    def initSignals(self):
        self.ui.searchBusWidget.selectedBus.connect(self.ui.remainTicketWidget.onSelectedBus)
        self.ui.searchBusWidget.selectedBus.connect(self.ui.buyTicketWidget.onSelctedBusLineChanged)
        self.ui.buyTicketWidget.requireBusInfo.connect(self.ui.searchBusWidget.onRequireBusInfo)
        self.ui.remainTicketWidget.calendarPageChanged.connect(self.ui.buyTicketWidget.setCurrentPage)
        self.ui.remainTicketWidget.calendarClicked.connect(self.ui.buyTicketWidget.onClickCalendar)
        self.ui.buyTicketWidget.calendarPageChanged.connect(self.ui.remainTicketWidget.setCurrentPage)
        self.ui.buyTicketWidget.ticketBooked.connect(self.ui.remainTicketWidget.checkRemindTicket)
        self.ui.btnRefreshOrders.clicked.connect(self.onRefreshOrder)

    def initUI(self):
        self.setWindowIcon(QIcon(":/image/bus.jpg"))
        self.ui.completeOrderWidget.setOperationWidgetsShown(False)

    def onRefreshOrder(self):
        # check imcomplete order
        imcompleteOrderReturnObj = request.requireCheckAllOrder(userData.loginName, userData.customerId, userData.keyCode, 1)
        if imcompleteOrderReturnObj is None:
            return
        self.ui.imcompleteOrderWidget.setOrderList(imcompleteOrderReturnObj.returnData)
        self.ui.imcompleteOrderWidget.resizeColumnsToContents()

        completeRrderReturnObj = request.requireCheckAllOrder(userData.loginName, userData.customerId, userData.keyCode, 2)
        if completeRrderReturnObj is None:
            return
        self.ui.completeOrderWidget.setOrderList(completeRrderReturnObj.returnData)
        self.ui.completeOrderWidget.resizeColumnsToContents()


