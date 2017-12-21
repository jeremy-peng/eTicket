#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QTextCharFormat

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
        self.initSignals()
        self.lineId = ""
        self.busStartTime = ""
        todayDate = QDate.currentDate()
        self.curDate = QDate(todayDate.year(), todayDate.month(), 1)
        self.ui.calendarTicket.setSelectedDate(QDate(1990,1,1))
        self.ui.calendarTicket.showToday()


    def onSelectedBus(self, lineId : str, busStartTime : str):
        logging.info("select bus: %s, time: %s" % (lineId, busStartTime))
        self.lineId = lineId
        self.busStartTime = busStartTime
        self.checkRemindTicket()



    def initSignals(self):
        self.ui.calendarTicket.currentPageChanged.connect(self.onCalendarPageChanged)


    def onCalendarPageChanged(self, year : int, month : int):
        logging.info("calendar page change  year:%s, month:%s" % (year, month))
        self.curDate.setDate(year, month, 1)
        self.checkRemindTicket()

    def checkRemindTicket(self):
        if self.lineId == "" or self.busStartTime == "" or \
            userData.customerId == "" or userData.loginName == "" or userData.keyCode == "":
            return
        startDate = QDate(self.curDate.year(), self.curDate.month(), 1)
        endDate = QDate(self.curDate.year(),self.curDate.month(), self.curDate.daysInMonth())
        startDateStr, endDateStr = startDate.toString("yyyyMMdd"), endDate.toString("yyyyMMdd")
        remindTicketObj = request.requireRemindTicket(userData.customerId, userData.loginName,userData.keyCode,
                                                      self.lineId, self.busStartTime, startDateStr, endDateStr)
        if remindTicketObj is None:
            return
        remindTicketList = remindTicketObj.returnData.tickets.split(',')
        self.updateCalendarTicketStatus(startDate, remindTicketList)

    def updateCalendarTicketStatus(self, startDate : QDate, ticketList : list):
        if startDate.isValid() == False or len(ticketList) == 0:
            return
        # clear all date format
        self.ui.calendarTicket.setDateTextFormat(QDate(), QTextCharFormat())

        for remindTicket in ticketList:
            if int(remindTicket) > 0:
                self.ui.calendarTicket.setDateTextFormat(startDate, RemindTicketWidget.hasTicketText)
            else:
                self.ui.calendarTicket.setDateTextFormat(startDate, RemindTicketWidget.noneTicketText)
            startDate.setDate(startDate.year(), startDate.month(), startDate.day() + 1)


