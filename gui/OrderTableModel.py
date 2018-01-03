#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant, QModelIndex
from collections import namedtuple
import util

class OrderTableModel(QAbstractTableModel):
    HeaderLabels = ['Line', 'StartTime', 'Mile', 'OnStation','OffStation', 'Price', 'Status', 'OrderTime', 'DayNum']

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
        elif Qt_Orientation == Qt.Vertical:
            return p_int + 1
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
        self.orderDataList.clear()
        for orderObj in orderDataList:
            statusStr = ''
            if orderObj.status == 0:
                statusStr = '未完成'
            elif orderObj.status == 1:
                statusStr = '已取消'
            elif orderObj.status == 2:
                statusStr = '已完成'
            orderInfo = OrderTableModel.OrderInfo(orderObj.lineNo, util.formatTime(orderObj.startTime), orderObj.mileage,
                                                  orderObj.onStationName, orderObj.offStationName, orderObj.originalPrice,
                                                  statusStr, orderObj.orderTime, orderObj.dayNum, orderObj.payType,
                                                  orderObj.vehTime, orderObj.id)
            self.orderDataList.append(orderInfo)
        self.endResetModel()

    def getOrderId(self, row : int):
        if row < 0 or row >= len(self.orderDataList):
            return -1
        return self.orderDataList[row].id

class DetailInfoModel(QAbstractTableModel):
    HeaderLabels = ['Date', 'Status']
    DetailInfo = namedtuple('DetailInfo', 'runDate status')

    def __init__(self, parent = None):
        super(DetailInfoModel, self).__init__(parent)
        self.detailInfoList = []

    def headerData(self, p_int, Qt_Orientation, role=None):
        if role != Qt.DisplayRole:
            return None
        if Qt_Orientation == Qt.Horizontal:
            return DetailInfoModel.HeaderLabels[p_int]
        elif Qt_Orientation == Qt.Vertical:
            return p_int + 1
        return None

    def columnCount(self, parent=None, *args, **kwargs):
        return len(DetailInfoModel.HeaderLabels)

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.detailInfoList)

    def data(self, index : QModelIndex, role=None):
        if not index.isValid() or role != Qt.DisplayRole:
            return QVariant()
        row = index.row()
        column = index.column()
        if row >= len(self.detailInfoList):
            return QVariant()
        return self.detailInfoList[row][column]


    def setDetailInfoList(self, detailInfoList : list):
        if len(detailInfoList) == 0:
            return
        self.beginResetModel()
        self.detailInfoList.clear()
        for detailInfoObj in detailInfoList:
            statusStr = ''
            if detailInfoObj.status == 0:
                statusStr = '未完成'
            elif detailInfoObj.status == 1:
                statusStr = '已取消'
            elif detailInfoObj.status == 2:
                statusStr = '已完成'
            orderInfo = DetailInfoModel.DetailInfo(detailInfoObj.runDate, statusStr)
            self.detailInfoList.append(orderInfo)
        self.endResetModel()

    def getRunDate(self, row : int):
        if row < 0 or row >= len(self.detailInfoList):
            return ''
        return self.detailInfoList[row].runDate

if __name__ == '__main__':
    pass
