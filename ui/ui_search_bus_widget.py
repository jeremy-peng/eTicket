# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_search_bus_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SearchBusWidget(object):
    def setupUi(self, SearchBusWidget):
        SearchBusWidget.setObjectName("SearchBusWidget")
        SearchBusWidget.resize(407, 388)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SearchBusWidget)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(SearchBusWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.textBusLine = QtWidgets.QLineEdit(self.groupBox_2)
        self.textBusLine.setObjectName("textBusLine")
        self.horizontalLayout_4.addWidget(self.textBusLine)
        self.btnSearchBus = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSearchBus.setObjectName("btnSearchBus")
        self.horizontalLayout_4.addWidget(self.btnSearchBus)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.listBusLine = QtWidgets.QListWidget(self.groupBox_2)
        self.listBusLine.setObjectName("listBusLine")
        self.verticalLayout_3.addWidget(self.listBusLine)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(SearchBusWidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listOnStation = QtWidgets.QListWidget(self.groupBox)
        self.listOnStation.setObjectName("listOnStation")
        self.horizontalLayout.addWidget(self.listOnStation)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(SearchBusWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listOffStation = QtWidgets.QListWidget(self.groupBox_3)
        self.listOffStation.setObjectName("listOffStation")
        self.verticalLayout.addWidget(self.listOffStation)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(SearchBusWidget)
        self.btnSearchBus.clicked.connect(SearchBusWidget.onBtnSearchBusClicked)
        QtCore.QMetaObject.connectSlotsByName(SearchBusWidget)

    def retranslateUi(self, SearchBusWidget):
        _translate = QtCore.QCoreApplication.translate
        SearchBusWidget.setWindowTitle(_translate("SearchBusWidget", "Form"))
        self.groupBox_2.setTitle(_translate("SearchBusWidget", "车次"))
        self.label_2.setText(_translate("SearchBusWidget", "线路:"))
        self.btnSearchBus.setText(_translate("SearchBusWidget", "查询"))
        self.groupBox.setTitle(_translate("SearchBusWidget", "上车点"))
        self.groupBox_3.setTitle(_translate("SearchBusWidget", "下车点"))

