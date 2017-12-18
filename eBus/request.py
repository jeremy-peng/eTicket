#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import json
import util

LOGIN_NAME_STR = "loginName"
LOGIN_CODE_STR = "loginCode"
CUSTOMER_NAME_STR = "customerName"
KEY_CODE_STR = "keyCode"
CUSTOMER_ID_STR = "CustomerId"
RETURN_CODE_STR = "returnCode"
RETURN_DATA_STR = "returnData"
SUCCESS_CODE_STR = "500"


def formatHeader(content : str, url : str):
    host = ""
    if url.find("ewrite") != -1 :
        host = "ewrite.szebus.net"
    else:
        host = "eread.szebus.net"
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "%s" % len(content),
        "Host": "%s" % host,
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.3.0"
    }
    return header

def payload2Str(kw : dict):
    ret = ''
    for k, v in kw.items():
        ret += "%s=%s&" % (k, v)
    ret = ret[:-1]
    return ret;

def str2payload(s: str):
    items = s.split('&')
    kw = {}
    for item in items:
        t = item.split('=')
        kw[t[0]] = t[1]
    return kw

def validateUserData(phoneNum : str, customerId : str, keyCode : str):
    if ( phoneNum == None or len(phoneNum) == 0 or
        customerId == None or len(customerId) == 0 or
        keyCode == None or len(keyCode) == 0 ):
        return False
    url = "http://ewrite.szebus.net/phone/open"
    kw = {CUSTOMER_NAME_STR : phoneNum,
          CUSTOMER_ID_STR: customerId,
          KEY_CODE_STR: keyCode}
    r = requests.post(url, data = kw, headers = formatHeader(payload2Str(kw), url))
    response = r.json()
    return response.get(RETURN_CODE_STR) == SUCCESS_CODE_STR

def requestSendPinCode(phoneNum : str):
    if phoneNum is None or phoneNum == "":
        return False
    url = "http://ewrite.szebus.net/code/phone/login"
    kw = {'Phone' : phoneNum}
    r = requests.post(url, data = kw, headers = formatHeader(payload2Str(kw), url))
    response = r.json()
    return response.get(RETURN_CODE_STR) == SUCCESS_CODE_STR

def requireLogin(phoneNum : str, pinCode: str):
    if phoneNum is None or phoneNum == "" or pinCode is None or pinCode == "":
        return False
    url = "http://ewrite.szebus.net/phone/login/new"
    kw = {LOGIN_NAME_STR : phoneNum,
          LOGIN_CODE_STR : pinCode}
    r = requests.post(url, data = kw, headers = formatHeader(payload2Str(kw), url))
    response = r.json()
    if (response.get(RETURN_CODE_STR) == SUCCESS_CODE_STR):
        return  str(response.get(RETURN_DATA_STR)), response.get(KEY_CODE_STR) # return customerId, keyCode
    else: return ('','')


def requireSearchBus(lineNum : str):
    if lineNum is None or lineNum == "":
        return None
    url = "http://eread.szebus.net/bc/phone/data"
    kw = {'lineNo' : lineNum,
          "pageNo=1" : 1,
          "pageNo=5" : 5}
    r = requests.post(url, data = kw, headers = formatHeader(payload2Str(kw), url))
    response = r.json()
    if response.get(RETURN_CODE_STR) != SUCCESS_CODE_STR:
        return None
    return util.json2obj(response)


if __name__ == "__main__":
    requireSearchBus("p177")
