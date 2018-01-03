#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QAbstractItemView
from ui.ui_tickets_order_widget import Ui_TicketOrderWidget
from gui.OrderTableModel import OrderTableModel


class TicketOrderWidget(QWidget):

    def __init__(self, parent = None):
        super(TicketOrderWidget, self).__init__(parent)
        self.ui = Ui_TicketOrderWidget()
        self.ui.setupUi(self)
        self.completeOrderModel = OrderTableModel()
        self.initUI()

    def setOperationWidgetsShown(self, shown : bool):
        self.ui.groupOrderOperationWidgets.setVisible(shown)

    def initUI(self):
        self.ui.tableOrderView.setModel(self.completeOrderModel)
        self.ui.tableOrderView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tableOrderView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.ui.tableOrderDetailView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tableOrderDetailView.setSelectionBehavior(QAbstractItemView.SelectRows)


    def setOrderList(self, orderList):
        self.completeOrderModel.setOrderData(orderList)

    def resizeColumnsToContents(self):
        self.ui.tableOrderView.resizeColumnsToContents()
        self.ui.tableOrderDetailView.resizeColumnsToContents()



if __name__ == '__main__':
    pass
