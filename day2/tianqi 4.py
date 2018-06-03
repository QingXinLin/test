# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 11:12:28 2018

@author: lenovo
"""
print("欢迎使用全球天气app")
print("查看某市连续5天天气情况")
print("1.查看当前城市天气，2.查看某市午时天气，3.保存当前城市")
menno=input("请输入菜单：")
if menno=='1':
    print("1.查看当前城市天气")
    import urllib.request as r
    city_pinyin=input("请输入城市拼音:")
    address='http://api.openweathermap.org/data/2.5/weather?q=nanchong&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
    info=r.urlopen(address.format(city_pinyin)) .read().decode('utf-8','ignore')


    import json
    data=json.loads(info)
    print('当日最高温度:'+str(data['main']['temp_max']))
    print('天气情况:'+str(data['weather'][0]['description']))
    print('气压：'+str(data['main']['pressure']))
if menno=='2':
    print("2.查看某市连续五天天气")
    import urllib.request as r
    city_pinyin=input("请输入城市拼音:")
    address='http://api.openweathermap.org/data/2.5/forecast?q=nanchong,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
    info1=r.urlopen(address.format(city_pinyin)) .read().decode('utf-8','ignore')


    import json
    data1=json.loads(info1)
    print("6月3日的天气为:"+str(data1["list"][2]['weather'][0]['description'])+";最高温度为:"+str(data1["list"][2]["main"]["temp_max"])+";最低温度为:"+str(data1["list"][2]["main"]["temp_min"])+";气压为:"+str(data1["list"][2]["main"]["pressure"]))
    print("6月4日的天气为:"+str(data1["list"][10]['weather'][0]['description'])+";最高温度为:"+str(data1["list"][8]["main"]["temp_max"])+";最低温度为:"+str(data1["list"][10]["main"]["temp_min"])+";气压为:"+str(data1["list"][10]["main"]["pressure"]))
    print("6月5日的天气为:"+str(data1["list"][18]['weather'][0]['description'])+";最高温度为:"+str(data1["list"][18]["main"]["temp"])+";最低温度为:"+str(data1["list"][18]["main"]["temp_min"])+";气压为:"+str(data1["list"][18]["main"]["pressure"]))
    print("6月6日的天气为:"+str(data1["list"][26]['weather'][0]['description'])+";最高温度为:"+str(data1["list"][26]["main"]["temp"])+";最低温度为:"+str(data1["list"][26]["main"]["temp_min"])+";气压为:"+str(data1["list"][26]["main"]["pressure"]))
    print("6月7日的天气为:"+str(data1["list"][34]['weather'][0]['description'])+";最高温度为:"+str(data1["list"][34]["main"]["temp"])+";最低温度为:"+str(data1["list"][34]["main"]["temp_min"])+";气压为:"+str(data1["list"][34]["main"]["pressure"]))

if menno=='3':
    print('3.保存当前城市') 
