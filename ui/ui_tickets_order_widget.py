# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_tickets_order_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TicketOrderWidget(object):
    def setupUi(self, TicketOrderWidget):
        TicketOrderWidget.setObjectName("TicketOrderWidget")
        TicketOrderWidget.resize(921, 485)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(TicketOrderWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(TicketOrderWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableOrderView = QtWidgets.QTableView(self.groupBox_2)
        self.tableOrderView.setObjectName("tableOrderView")
        self.tableOrderView.horizontalHeader().setStretchLastSection(True)
        self.tableOrderView.verticalHeader().setVisible(True)
        self.horizontalLayout.addWidget(self.tableOrderView)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(TicketOrderWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableDetailView = QtWidgets.QTableView(self.groupBox_3)
        self.tableDetailView.setObjectName("tableDetailView")
        self.horizontalLayout_2.addWidget(self.tableDetailView)
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        self.groupOrderOperationWidgets = QtWidgets.QGroupBox(TicketOrderWidget)
        self.groupOrderOperationWidgets.setObjectName("groupOrderOperationWidgets")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupOrderOperationWidgets)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnCancelOrder = QtWidgets.QPushButton(self.groupOrderOperationWidgets)
        self.btnCancelOrder.setObjectName("btnCancelOrder")
        self.verticalLayout.addWidget(self.btnCancelOrder)
        self.btnCancelSelectedDate = QtWidgets.QPushButton(self.groupOrderOperationWidgets)
        self.btnCancelSelectedDate.setObjectName("btnCancelSelectedDate")
        self.verticalLayout.addWidget(self.btnCancelSelectedDate)
        spacerItem = QtWidgets.QSpacerItem(20, 350, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3.addWidget(self.groupOrderOperationWidgets)
        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 1)

        self.retranslateUi(TicketOrderWidget)
        QtCore.QMetaObject.connectSlotsByName(TicketOrderWidget)

    def retranslateUi(self, TicketOrderWidget):
        _translate = QtCore.QCoreApplication.translate
        TicketOrderWidget.setWindowTitle(_translate("TicketOrderWidget", "Form"))
        self.groupBox_2.setTitle(_translate("TicketOrderWidget", "订单"))
        self.groupBox_3.setTitle(_translate("TicketOrderWidget", "详细"))
        self.groupOrderOperationWidgets.setTitle(_translate("TicketOrderWidget", "操作"))
        self.btnCancelOrder.setToolTip(_translate("TicketOrderWidget", "取消全部日期订单"))
        self.btnCancelOrder.setText(_translate("TicketOrderWidget", "取消订单"))
        self.btnCancelSelectedDate.setToolTip(_translate("TicketOrderWidget", "取消选择日期订单"))
        self.btnCancelSelectedDate.setText(_translate("TicketOrderWidget", "取消选择"))

