#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal
from ui.ui_search_bus_widget import Ui_SearchBusWidget
from eBus import request
import logging
from config import userData
import  util
from gui.BusInfo import BusInfo


class SearchBusWidget(QWidget):
    selectedBus = pyqtSignal(str, str)
    def __init__(self, parent):
        super(SearchBusWidget, self).__init__(parent)
        self.ui = Ui_SearchBusWidget()
        self.ui.setupUi(self)
        self.curLineListObj = None
        self.curBusDetailObj =None
        self.ui.textBusLine.setText(userData.lastBusNum)

    def onBtnSearchBusClicked(self):
        busLine = self.ui.textBusLine.text()
        logging.debug("input line: %s" % busLine)
        if busLine == "":
            QMessageBox.critical(self, "Error", "Input bus line.")
            return;
        busLineListObj = request.requireSearchBus(busLine)
        if busLineListObj is None:
            QMessageBox.critical(self, "Error", "Error happens while searching line:%s" %busLine)
            self.clearBusLine()
            return
        if len(busLineListObj.returnData) == 0:
            QMessageBox.critical(self, "Error", "Line:%s doesn't exist" %busLine)
            self.clearBusLine()
            return
        self.updateBusLineList(busLineListObj)
        userData.lastBusNum = busLine


    def clearBusLine(self):
        self.ui.listBusLine.clear()
        self.ui.listOffStation.clear()
        self.ui.listOnStation.clear()
        self.ui.textBusInfo.clear()
        self.curLineListObj = None


    def updateBusLineList(self, lineListObj):
        self.clearBusLine()
        self.curLineListObj = lineListObj
        if lineListObj is None:
            return
        for lineInfo in lineListObj.returnData:
            logging.info("add bus line: %s" % lineInfo.lineNo)
            self.ui.listBusLine.addItem(lineInfo.lineNo)


    def onBusLineSeletedChange(self, index):
        if index < 0:
            return
        if self.curLineListObj is None or self.curLineListObj.returnData is None:
            logging.info("curLineListObj is None")
            return
        if index >= len(self.curLineListObj.returnData):
            logging.info("index exceed bus lines.")
            return
        lineInfo = self.curLineListObj.returnData[index]
        lineText, lineId = lineInfo.lineNo, lineInfo.lineId
        logging.info("select line:%s id:%s" %(lineText, lineId))
        #require detail bus info
        busDetailObj = request.requireBusDetail(lineId, userData.loginName, userData.customerId, userData.keyCode,
                                                lineInfo.vehTime, lineInfo.onStationId, lineInfo.offStationId)
        if busDetailObj is None:
            logging.info("bus detail is none.")
            return
        self.curBusDetailObj = busDetailObj.returnData
        self.updateBusInfoText(self.curBusDetailObj)
        self.updateOnOffStation(self.curBusDetailObj)
        self.selectedBus.emit(str(lineId), self.curBusDetailObj.vehTime)

    def updateOnOffStation(self, busDetailObj):
        onStationNames, onStationTimes = busDetailObj.onStations.split(';'),\
                                         util.getFormatTime(busDetailObj.onTimes.split(';'))
        offStationNames, offStationTimes = busDetailObj.offStations.split(';'),\
                                           util.getFormatTime(busDetailObj.offTimes.split(';'))
        connector = ' - '
        onStationText = util.combineList(onStationNames, onStationTimes, connector)
        offStationText = util.combineList(offStationNames, offStationTimes, connector)
        self.ui.listOffStation.clear()
        self.ui.listOnStation.clear()
        self.ui.listOnStation.addItems(onStationText)
        self.ui.listOffStation.addItems(offStationText)


    def updateBusInfoText(self, busDetailObj):
        if busDetailObj is None:
            return
        busInfoText = "lineId: {0}\n" \
        "lineNo: {1}\n" \
        "mileage: {2}(km)\n" \
        "needTime: {3}(min)\n" \
        "isCl: {4}\n" \
        "openType: {5}\n" \
        "perNum: {6} \n" \
        "price: {7}\n" \
        "tradePrice: {8}\n" \
        "status: {9}\n"
        busInfoText = busInfoText.format(busDetailObj.lineId, busDetailObj.lineNo,
                                         busDetailObj.mileage, busDetailObj.needTime, busDetailObj.isCl,
                                         busDetailObj.openType, busDetailObj.perNum, busDetailObj.price,
                                         busDetailObj.tradePrice, busDetailObj.status
                                         )
        self.ui.textBusInfo.setText(busInfoText)

    def onRequireBusInfo(self, busInfo : BusInfo):
        logging.info("Try require bus info")
        if (self.curBusDetailObj is None):
            QMessageBox.critical(self, "Error", "Please select bus line first.")
            return
        onStationIndex = self.ui.listOnStation.currentRow()
        offStationIndex = self.ui.listOffStation.currentRow()
        busInfo.lineId = self.curBusDetailObj.lineId
        busInfo.lineNo = self.curBusDetailObj.lineNo
        busInfo.vehTime = self.curBusDetailObj.vehTime
        if onStationIndex >= 0:
            busInfo.startTime = self.curBusDetailObj.onTimes.split(';')[onStationIndex]
            busInfo.onStationId = self.curBusDetailObj.onStationIds.split(';')[onStationIndex]

        busInfo.tradePrice = self.curBusDetailObj.tradePrice
        if offStationIndex >= 0:
            busInfo.offStationId = self.curBusDetailObj.offStationIds.split(';')[offStationIndex]