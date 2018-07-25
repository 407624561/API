# -*- coding:utf-8 -*-
import unittest
# import createNewTest
from Test_unittest.createNewTest import *
import HTMLTestRunner
if __name__ == '__main__':
    suit=unittest.TestSuite()
    suit.addTest(CreateTest("test_addOk"))
    suit.addTest(CreateTest("test_addIdIsNull"))
    suit.addTest(CreateTest("test_addUseridIsNull"))
    # runner=unittest.TextTestRunner()
    # runner.run(suit)
    file = open("../report/testReport.html",'wb')
    runner=HTMLTestRunner.HTMLTestRunner(file,title=u"接口测试",description=u"新增lincese用例执行情况说明")
    runner.run(suit)
#删除的接口 unittest 写测试用例
#生成测试报告
