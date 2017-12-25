#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
from builtins import isinstance
from collections import namedtuple
from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5.QtCore import QDate


def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data):
    if isinstance(data, str):
        return json.loads(data, object_hook=_json_object_hook)
    elif isinstance(data, dict):
        return json2obj(json.dumps(data))


def combineList(l1 : list, l2 : list, connector : str):
    '''
    :param l1: ["a", "b", "c"]
    :param l2: ['1', '2', '3']
    :param connector:  '-'
    :return: ['a-1', 'b-2', 'c-3']
    '''
    if len(l1) != len(l2):
        return None
    ret = []
    for i, value in enumerate(l1):
        ret.append(value + connector + l2[i])
    return ret

def _formatTime(timeStr : str):
    timeStr = timeStr[:2] + ":" + timeStr[2:]
    return timeStr

def getFormatTime(timeList : list):
    """
    :param timeList: ['1122','3344']
    :return: ['11:22', '33:44']
    """
    return list(map(_formatTime, timeList))


def getStartEndDateStr(year : int, month : int):
    startDate = QDate(year, month, 1)

    endDate = QDate(year, month, startDate.daysInMonth())

    return startDate.toString("yyyyMMdd"), endDate.toString("yyyyMMdd")

def getStartEndDate(year : int, month : int):
    startDate = QDate(year, month, 1)

    endDate = QDate(year, month, startDate.daysInMonth())

    return startDate, endDate


def raiseTopMainWindow():
    topWin = None
    for win in QApplication.instance().topLevelWidgets():
        if isinstance(win, QMainWindow):
            topWin = win
            break
    if topWin is not None:
        topWin.showNormal()
        topWin.activateWindow()

if __name__ == '__main__':
    data = """
    {"returnCode":"500","returnData":[{"id":263034,"isEnd":1,"isFirst":1,"isLabel":1,"lineId":10618,"lineNo":"P177-1","mileage":80.97,"needTime":100,"offGeogId":5,"offStationId":517003,"offStationName":"深圳湾口岸（临时站）","onGeogId":8,"onStationId":511450,"onStationName":"双龙地铁站②","openType":1,"perNum":0,"price":10,"startTime":"0700","status":5,"tradePrice":10,"vehTime":"0700"},{"id":263218,"isEnd":1,"isFirst":1,"isLabel":1,"lineId":11896,"lineNo":"P177-2","mileage":73.19,"needTime":70,"offGeogId":8,"offStationId":20527,"offStationName":"香林世纪华府","onGeogId":5,"onStationId":512493,"onStationName":"A8音乐大厦（临时站）","openType":1,"perNum":0,"price":10,"startTime":"1732","status":5,"tradePrice":10,"vehTime":"1732"}],"returnInfo":"获取成功","returnSize":2}
    """
    x = json2obj(data)

    print(x)

    print(x.returnCode)
    print(x.returnData[0].lineNo)

    print(getStartEndDateStr(2017, 11))