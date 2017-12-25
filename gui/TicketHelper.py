#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtCore import QDate

from config import userData
from eBus import request

def getRemindTicketNumber(lineId : str, vehTime: str, year : int, month : int, day = 1):
    if lineId == "" or vehTime == "" or \
                    userData.customerId == "" or userData.loginName == "" or userData.keyCode == "":
        return None
    startDate = QDate(year, month, day)
    endDate = QDate(year, month, startDate.daysInMonth())
    startDateStr, endDateStr = startDate.toString("yyyyMMdd"), endDate.toString("yyyyMMdd")
    remindTicketObj = request.requireRemindTicket(userData.customerId, userData.loginName, userData.keyCode,
                                                  lineId, vehTime, startDateStr, endDateStr)
    if remindTicketObj is None:
        return
    remindTicketList = remindTicketObj.returnData.tickets.split(',')
    remindTicketNum = list(map(int, remindTicketList))
    return remindTicketNum



if __name__ == '__main__':
    pass
