#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import QTextCharFormat
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QDate, Qt, pyqtSignal

from ui.ui_buy_ticket_widget import Ui_BuyTicketWidget
from gui.BuyTicketDateModel import BuyTicketDateModel
import logging
from gui.BusInfo import BusInfo

class BuyTicketWidget(QWidget):
    BuyTicketText = QTextCharFormat()
    BuyTicketText.setForeground(Qt.black)
    BuyTicketText.setBackground(Qt.green)
    requireBusInfo = pyqtSignal(BusInfo)


    def __init__(self, parent = None):
        super(BuyTicketWidget, self).__init__(parent)
        self.ui = Ui_BuyTicketWidget()
        self.ui.setupUi(self)
        self.ticketDayModel = BuyTicketDateModel()
        self.initUI()
        self.initSignals()


    def initSignals(self):
        self.ui.btnSelectAllDays.clicked.connect(self.onSelectedAllDays)
        self.ui.btnInvertSelectedDays.clicked.connect(self.onInvertSelectedDays)
        self.ui.btnSelectAllWeekDays.clicked.connect(self.onSelectedAllWeekDays)
        self.ui.btnSelectAllWorkDays.clicked.connect(self.onSelectedAllWorkDays)
        self.ui.btnClear.clicked.connect(self.onClearAllDays)
        self.ui.btnBuyTicket.clicked.connect(self.onBuyTicket)
        self.ui.calendarWidget.currentPageChanged.connect(self.onCurrentPageChanged)
        self.ui.calendarWidget.clicked.connect(self.onClickCalendar)

    def initUI(self):
        curDate = QDate.currentDate()
        self.ui.calendarWidget.setSelectedDate(curDate)
        self.ticketDayModel.setDate(curDate.year(), curDate.month())


    def onSelectedAllDays(self):
        logging.info("select all days")
        self.ticketDayModel.selectAllDays()
        self.updateBuyTicketDays(self.ticketDayModel.getSeletedDays())

    def onInvertSelectedDays(self):
        logging.info("invert all days")
        self.ticketDayModel.invertSelectDay()
        self.updateBuyTicketDays(self.ticketDayModel.getSeletedDays())

    def onSelectedAllWorkDays(self):
        logging.info("select all work days")
        self.ticketDayModel.selectAllWorkDays()
        self.updateBuyTicketDays(self.ticketDayModel.getSeletedDays())

    def onSelectedAllWeekDays(self):
        logging.info("invert all week days")
        self.ticketDayModel.selectAllWeekDays()
        self.updateBuyTicketDays(self.ticketDayModel.getSeletedDays())

    def onClearAllDays(self):
        logging.info("clear all selected")
        self.ticketDayModel.clearSelectedDays()
        self.updateBuyTicketDays(self.ticketDayModel.getSeletedDays())

    def onCurrentPageChanged(self, year, month):
        self.ticketDayModel.setDate(year, month)
        self.updateBuyTicketDays(self.ticketDayModel.getSeletedDays())


    def updateBuyTicketDays(self, buyDays : list):
        self.ui.calendarWidget.setDateTextFormat(QDate(), QTextCharFormat())
        self.ui.listSelectedDays.clear()
        selectedDayStrList = []
        for date in buyDays:
            self.ui.calendarWidget.setDateTextFormat(date, BuyTicketWidget.BuyTicketText)
            selectedDayStrList.append(date.toString("yyyyMMdd"))
        self.ui.listSelectedDays.addItems(selectedDayStrList)

    def onClickCalendar(self, date : QDate):
        if self.ticketDayModel.hasDate(date):
            self.ticketDayModel.removeDate(date)
        else:
            self.ticketDayModel.addDate(date)
        self.updateBuyTicketDays(self.ticketDayModel.getSeletedDays())

    def onBuyTicket(self):
        logging.info("Start buy ticket")
        self.ui.listBuyDays.clear()
        busInfo = BusInfo()
        self.requireBusInfo.emit(busInfo)
        logging.info("Bus info: %s" % str(busInfo))