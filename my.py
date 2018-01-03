#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import QDate

from gui import  Application
import  logging
from config import userData
from eBus import request


def combindList(l1 : list, l2 : list, connector : str):
    if len(l1) != len(l2):
        return None
    ret = []
    for i, value in enumerate(l1):
        ret.append(value + connector + l2[i])
    return ret


def formatTime(timeStr : str):
    timeStr = timeStr[:2] + ":" + timeStr[2:]
    return timeStr

def getFormatTime(timeList : list):
    return list(map(formatTime, timeList))


class RefData(object):
    def __init__(self):
        self.a = ""
        self.b = 0


def funChangeData(d):
    d.a = "aaaa"
    d.b = 10




def main():
    print(','.join(["dd"]))


if __name__ == "__main__":
    main()