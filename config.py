#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtCore import QSettings

class UserData(object):
    ORG_NAME = "jepeng"
    APP_NAME = "eTicket"

    LOGIN_NAME_STR = "loginName"
    KEY_CODE_STR = "KeyCode"
    CUSTOMER_ID_STR = "CustomerId"

    def __init__(self):
        self.settings = QSettings(UserData.ORG_NAME, UserData.APP_NAME)

    @property
    def loginName(self):
        return self.settings.value(UserData.LOGIN_NAME_STR, "")
    @loginName.setter
    def loginName(self, name):
        self.settings.setValue(UserData.LOGIN_NAME_STR, name)


userData = UserData()