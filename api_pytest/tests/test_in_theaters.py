#!/usr/bin/python
# -*- coding: utf-8 -*-
import pytest
import requests
import yaml

import json, urllib
from urllib import parse
from urllib import request



from utils.commlib import get_test_data

#导入读取测试数据的函数     


#调用get_test_data函数，同时赋值给变量cases，parameters
cases,parameters=get_test_data("D:\\python20190819\\api_pytest\\data\\test_in_theaters.yaml")

# #list() 方法用于将元组转换为列表。
list_params=list(parameters)
print(list_params)
#print(list_params[0][1]['http']["method"])
#print(list_params[0][1]['http']["params"])

#使用requests库请求数据
class TestInTheaters(object):
    

    @pytest.mark.parametrize("case,http,expected",list_params,ids=cases)
    #参数化，引用列表list_params中的参数
    #参数ids，这个值作为测试用例的名称将打印到测试结果中
    def test_in_theaters(self,env,case,http,expected):
        #直接传入env获取host
 
        #host = "http://web.juhe.cn:8080"
        
        r = requests.request(list_params[0][1]["method"],
                             url=env['host']['api'] + list_params[0][1]["path"],
                             params=list_params[0][1]["params"],
                             headers=list_params[0][1]["headers"])
        res = r.json()
        #解析返回的json数据，转换为列表或字典格式
        print(r.status_code)
        print(res)
        #assert res["date"] == 20200909
        assert res['name'] =="白羊座"
        assert res['name'] ==expected['response']['name']
#         #assert res['date'] ==expected['response']['date']
   
 
 
 


        #使用urllib库请求数据

        # m="GET"
        # url = "http://web.juhe.cn:8080/constellation/getAll"
        # params = {
        # "key" : "66377bf6f486191b6e316349a72cde09",
        # "consName" : "白羊座", 
        # "type" : "today" 
        # }

        # params = parse.urlencode(params)
        # #将params转换为url能识别的字符串格式（requests库相比urllib会自动转换）
        # if m =="GET":
        #     f = request.urlopen("%s?%s" % (url, params))
        # else:
        #     f = request.urlopen(url, params)
 
        # content = f.read()
        # #读取返回的数据并赋值给content
        # res = json.loads(content)
        # #把返回的字符串类型数据转换字典
        # print(type(res))
        # print(res['name'])
        #assert res['name'] == params['consName']
        #报错TypeError: string indices must be integers，原因是params已转为字符串类型数据
      

   