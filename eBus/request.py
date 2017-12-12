import requests
import json

LOGIN_NAME_STR = "loginName"
CUSTOMER_NAME_STR = "customerName"
KEY_CODE_STR = "KeyCode"
CUSTOMER_ID_STR = "CustomerId"
RETURN_CODE_STR = "returnCode"
SUCCESS_CODE_STR = "500"


def formatHeader(content):
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "%s" % len(content),
        "Host": "ewrite.szebus.net",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.3.0"
    }
    return header

def payload2Str(kw):
    ret = ''
    for k, v in kw.items():
        ret += "%s=%s&" % (k, v)
    ret = ret[:-1]
    return ret;

def str2payload(s):
    items = s.split('&')
    kw = {}
    for item in items:
        t = item.split('=')
        kw[t[0]] = t[1]
    return kw

def validateUserData(customerName, customerId, keyCode):
    if ( customerName == None or len(customerName) == 0 or
        customerId == None or len(customerId) == 0 or
        keyCode == None or len(keyCode) == 0 ):
        return False
    url = "http://ewrite.szebus.net/phone/open"
    kw = {CUSTOMER_NAME_STR : customerName,
          CUSTOMER_ID_STR: customerId,
          KEY_CODE_STR: keyCode}
    r = requests.post(url, data = kw, headers = formatHeader(payload2Str(kw)))
    response = r.json()
    return response.get(RETURN_CODE_STR) == SUCCESS_CODE_STR



if __name__ == "__main__":
    print(validateUserData("18118728184", "307475", "704bc707a35c4c8cfdf08333322b9174"))
