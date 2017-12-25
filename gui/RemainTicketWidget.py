#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QDate, Qt, QTimer
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
        self.ui.checkAutoRefresh.clicked.connect(self.onCheckAutoRefresh)


    def initUI(self):
        self.ui.calendarTicket.setSelectedDate(QDate(1990,1,1))
        self.ui.calendarTicket.showToday()



    def onCalendarPageChanged(self, year : int, month : int):
        logging.info("calendar page change  year:%s, month:%s" % (year, month))
        self.curDate.setDate(year, month, 1)
        self.checkRemindTicket()


    def checkRemindTicket(self):
        startDate = QDate(self.curDate.year(), self.curDate.month(), 1)
        remindTicketNumber = TicketHelper.getRemindTicketNumber(self.lineId,
                                                                self.busStartTime, self.curDate.year(), self.curDate.month())
        if remindTicketNumber is None:
            return
        logging.info("Check remind ticket lists:" + str(remindTicketNumber))
        self.updateCalendarTicketStatus(startDate, remindTicketNumber)


    def updateCalendarTicketStatus(self, startDate : QDate, ticketList : list):
        if startDate.isValid() == False or len(ticketList) == 0:
            return
        # clear all date format
        self.ui.calendarTicket.setDateTextFormat(QDate(), QTextCharFormat())

        for remindTicket in ticketList:
            if remindTicket > 0:
                self.ui.calendarTicket.setDateTextFormat(startDate, RemindTicketWidget.hasTicketText)
            else:
                self.ui.calendarTicket.setDateTextFormat(startDate, RemindTicketWidget.noneTicketText)
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




