#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QDate, Qt, QTimer, pyqtSignal
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtGui import QTextCharFormat
from gui import TicketHelper


from ui.ui_remain_ticket_widget import Ui_remainTicketWidget
from config import userData
import logging
from eBus import request


class RemindTicketWidget(QWidget):
    hasTicketText = QTextCharFormat()
    hasTicketText.setForeground(Qt.black)
    hasTicketText.setBackground(Qt.green)

    noneTicketText = QTextCharFormat()
    noneTicketText.setForeground(Qt.white)
    noneTicketText.setBackground(Qt.red)

    bookedTicketText = QTextCharFormat()
    bookedTicketText.setForeground(Qt.yellow)
    bookedTicketText.setBackground(Qt.blue)

    calendarPageChanged = pyqtSignal(int, int)
    calendarClicked = pyqtSignal(QDate)

    def __init__(self, parent = None):
        super(RemindTicketWidget, self).__init__(parent)
        self.ui = Ui_remainTicketWidget()
        self.ui.setupUi(self)
        self.lineId = ""
        self.busStartTime = ""
        todayDate = QDate.currentDate()
        self.curDate = QDate(todayDate.year(), todayDate.month(), 1)
        self.autoRefreshTimer = None
        self.initSignals()
        self.initUI()

    def onSelectedBus(self, lineId : str, busStartTime : str):
        logging.info("select bus: %s, time: %s" % (lineId, busStartTime))
        self.lineId = lineId
        self.busStartTime = busStartTime
        self.checkRemindTicket()



    def initSignals(self):
        self.ui.calendarTicket.currentPageChanged.connect(self.onCalendarPageChanged)
        self.ui.calendarTicket.currentPageChanged.connect(self.calendarPageChanged)
        self.ui.checkAutoRefresh.clicked.connect(self.onCheckAutoRefresh)
        self.ui.calendarTicket.clicked.connect(self.calendarClicked)


    def initUI(self):
        self.ui.calendarTicket.setSelectedDate(QDate(1990,1,1))
        self.ui.calendarTicket.showToday()
        hasTicketItem = self.ui.tableTicketStatusIndicator.item(0, 0)
        hasTicketItem.setText('有票')
        hasTicketItem.setBackground(RemindTicketWidget.hasTicketText.background())
        hasTicketItem.setForeground(RemindTicketWidget.hasTicketText.foreground())
        noneTicketItem = self.ui.tableTicketStatusIndicator.item(0, 1)
        noneTicketItem.setText('无票')
        noneTicketItem.setBackground(RemindTicketWidget.noneTicketText.background())
        noneTicketItem.setForeground(RemindTicketWidget.noneTicketText.foreground())
        bookTicketItem = self.ui.tableTicketStatusIndicator.item(0, 2)
        bookTicketItem.setText('已购')
        bookTicketItem.setBackground(RemindTicketWidget.bookedTicketText.background())
        bookTicketItem.setForeground(RemindTicketWidget.bookedTicketText.foreground())

    def setCurrentPage(self, year : int, month : int):
        self.ui.calendarTicket.setCurrentPage(year, month)



    def onCalendarPageChanged(self, year : int, month : int):
        logging.info("calendar page change  year:%s, month:%s" % (year, month))
        self.curDate.setDate(year, month, 1)
        self.checkRemindTicket()


    def checkRemindTicket(self):
        startDate = QDate(self.curDate.year(), self.curDate.month(), 1)
        remindTicketNumber, ticketPriceList = TicketHelper.getRemindTicketNumber(self.lineId,
                                                                self.busStartTime, self.curDate.year(), self.curDate.month())
        if remindTicketNumber is None:
            return
        logging.info("Check remind ticket lists:" + str(remindTicketNumber))
        logging.info("Check ticket price:" + str(ticketPriceList))
        self.updateCalendarTicketStatus(startDate, remindTicketNumber, ticketPriceList)


    def updateCalendarTicketStatus(self, startDate : QDate, remindTicketList : list, ticketPrice : list):
        if startDate.isValid() == False or len(remindTicketList) == 0:
            return
        # clear all date format
        self.ui.calendarTicket.setDateTextFormat(QDate(), QTextCharFormat())

        for i, remindTicket in enumerate(remindTicketList):
            textFormat = QTextCharFormat()
            if ticketPrice[i] == -2:
                # already booked
                textFormat = RemindTicketWidget.bookedTicketText
            else:
                if remindTicket > 0:
                    textFormat = RemindTicketWidget.hasTicketText
                else:
                    textFormat = RemindTicketWidget.noneTicketText
            self.ui.calendarTicket.setDateTextFormat(startDate, textFormat)
            startDate.setDate(startDate.year(), startDate.month(), startDate.day() + 1)

    def onCheckAutoRefresh(self, checked : bool):
        logging.info("onCheckAutoRefresh")
        if checked:
            if self.autoRefreshTimer is None:
                self.autoRefreshTimer = QTimer(self)
                self.autoRefreshTimer.timeout.connect(self.onAutoRefreshTimeout)
            timeIntervalSt = self.ui.textRefreshInterval.text()
            if timeIntervalSt == "":
                QMessageBox.critical(self, "Error",'Please input time interval')
                self.ui.checkAutoRefresh.setChecked(False)
                return
            timeInterval = int(timeIntervalSt) * 1000
            self.autoRefreshTimer.setInterval(timeInterval)
            self.autoRefreshTimer.start(timeInterval)
        else:
            if not self.autoRefreshTimer is None and self.autoRefreshTimer.isActive():
                self.autoRefreshTimer.stop()


    def onAutoRefreshTimeout(self):
        remindTickets = self.checkRemindTicket()





