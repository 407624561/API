# /usr/bin/env python
# -*- coding: utf-8 -*
from requests1.HttpApi import httpapi

if __name__ == '__main__':
    url = "http://v.juhe.cn/calendar/day"
    data = {"date": "2018-7-6", "key": "3fc2053b46fcafdaacd98165f31706d4"}
    headers = {'content-type': 'application/json'}
    http3 = httpapi()
    print http3.http_post(url, data,headers)
