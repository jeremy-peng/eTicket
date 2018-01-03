#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QMessageBox
from ui.ui_tickets_order_widget import Ui_TicketOrderWidget
from gui.OrderTableModel import OrderTableModel,DetailInfoModel
import logging
from eBus import request
from config import userData


class TicketOrderWidget(QWidget):

    def __init__(self, parent = None):
        super(TicketOrderWidget, self).__init__(parent)
        self.ui = Ui_TicketOrderWidget()
        self.ui.setupUi(self)
        self.orderTableModel = OrderTableModel()
        self.detailTableModel = DetailInfoModel()
        self.initUI()
        self.initSignals()

    def setOperationWidgetsShown(self, shown : bool):
        self.ui.groupOrderOperationWidgets.setVisible(shown)

    def initUI(self):
        self.ui.tableOrderView.setModel(self.orderTableModel)
        self.ui.tableOrderView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tableOrderView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.ui.tableDetailView.setModel(self.detailTableModel)
        self.ui.tableDetailView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.ui.tableDetailView.setSelectionBehavior(QAbstractItemView.SelectRows)


    def initSignals(self):
        self.ui.tableOrderView.selectionModel().currentRowChanged.connect(self.onCurrentOrderRowChanged)
        self.ui.btnCancelOrder.clicked.connect(self.onBtnCancelOrder)
        self.ui.btnCancelSelectedDate.clicked.connect(self.onBtnCancelSelectedDateOrder)

    def setOrderList(self, orderList):
        self.orderTableModel.setOrderData(orderList)

    def resizeColumnsToContents(self):
        self.ui.tableOrderView.resizeColumnsToContents()
        self.ui.tableDetailView.resizeColumnsToContents()

    def onCurrentOrderRowChanged(self, current : QModelIndex, previous : QModelIndex):
        row = current.row()
        orderId = self.orderTableModel.getOrderId(row)
        if orderId < 0:
            return

        logging.info("select order row: {0}, id: {1}".format(row, orderId))
        self.updateDetailTable(orderId)


    def updateDetailTable(self, orderId):
        detailInfoObj = request.requireOrderDetail(orderId, userData.loginName, userData.customerId, userData.keyCode)
        if detailInfoObj is None:
            return
        self.detailTableModel.setDetailInfoList(detailInfoObj.returnData.secondList)
        self.ui.tableDetailView.resizeColumnsToContents()

    def onBtnCancelSelectedDateOrder(self):
        row = self.ui.tableOrderView.currentIndex().row()
        if row < 0:
            QMessageBox.critical(self, "Error", "Please select one order.")
        orderId = self.orderTableModel.getOrderId(row)

        selDateRows = self.ui.tableDetailView.selectionModel().selectedRows()
        if len(selDateRows) == 0:
            QMessageBox.critical(self, "Error", "Please select at latest one date.")
            return

        runDateList = []

        for modelIndex in selDateRows:
            dateRow = modelIndex.row()
            runDateList.append(self.detailTableModel.getRunDate(dateRow))

        if orderId < 0:
            return
        logging.info("Try to cancel order:{0} date:{1}".format(orderId, ','.join(runDateList)))

        if (QMessageBox.question(self, "Question",
                     "Are you sure to cancel this order contain:{0}".format(','.join(runDateList)),
                                 QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes):
            obj = request.requireCancelOrder(orderId, userData.loginName, userData.customerId, userData.keyCode, runDateList)
            self.updateDetailTable(orderId)
            if obj is None:
                logging.info("Fail to cancel order")


    def onBtnCancelOrder(self):
        row = self.ui.tableOrderView.currentIndex().row()
        if row < 0:
            QMessageBox.critical(self, "Error", "Please select one order.")
        orderId = self.orderTableModel.getOrderId(row)
        if orderId < 0:
            return
        logging.info("Try to cancel order:{0}".format(orderId))

        if (QMessageBox.question(self, "Question",
                                 "Are you sure to cancel this order?",
                                 QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes):
            obj = request.requireCancelOrder(orderId, userData.loginName, userData.customerId, userData.keyCode, [])
            if obj is None:
                logging.info("Fail to cancel order")



if __name__ == '__main__':
    pass
