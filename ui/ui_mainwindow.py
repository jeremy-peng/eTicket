# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(922, 814)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/bus.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 881, 721))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setGeometry(QtCore.QRect(390, 360, 441, 291))
        self.groupBox_5.setObjectName("groupBox_5")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.groupBox_5)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 30, 248, 197))
        self.calendarWidget.setObjectName("calendarWidget")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton.setGeometry(QtCore.QRect(40, 250, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox.setGeometry(QtCore.QRect(120, 260, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.listWidget_4 = QtWidgets.QListWidget(self.groupBox_5)
        self.listWidget_4.setGeometry(QtCore.QRect(270, 30, 151, 201))
        self.listWidget_4.setObjectName("listWidget_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 260, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setGeometry(QtCore.QRect(170, 260, 71, 16))
        self.label_3.setObjectName("label_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(600, 10, 151, 311))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget_3 = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget_3.setObjectName("listWidget_3")
        self.verticalLayout.addWidget(self.listWidget_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 90, 276, 224))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(90, 60, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 54, 12))
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(320, 10, 231, 321))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout.addWidget(self.listWidget_2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setGeometry(QtCore.QRect(40, 360, 341, 281))
        self.groupBox_4.setObjectName("groupBox_4")
        self.calendarTicket = QtWidgets.QCalendarWidget(self.groupBox_4)
        self.calendarTicket.setGeometry(QtCore.QRect(40, 70, 248, 197))
        self.calendarTicket.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendarTicket.setGridVisible(True)
        self.calendarTicket.setSelectionMode(QtWidgets.QCalendarWidget.NoSelection)
        self.calendarTicket.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarTicket.setNavigationBarVisible(True)
        self.calendarTicket.setDateEditEnabled(False)
        self.calendarTicket.setObjectName("calendarTicket")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 30, 71, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 30, 113, 20))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(110, 30, 71, 16))
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 30, 16))
        self.label.setObjectName("label")
        self.labelUserName = QtWidgets.QLabel(self.centralwidget)
        self.labelUserName.setGeometry(QtCore.QRect(60, 10, 121, 16))
        self.labelUserName.setObjectName("labelUserName")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 922, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_5.setTitle(_translate("MainWindow", "购票"))
        self.pushButton.setText(_translate("MainWindow", "购票"))
        self.checkBox.setText(_translate("MainWindow", "刷票"))
        self.label_3.setText(_translate("MainWindow", "刷票间隔(s):"))
        self.groupBox_3.setTitle(_translate("MainWindow", "下车点"))
        self.groupBox_2.setTitle(_translate("MainWindow", "车次"))
        self.label_2.setText(_translate("MainWindow", "线路:"))
        self.groupBox.setTitle(_translate("MainWindow", "上车点"))
        self.groupBox_4.setTitle(_translate("MainWindow", "余票:"))
        self.checkBox_2.setText(_translate("MainWindow", "自动刷新"))
        self.label_4.setText(_translate("MainWindow", "刷票间隔(s):"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "查询购票"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "订单"))
        self.label.setText(_translate("MainWindow", "你好:"))
        self.labelUserName.setText(_translate("MainWindow", "UserName"))

