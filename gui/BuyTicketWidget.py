#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import QTextCharFormat
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import QDate, Qt, pyqtSignal

from ui.ui_buy_ticket_widget import Ui_BuyTicketWidget
from gui.BuyTicketDateModel import BuyTicketDateModel
import logging
from gui.BusInfo import BusInfo
from config import userData
from gui import TicketHelper
from eBus import request

class BuyTicketWidget(QWidget):
    BuyTicketText = QTextCharFormat()
    BuyTicketText.setForeground(Qt.black)
    BuyTicketText.setBackground(Qt.green)
    requireBusInfo = pyqtSignal(BusInfo)
    calendarPageChanged = pyqtSignal(int, int)


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
        self.ui.calendarWidget.currentPageChanged.connect(self.calendarPageChanged)
        self.ui.calendarWidget.clicked.connect(self.onClickCalendar)
        self.ui.textSZBusCard.editingFinished.connect(self.onTextSZTEditFinished)


    def initUI(self):
        curDate = QDate.currentDate()
        self.ui.calendarWidget.setSelectedDate(curDate)
        self.ticketDayModel.setDate(curDate.year(), curDate.month())
        self.ui.textSZBusCard.setText(userData.sztNum)


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

    def setCurrentPage(self, year : int, month : int):
        self.ui.calendarWidget.setCurrentPage(year, month)

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
        if not busInfo.isValid():
            QMessageBox.critical(self, "Error", "Bus info isn't valid")
            return
        selectedDays = self.ticketDayModel.getSeletedDays()
        if len(selectedDays) == 0:
            QMessageBox.critical(self, 'Error', 'Please select date first.')

        remindTicketNum, ticketPriceList = TicketHelper.getRemindTicketNumber(busInfo.lineId, busInfo.vehTime,
                                                             self.ticketDayModel.year, self.ticketDayModel.month)
        if remindTicketNum is None or len(remindTicketNum) == 0 :
            return
        buyTicketDays = []
        startDate = QDate(self.ticketDayModel.year, self.ticketDayModel.month, 1)
        allDateHasTicket = [QDate(self.ticketDayModel.year, self.ticketDayModel.month, i + 1) for i in range(startDate.daysInMonth())
                            if remindTicketNum[i] > 0 ]
        logging.info('all days has ticket' + str(allDateHasTicket))
        for buyDay in selectedDays:
            if buyDay in allDateHasTicket:
                buyTicketDays.append(buyDay)

        if len(buyTicketDays) == 0:
            return

        buyTicketDayStrList = []
        for buyDay in buyTicketDays:
            buyTicketDayStrList.append(buyDay.toString('yyyy-MM-dd'))

        logging.info('select days has ticket' + str(buyTicketDayStrList))

        totalPrice = busInfo.tradePrice * len(buyTicketDayStrList)
        buyTicketResponObj = request.requireBuyTicket(userData.customerId, userData.loginName, userData.keyCode,
                                 busInfo.lineId, busInfo.vehTime, busInfo.startTime,
                                 busInfo.onStationId, busInfo.offStationId, totalPrice,
                                 userData.sztNum, buyTicketDayStrList)
        if buyTicketResponObj is None:
            QMessageBox.critical(self, "Error", 'fail to buy ticket')
            return




    def onTextSZTEditFinished(self):
        userData.sztNum = self.ui.textSZBusCard.text()