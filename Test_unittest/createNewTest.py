# -*- coding:utf-8 -*-
import unittest
import json
import requests
from apihttp.common import *
from requests1.LicesenCommon import *
class CreateTest(unittest.TestCase):
    def setUp(self):
        pass
    #正常新增lincesen
    def test_addOk(self):
        #获取接口所需数据
        id="800"
        userid="1000"
        url="http://47.92.88.246:8999/it-license/it/license/create"
        createFile = open("..\data\create.json")
        headers = {'content-type': 'application/json'}
        loadData=json.load(createFile)
        data=json.dumps(loadData)
        #对数据进行转换
        dict={}
        dict["ID"]=id
        dict["usersID"]=userid
        common=CommonMethod()
        changedData=common.changeDate(data,dict)
        print(changedData)
        res=requests.post(url=url,data=changedData,headers=headers)
        print(res.text)
        dateID=res.json()['result']
        self.assertEqual(res.json()['errMessage'],"success")
        #self.assertEqual(res.json()['errCode'],0)
        #数据清理
        # licesen=LicesenMethod()
        # licesen.deleteLicesen(id,userid,dateID)
    #企业id为空测试
    def test_addIdIsNull(self):
        #获取接口所需数据
        id=""
        userid="1000"
        url="http://47.92.88.246:8999/it-license/it/license/create"
        createFile = open("..\data\create.json")
        headers = {'content-type': 'application/json'}
        loadData=json.load(createFile)
        data=json.dumps(loadData)
        #对数据进行转换
        dict={}
        dict["ID"]=id
        dict["usersID"]=userid
        common=CommonMethod()
        changedData=common.changeDate(data,dict)
        print(changedData)
        res=requests.post(url=url,data=changedData,headers=headers)
        print(res.text)
        #dateID=res.json()['result']
        self.assertEqual(res.json()['errCode'], 301140002)
        #数据清理
        #licesen=LicesenMethod()
        #licesen.deleteLicesen(id,userid,dateID)
        # 企业id为空测试
    def test_addUseridIsNull(self):
        #获取接口所需数据
        id="800"
        userid=""
        url="http://47.92.88.246:8999/it-license/it/license/create"
        createFile = open("..\data\create.json")
        headers = {'content-type': 'application/json'}
        loadData=json.load(createFile)
        data=json.dumps(loadData)
        #对数据进行转换
        dict={}
        dict["ID"]=id
        dict["usersID"]=userid
        common=CommonMethod()
        changedData=common.changeDate(data,dict)
        print(changedData)
        res=requests.post(url=url,data=changedData,headers=headers)
        print(res.text)
        #dateID=res.json()['result']
        self.assertEqual(res.json()['errCode'], 301140002)
        #数据清理
        #licesen=LicesenMethod()
        #licesen.deleteLicesen(id,userid,dateID)
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()