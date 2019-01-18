# -*- coding: utf-8 -*-
'''
Created on 2016/7/19

@author: xiaoguan
'''
import urllib.request
import bs4,re
f=open(r'e:\programming\txt\text.txt','r')
line=f.readlines()
header={'authority':'derpiboo.ru','method':'GET','scheme':'https',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'accept-language':'zh-CN,zh;q=0.8',
        'cache-control':'max-age=0',
        'upgrade-insecure-requests':'1',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    
    # 头文件里的(含gzip的这句)accept-encoding:gzip, deflate, sdch, br不要
N=len(line)
for i in range(N):
    url=line[i]
    req=urllib.request.Request(url,headers=header)
    con=urllib.request.urlopen(req)
    script=con.read()
    script=script.decode('utf-8')        #用utf-8解码
                                         #写入txt一定要标明utf-8编码，否则默认是GKB
    #f=open(r'e:\programming\txt\textcon.txt','w',encoding='utf-8')
    #f.write(script)
    
    soup=bs4.BeautifulSoup(script)
    imgcontainer=soup.body.find('div',class_='image-show-container')
    imgurl=eval(imgcontainer['data-uris'])
    imgurl=imgurl.get('full')
    img_extension=imgurl.split('.')
    img_extension=img_extension[-1]
    con=urllib.request.urlopen('https:'+imgurl)
    content='e:\\programming\\txt\\'+str(i)+'.'+img_extension
    
    f=open(content,'wb')
    f.write(con.read())
    f.close()
    print(imgurl)

