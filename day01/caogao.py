# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 15:30:25 2018

@author: lenovo
"""
msg={"地址":"北京海淀区xxxx","手机号码":"123456","寄信人":"agfag" }
print(msg["地址"])
print(msg["手机号码"])
print(msg["寄信人"])





liuchen={"姓名":"刘晨","身高":"1.5米","性别":"男","年龄":"23" }
print(liuchen["姓名"])
print(liuchen["身高"])
print(liuchen["性别"])
print(liuchen["年龄"])
xzhq={'name':'薛之谦',
     'song':['特别辣','演员','暧昧','认真的雪'],
     '昵称':'xiao薛',
     '认识过女朋友':'2,1,3,8,-1'  }
songs=xzhq['songs']
print(songs)
print("歌曲总数:"+str(len(songs)))
print(max(xzhq['认识过女朋友']))
wd=['20','30','25','18','20']
qk=['阴','晴','小雨','阴','阴']
print(wd)
print(qk)
w={'wd':['20','30','25','18','20'],
   'qk':['阴','晴','小雨','阴','阴'],
    'day':['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期天']}
day=w['day']
print('today is :'+day[5])
print(max(w['wd']))
