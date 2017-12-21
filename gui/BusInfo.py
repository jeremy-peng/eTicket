#!/usr/bin/python3
# -*- coding: utf-8 -*-
class BusInfo(object):
    def __init__(self):
        self.lineId = ""
        self.vehTime = ""
        self.startTime = ""
        self.onStationId = ""
        self.offStationId = ""
        self.tradePrice = 0

    def __str__(self):
        return "lineId:{0}, vehTime:{1}, startTime:{2}, " \
               "onStationId:{3}, offStationId:{4}, tradePrice:{5}"\
            .format(self.lineId, self.vehTime, self.startTime, self.onStationId, self.offStationId, self.tradePrice)


if __name__ == '__main__':
    a = BusInfo()
    a.lineId="1234"
    a.vehTime = "2222"
    a.startTime = "3333"
    a.onStationId = "4444"
    a.offStationId = "5555"
    a.tradePrice = 10
    print(a)
    pass