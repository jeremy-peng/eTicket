import requests

url = 'http://ewrite.szebus.net/phone/login/new'

kw = {'loginName': '18118728184', 'loginCode' : '8875'}


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

if __name__ == "__main__":
    print(str2payload("customerId=166015&customerName=18823188184&keyCode=e2a3fc18953547b3d74096973d7524b5&lineId=11896&vehTime=1732&beginDate=20171204&endDate=20171231"))
    # payloadStr = payload2Str(kw)
    # r = requests.post(url, data = kw, headers = formatHeader(payloadStr))
    # print(r.json())