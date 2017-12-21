#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from ui.ui_mainwindow import Ui_MainWindow
import  logging
import ui.eTicket


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
        self.ui.buyTicketWidget.requireBusInfo.connect(self.ui.searchBusWidget.onRequireBusInfo)

    def initUI(self):
        self.setWindowIcon(QIcon(":/image/bus.jpg"))



