# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 16:36:45 2018

@author: lenovo
"""

city_pinyin=input("请输入城市拼音:")

address='http://api.openweathermap.org/data/2.5/weather?q=meishan&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'

print(address.format(city_pinyin))

print("欢迎使用全球天气app")
print("1.查看当前城市天气，2.查看其它城市天气，3.保存当前城市")
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
if menno=="2":
    print('2.查看其它城市天气')
if menno=='3':
    print('3.保存当前城市')    


