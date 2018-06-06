# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 14:30:46 2018

@author: lenovo
"""

import urllib.request as r

url = "http://www.gaokaopai.com/university-ajaxGetMajor.html "

xtype = [1,2]
xcity = [11,12,13,14,15,21,22,23,31,32,33,34,35,36,37,41,42,43,44,45,46,50,51,52,53,54,61,62,63,64,65]
xue = open ('./all_school.txt','r',encoding = "utf-8").readlines()

xid =[]
for i in xue:
    xid.append(i[:-5].split("-")[2].split(".")[0])
params = []
#f = open('./urls2.txt','a')    
for city in xcity:  
    for o in xid: 
        par = 'id={}&type=1&city={}&state=1'.format(o,city)
        #f.write(par+'\n')
        params.append(par)
for city in xcity:  
    for o in xid: 
        par = 'id={}&type=2&city={}&state=1'.format(o,city)
        #f.write(par+'\n')
        params.append(par)

#redis 保存状态       
#params = 'id={}&type={}&city={}&state={}'.format().encode()  .encode()是编码的意思
headers = {"X-Requested-With":"XMLHttpRequest",
           "connection":"Keep-alive",
           "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
           }
for p in params[0:10]:
    req = r.Request(url,p.encode(),headers)
    #网络异常处理 1 自己的网络问题  2 对方的网络问题 
    try:
        data = r.urlopen(req).read().decode('utf-8','ignore')
        print(len(data))
        open('./gaokaopai5.txt','a',encoding = 'utf -8').write(data+"\n")  
    except Exception:
        print(params + "数据下载失败")