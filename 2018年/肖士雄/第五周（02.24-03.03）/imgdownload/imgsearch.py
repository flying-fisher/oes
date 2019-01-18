#coding=utf-8
'''
Created on 2018/1/31

@author: xiaoguan
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib2
import re
import sys,os
import time

class imgsearch(object):
    def __init__(self):
        self.driver = webdriver.PhantomJS()    #加载浏览器
    
    def openweb(self,str):
        try:
            self.url = str
            self.web = self.driver.get(self.url)   #尝试打开网页
            time.sleep(2)               
        except Exception as e:
            print(e)
        else:
            print('Successfully opened...')
    
    def search(self,str):
        self.keys = str
        inputelem = self.driver.find_element_by_id('kw')      #模拟输入关键字查询
        inputelem.send_keys(self.keys)
        inputelem.send_keys(Keys.RETURN)
        time.sleep(3)
        content = self.driver.page_source
        self.imgelem = self.driver.find_elements_by_class_name('main_img')  #通过class_name定位图片元素
        self.count = len(self.imgelem)
        print('Totally found %d images...' %(self.count))
        
    
    def download(self,address):
        self.imgurl = []
        self.img_extension = []
        for i in range(self.count):
            url = self.imgelem[i].get_attribute('data-imgurl')
            extension = url.split('.')               #获取图片格式
            extension = extension[-1]
            self.img_extension.append(extension)
            self.imgurl.append(url)
        for i in range(self.count):
            while True:                     #依次下载图片，如果超时则重新下载
                try:
                    file = address + 'img_' + str(i) + '.' + self.img_extension[i]
                    con = urllib2.urlopen(self.imgurl[i],timeout = 5)
                    f = open(file,'wb')
                    f.write(con.read())
                    f.close()
                    time.sleep(2)
                except Exception as e:
                    print(e)
                else:
                    pass
                    #print(file,self.imgurl[i])
                if os.path.getsize(file) > 0:
                    print(str(i+1) + '/' + str(self.count))
                    break
    
    def close(self):
        self.close()
        



