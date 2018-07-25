# -*- coding:utf-8 -*-
import requests
class HttpApi:
    def __init__(self):
        self.headers ={'content-type': 'application/json'}
    def send_get(self,url,data):
        res = requests.get(url=url, params=data)
        return res.json()
    def send_post(self,url,data):
        res = requests.post(url=url, data=data,headers=self.headers)
        return res.json()

