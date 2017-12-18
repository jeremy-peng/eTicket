#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
from builtins import isinstance
from collections import namedtuple


def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data):
    if isinstance(data, str):
        return json.loads(data, object_hook=_json_object_hook)
    elif isinstance(data, dict):
        return json2obj(json.dumps(data))


if __name__ == '__main__':
    data = """
    {"returnCode":"500","returnData":[{"id":263034,"isEnd":1,"isFirst":1,"isLabel":1,"lineId":10618,"lineNo":"P177-1","mileage":80.97,"needTime":100,"offGeogId":5,"offStationId":517003,"offStationName":"深圳湾口岸（临时站）","onGeogId":8,"onStationId":511450,"onStationName":"双龙地铁站②","openType":1,"perNum":0,"price":10,"startTime":"0700","status":5,"tradePrice":10,"vehTime":"0700"},{"id":263218,"isEnd":1,"isFirst":1,"isLabel":1,"lineId":11896,"lineNo":"P177-2","mileage":73.19,"needTime":70,"offGeogId":8,"offStationId":20527,"offStationName":"香林世纪华府","onGeogId":5,"onStationId":512493,"onStationName":"A8音乐大厦（临时站）","openType":1,"perNum":0,"price":10,"startTime":"1732","status":5,"tradePrice":10,"vehTime":"1732"}],"returnInfo":"获取成功","returnSize":2}
    """
    x = json2obj(data)

    print(x)

    print(x.returnCode)
    print(x.returnData[0].lineNo)