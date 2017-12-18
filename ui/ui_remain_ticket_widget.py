# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_remain_ticket_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_remainTicketWidget(object):
    def setupUi(self, remainTicketWidget):
        remainTicketWidget.setObjectName("remainTicketWidget")
        remainTicketWidget.resize(414, 439)
        self.verticalLayout = QtWidgets.QVBoxLayout(remainTicketWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_4 = QtWidgets.QGroupBox(remainTicketWidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_5.addWidget(self.checkBox_2)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_5.addWidget(self.lineEdit_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.calendarTicket = QtWidgets.QCalendarWidget(self.groupBox_4)
        self.calendarTicket.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendarTicket.setGridVisible(True)
        self.calendarTicket.setSelectionMode(QtWidgets.QCalendarWidget.NoSelection)
        self.calendarTicket.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarTicket.setNavigationBarVisible(True)
        self.calendarTicket.setDateEditEnabled(False)
        self.calendarTicket.setObjectName("calendarTicket")
        self.verticalLayout_4.addWidget(self.calendarTicket)
        self.verticalLayout.addWidget(self.groupBox_4)

        self.retranslateUi(remainTicketWidget)
        QtCore.QMetaObject.connectSlotsByName(remainTicketWidget)

    def retranslateUi(self, remainTicketWidget):
        _translate = QtCore.QCoreApplication.translate
        remainTicketWidget.setWindowTitle(_translate("remainTicketWidget", "Form"))
        self.groupBox_4.setTitle(_translate("remainTicketWidget", "余票:"))
        self.checkBox_2.setText(_translate("remainTicketWidget", "自动刷新"))
        self.label_4.setText(_translate("remainTicketWidget", "  间隔(s):"))

