#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import QTextCharFormat
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import QDate, Qt, pyqtSignal

from ui.ui_buy_ticket_widget import Ui_BuyTicketWidget
from gui.BuyTicketDateModel import BuyTicketDateModel
import logging
from gui.BusInfo import BusInfo
from gui.TicketHelper import TicketStatus
from config import userData
from gui import TicketHelper
from eBus import request

class BuyTicketWidget(QWidget):


    requireBusInfo = pyqtSignal(BusInfo)
    calendarPageChanged = pyqtSignal(int, int)


    def __init__(self, parent = None):
        super(BuyTicketWidget, self).__init__(parent)
        self.ui = Ui_BuyTicketWidget()
        self.ui.setupUi(self)
        self.ticketDateModel = BuyTicketDateModel()
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
        self.ticketDateModel.setDate(curDate.year(), curDate.month())
        self.ui.textSZBusCard.setText(userData.sztNum)


    def onSelectedAllDays(self):
        logging.info("select all days")
        self.ticketDateModel.selectAllDays()
        self.updateTicketStatus(self.ticketDateModel.getSelectedDays(), self.ticketDateModel.getBookedDays())

    def onInvertSelectedDays(self):
        logging.info("invert all days")
        self.ticketDateModel.invertSelectDay()
        self.updateTicketStatus(self.ticketDateModel.getSelectedDays(), self.ticketDateModel.getBookedDays())

    def onSelectedAllWorkDays(self):
        logging.info("select all work days")
        self.ticketDateModel.selectAllWorkDays()
        self.updateTicketStatus(self.ticketDateModel.getSelectedDays(), self.ticketDateModel.getBookedDays())

    def onSelectedAllWeekDays(self):
        logging.info("invert all week days")
        self.ticketDateModel.selectAllWeekDays()
        self.updateTicketStatus(self.ticketDateModel.getSelectedDays(), self.ticketDateModel.getBookedDays())

    def onClearAllDays(self):
        logging.info("clear all selected")
        self.ticketDateModel.clearSelectedDays()
        self.updateTicketStatus(self.ticketDateModel.getSelectedDays(), self.ticketDateModel.getBookedDays())

    def setCurrentPage(self, year : int, month : int):
        self.ui.calendarWidget.setCurrentPage(year, month)

    def onCurrentPageChanged(self, year, month):
        self.ticketDateModel.setDate(year, month)
        self.updateBookedTicketDays(year, month)
        self.updateTicketStatus(self.ticketDateModel.getSelectedDays(), self.ticketDateModel.getBookedDays())

    def updateBookedTicketDays(self, year, month):
        busInfo = BusInfo()
        self.requireBusInfo.emit(busInfo)
        logging.info("Bus info: %s" % str(busInfo))
        if not busInfo.isValid():
            return
        remindTicketNum, ticketPriceList = TicketHelper.getRemindTicketInfo(busInfo.lineId, busInfo.vehTime,
                                                                            year, month)
        if ticketPriceList is None or len(ticketPriceList) == 0 :
            return
        startDate = QDate(year, month, 1)
        bookedDays = [QDate(year, month, i + 1) for i in range(startDate.daysInMonth()) if ticketPriceList[i] == -2 ]
        self.ticketDateModel.setBookedDate(bookedDays)


    def updateTicketStatus(self, selectedDays : list, bookedDays : list):
        self.ui.calendarWidget.setDateTextFormat(QDate(), QTextCharFormat())
        self.ui.listSelectedDays.clear()
        selectedDayStrList = []
        for date in bookedDays:
            self.ui.calendarWidget.setDateTextFormat(date, TicketStatus.BookedTicketText)
        for date in selectedDays:
            self.ui.calendarWidget.setDateTextFormat(date, TicketStatus.SelectedTicketText)
            selectedDayStrList.append(date.toString("yyyyMMdd"))

        self.ui.listSelectedDays.addItems(selectedDayStrList)

    def onClickCalendar(self, date : QDate):
        if self.ticketDateModel.hasSelectedDate(date):
            self.ticketDateModel.removeSelectedDate(date)
        else:
            self.ticketDateModel.addSelectedDate(date)
        self.updateTicketStatus(self.ticketDateModel.getSelectedDays(), self.ticketDateModel.getBookedDays())

    def onBuyTicket(self):
        logging.info("Start buy ticket")
        self.ui.listBuyDays.clear()
        busInfo = BusInfo()
        self.requireBusInfo.emit(busInfo)
        logging.info("Bus info: %s" % str(busInfo))
        if not busInfo.isValid():
            QMessageBox.critical(self, "Error", "Bus info isn't valid")
            return
        selectedDays = self.ticketDateModel.getSelectedDays()
        if len(selectedDays) == 0:
            QMessageBox.critical(self, 'Error', 'Please select date first.')

        remindTicketNum, ticketPriceList = TicketHelper.getRemindTicketInfo(busInfo.lineId, busInfo.vehTime,
                                                                            self.ticketDateModel.year, self.ticketDateModel.month)
        if remindTicketNum is None or len(remindTicketNum) == 0 :
            return
        buyTicketDays = []
        startDate = QDate(self.ticketDateModel.year, self.ticketDateModel.month, 1)
        allDateHasTicket = [QDate(self.ticketDateModel.year, self.ticketDateModel.month, i + 1) for i in range(startDate.daysInMonth())
                            if remindTicketNum[i] > 0]
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
        buyTicketResponseObj = request.requireBuyTicket(userData.customerId, userData.loginName, userData.keyCode,
                                 busInfo.lineId, busInfo.vehTime, busInfo.startTime,
                                 busInfo.onStationId, busInfo.offStationId, totalPrice,
                                 userData.sztNum, buyTicketDayStrList)
        if buyTicketResponseObj is None:
            QMessageBox.critical(self, "Error", 'fail to buy ticket')
            return




    def onTextSZTEditFinished(self):
        userData.sztNum = self.ui.textSZBusCard.text()