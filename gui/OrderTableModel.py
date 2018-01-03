#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant, QModelIndex
from collections import namedtuple

class OrderTableModel(QAbstractTableModel):
    HeaderLabels = ['Line', 'StartTime', 'Mile', 'OnStation','OffStation', 'Price', 'Status', 'OrderTime']

    OrderInfo = namedtuple('OrderInfo', 'lineNo startTime mileage onStationName offStationName originalPrice status'
                                        ' orderTime dayNum payType  vehTime id')

    def __init__(self, parent = None):
        super(OrderTableModel, self).__init__(parent)
        self.orderDataList = []

    def headerData(self, p_int, Qt_Orientation, role=None):
        if role != Qt.DisplayRole:
            return None
        if Qt_Orientation == Qt.Horizontal:
            return OrderTableModel.HeaderLabels[p_int]
        return None

    def columnCount(self, parent=None, *args, **kwargs):
        return len(OrderTableModel.HeaderLabels)

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.orderDataList)

    def data(self, index : QModelIndex, role=None):
        if not index.isValid() or role != Qt.DisplayRole:
            return QVariant()
        row = index.row()
        column = index.column()
        if row >= len(self.orderDataList):
            return QVariant()
        return self.orderDataList[row][column]


    def setOrderData(self, orderDataList : list):
        if len(orderDataList) == 0:
            return
        self.beginResetModel()
        for orderObj in orderDataList:
            statusStr = ''
            if orderObj.status == 0:
                statusStr = '未完成'
            elif orderObj.status == 1:
                statusStr = '已取消'
            elif orderObj.status == 2:
                statusStr = '已完成'
            orderInfo = OrderTableModel.OrderInfo(orderObj.lineNo, orderObj.startTime, orderObj.mileage,
                                                  orderObj.onStationName, orderObj.offStationName, orderObj.originalPrice,
                                                  statusStr, orderObj.orderTime, orderObj.dayNum, orderObj.payType,
                                                  orderObj.vehTime, orderObj.id)
            self.orderDataList.append(orderInfo)
        self.endResetModel()

if __name__ == '__main__':
    pass
