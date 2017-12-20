#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtCore import QSettings

class UserData(object):
    ORG_NAME = "jepeng"
    APP_NAME = "eTicket"

    LOGIN_NAME_STR = "loginName"
    KEY_CODE_STR = "KeyCode"
    CUSTOMER_ID_STR = "CustomerId"
    LAST_INPUT_BUS_NUM = "LastInputBusNum"

    def __init__(self):
        self.settings = QSettings("settings.ini", QSettings.IniFormat)

    @property
    def loginName(self):
        return self.settings.value(UserData.LOGIN_NAME_STR, "")
    @loginName.setter
    def loginName(self, name):
        self.settings.setValue(UserData.LOGIN_NAME_STR, name)

    @property
    def keyCode(self):
        return self.settings.value(UserData.KEY_CODE_STR, "")
    @keyCode.setter
    def keyCode(self, code):
        self.settings.setValue(UserData.KEY_CODE_STR, code)

    @property
    def customerId(self):
        return self.settings.value(UserData.CUSTOMER_ID_STR, "")
    @customerId.setter
    def customerId(self, id):
        self.settings.setValue(UserData.CUSTOMER_ID_STR, id)

    @property
    def lastBusNum(self):
        return self.settings.value(UserData.LAST_INPUT_BUS_NUM, "")

    @lastBusNum.setter
    def lastBusNum(self, busNum):
        self.settings.setValue(UserData.LAST_INPUT_BUS_NUM, busNum)

    def sync(self):
        self.settings.sync()

userData = UserData()