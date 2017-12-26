#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QDate


class BuyTicketDateModel(object):
    def __init__(self):
        self.selectedDays = list()
        self.allDaySet = list()
        self.bookedDays = list()
        self._year = QDate.currentDate().year()
        self._month = QDate.currentDate().month()

    def setDate(self, year : int, month : int):
        self._year, self._month = year, month
        self.selectedDays.clear()
        self.bookedDays.clear()
        self.genAllDaySet()

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year : int):
        self._year = year
        self.genAllDaySet()

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month : int):
        self._month = month
        self.genAllDaySet()

    def addSelectedDate(self, date : QDate):
        if date not in self.bookedDays:
            self.selectedDays.append(date)

    def removeSelectedDate(self, date : QDate):
        for i, d in enumerate(self.selectedDays):
            if d == date:
                self.selectedDays.remove(d)
                break

    def addBookedDate(self, date : QDate, updateAllDay = True):
        if not self.hasBookedDate(date):
            self.bookedDays.append(date)
            if updateAllDay:
                self.genAllDaySet()
            if self.hasSelectedDate(date):
                self.removeSelectedDate(date)

    def addBookedDateList(self, days : list):
        for date in days:
            self.addBookedDate(date, False)
        self.genAllDaySet()


    def setBookedDate(self, dateList : list):
        self.bookedDays = dateList[:]
        self.genAllDaySet()

    def removeBookedDate(self, date : QDate):
        for i, d in enumerate(self.bookedDays):
            if d == date:
                self.bookedDays.remove(d)
                self.genAllDaySet()
                break

    def genAllDaySet(self):
        curDate = QDate(self._year, self._month, 1)
        dayInMonth = curDate.daysInMonth()
        self.allDaySet.clear()
        for i in range(1, dayInMonth + 1):
            date = QDate(self._year, self._month, i)
            if not self.hasBookedDate(date):
                self.allDaySet.append(date)


    def selectAllDays(self):
        self.selectedDays.clear()
        self.selectedDays = self.allDaySet[:]

    def invertSelectDay(self):
        tmpDate = self.selectedDays[:]
        self.selectedDays.clear()
        for date in self.allDaySet:
            if not date in tmpDate:
                self.selectedDays.append(date)


    def selectAllWeekDays(self):
        self.selectedDays.clear()
        for date in self.allDaySet:
            if date.dayOfWeek() == 6 or date.dayOfWeek() == 7:
                self.selectedDays.append(date)


    def selectAllWorkDays(self):
        self.selectedDays.clear()
        for date in self.allDaySet:
            if date.dayOfWeek() != 6 and date.dayOfWeek() != 7:
                self.selectedDays.append(date)

    def getSelectedDays(self):
        return self.selectedDays

    def clearSelectedDays(self):
        self.selectedDays.clear()

    def hasSelectedDate(self, date : QDate):
        return date in self.selectedDays

    def getBookedDays(self):
        return self.bookedDays

    def clearBookedDays(self):
        self.bookedDays.clear()
        self.genAllDaySet()

    def hasBookedDate(self, date : QDate):
        return date in self.bookedDays