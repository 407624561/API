# /usr/bin/env python
# -*- coding: utf-8 -*
import requests
class asd:
    def aa(self,url,data):
        ww=requests.get(url=url,params=data)
        return ww.text
    def bb(self,url,data,headers):
        mm=requests.post(url=url,data=data,headers=headers)
        return mm.text
if __name__ == '__main__':
    url="https://report.stage.yunshanmeicai.com/preview-pc.html#/page/852"
    data={"preview":"852","type":"2"}
    headers={"Content-Type":"application/json"}
    efd=asd()
    print efd.bb(url,data,headers)