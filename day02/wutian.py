# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 14:59:17 2018

@author: lenovo
"""
print("欢迎使用全球天气app")
print("查看某市连续5天天气情况")
print("1.查看当前城市天气，2.查看某市午时天气，3.查看其它城市天气")
menno=input("请输入菜单：")
if menno=='1':
    print("1.查看当前城市天气")
    import urllib.request as r
    city_pinyin=input("请输入城市拼音:")
    address='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
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
    address='http://api.openweathermap.org/data/2.5/forecast?q={}&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
    info1=r.urlopen(address.format(city_pinyin)) .read().decode('utf-8','ignore')


    import json
    
    data1=json.loads(info1)
    print('-----------------以下为查询结果----------------')
    print('--时间（3小时段)-----天气情况-----温度------气压')
    for i in range(37):
        
        
        print(data1["list"][i]["dt_txt"],'  ',data1["list"][i]['weather'][0]['description'],'    ',data1["list"][i]["main"]["temp"],'    ',data1["list"][2]["main"]["pressure"])
        
        
    
if menno=='3':
    
    print('3.查看其它城市天气')
   
sfar=input("是否退出")
if sfar=='1':
    print('---------------')
    print('   是   ')
    print('---------------')
if sfar=='2':
    print('---------------')
    print('  否  ')
    print('---------------')
    
sfer=input("是否保存用户信息")
if sfer=='1':
    print('---------------')
    print('用户信息保存成功')
    print('---------------')
if sfer=='2':
    print('---------------')
    print('  该用户已注销  ')
    print('---------------')
