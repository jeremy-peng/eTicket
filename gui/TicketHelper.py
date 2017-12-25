#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtCore import QDate

from config import userData
from eBus import request


def _getRemindTicketTicketObj(lineId : str, vehTime: str, year : int, month : int, day = 1):
    if lineId == "" or vehTime == "" or \
                    userData.customerId == "" or userData.loginName == "" or userData.keyCode == "":
        return None
    startDate = QDate(year, month, day)
    endDate = QDate(year, month, startDate.daysInMonth())
    startDateStr, endDateStr = startDate.toString("yyyyMMdd"), endDate.toString("yyyyMMdd")
    remindTicketObj = request.requireRemindTicket(userData.customerId, userData.loginName, userData.keyCode,
                                                  lineId, vehTime, startDateStr, endDateStr)
    if remindTicketObj is None:
        return None
    return remindTicketObj

def getRemindTicketNumber(lineId : str, vehTime: str, year : int, month : int, day = 1):
    remindTicketObj = _getRemindTicketTicketObj(lineId, vehTime, year, month, day)
    if remindTicketObj is None:
        return (None, None)
    remindTicketList = remindTicketObj.returnData.tickets.split(',')
    remindTicketNumList = list(map(int, remindTicketList))
    ticketPriceStrList = remindTicketObj.returnData.prices.split(',')
    ticketPriceList = list(map(float, ticketPriceStrList))
    return remindTicketNumList, ticketPriceList



if __name__ == '__main__':
    pass
