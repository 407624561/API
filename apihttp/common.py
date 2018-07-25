# -*- coding:utf-8 -*-
class CommonMethod:
    # 将json中的变量替换掉
    #date  json数据
    #change map 传的  key：json中的值，value：要替换的值
    def changeDate(self,data, change):
        for key in change:
            dataNew = data.replace(key, change[key])
            data = dataNew
        return dataNew