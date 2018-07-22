# /usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
from apihttp.common import *
from apihttp.HttpApi1 import *
from requests1.LicesenCommon import *
change = CommonMethod()
http=HttpApi()
liceseMethod=LicesenMethod()
class createTest(unittest.TestCase):
    def setUp(self):
        self.url='http://47.92.88.246:8999/it-license/it/license/create'
        createFile = open("..\data\create.json")
        self.jsonData = json.load(createFile)
        self.changeDate = {}
        self.id = '500'
        self.userId = '500'
        self.liceseID=None
    def testAddLicesen(self):
        self.headers = {'content-type': 'application/json'}
        self.changeDate["ID"]=self.id
        self.changeDate["usersId"]=self.userId
        data=change.changeDate(json.dumps(self.jsonData),self.changeDate)
        res = http.send_post(self.url, data)
        #print(res)
        self.liceseID = res['result']
        self.assertEqual(res['errMessage'],"success",'添加lincesen成功')

    # #企业id为空
    # def testAddisNull(self):
    #     self.changeDate["ID"]=''
    #     self.changeDate["usersId"]=self.userId
    #     data=change.changeDate(json.dumps(self.jsonData),self.changeDate)
    #     res= http.send_post(self.url,data)
    #    # print(res)
    #     self.assertEqual(res['errCode'],301140002,'测试失败')
    # #userId为空测试
    # def testAddUserIsNull(self):
    #     self.changeDate["ID"]=self.id
    #     self.changeDate["usersId"]=''
    #     data=change.changeDate(json.dumps(self.jsonData),self.changeDate)
    #     res = http.send_post(self.url, data)
    #     #print(res)
    #     self.assertEqual(res['errCode'], 301140002, '测试失败')
    def tearDown(self):
        print(self.liceseID)
        liceseMethod.deleteLicesen(self.id,self.userId,self.liceseID)

if __name__ == '__main__':
    unittest.main()
