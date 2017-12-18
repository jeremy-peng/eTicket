from PyQt5.QtWidgets import QWidget, QMessageBox
from ui.ui_search_bus_widget import Ui_SearchBusWidget
from eBus import request
import sys


class SearchBusWidget(QWidget):
    def __init__(self, parent):
        super(SearchBusWidget, self).__init__(parent)
        self.ui = Ui_SearchBusWidget()
        self.ui.setupUi(self)
        self.lineListObj = None

    def onBtnSearchBusClicked(self):
        busLine = self.ui.textBusLine.text()
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


    def clearBusLine(self):
        self.ui.listBusLine.clear()
        self.ui.listOffStation.clear()
        self.ui.listOnStation.clear()

    def updateBusLineList(self, lineListObj):
        if lineListObj is None:
            return
        for lineInfo in lineListObj.returnData:
            self.ui.listBusLine.addItem(lineInfo.lineNo)
