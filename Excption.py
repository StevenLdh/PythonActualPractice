#!/usr/bin/env python
# -*- coding:utf8 -*-

'''
# 捕获异常处理
num1 = input("please input a num1:")
num2 = input("please input a num1:")
try:
    print(float(num1)/float(num2))
except ZeroDivisionError:
    print("error")
finally:
    print("over")

assert (float(num2) != 0),'Error!'
print(float(num1)/float(num2))
'''
import requests
from urllib.parse import urlencode
import json
def get_page():
    params = {
        '___method': 'cc.erp.bll.report.reportmanager.getdatalist',
        'pagetype': 'erp',
        'from': 'allinoneclient',
        'platform': 'pc',
        's': '63c8be8fa3f3b42e',
        'tok': '346f6f14de5543ce8826af3a4d4691a0'
    }
    param = {
        "reportparam": {
            "orders": "",
            "parid": 0,
            "pagetype": "erp",
            "displaytype": "tree",
            "pagerow": 19,
            "pagenumber": 0
        },
        "conditionparam": {
            "sid": "",
            "sfullname": "",
            "gfullname": "",
            "dfullname1": "",
            "did1": "",
            "showtree": "false",
            "showqtytype": "-1",
            "isexchange": "-1",
            "showstop": "-1",
            "shownotused": "false",
            "brandid": "",
            "keywords": "",
            "showstopstatus": "0",
            "deal1name": "",
            "deal2name": "",
            "brandname": "",
            "showcansaleqtytype": "-1",
            "showrealqtyqtytype": "-1",
            "pagetype": "erp",
            "pageid": "stock_allstatus",
            "usedeal1": 0,
            "usedeal2": 0,
            "usedeal3": 0,
            "dealsfullname": "",
            "deal1id": "",
            "deal2id": ""
        }
    }
    data = {
       '__postdata': json.dumps(param)
    }
    headers = {'Content-Type': 'application/json'}
    url = 'http://192.168.4.108:93/api.cc?' + urlencode(params)
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None

if __name__ == '__main__':
    data = get_page()
    for item in data['data']['datasource']:
        print(item)





