import sys

from PyQt5.QtCore import QDate

from gui import  Application
import  logging


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

def main():
    a = ["1133", "2222"]
    b = ["3444" ,"4444"]
    #c = combindList(a, b, '-')
    for i in range(1, 32):
        date = QDate(2017,12,i)
        print(date.dayOfWeek())


if __name__ == "__main__":
    main()