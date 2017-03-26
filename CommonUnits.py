# coding=utf-8
from bs4 import BeautifulSoup
import requests
import urllib2
import sys
import re
import redis

#获取机场列表
class CNList:
    list = []
    url = "http://www.fnetravel.com/airports-in-china-cn.html"
    req = urllib2.urlopen(url)
    resp = req.read();
    soup = BeautifulSoup(resp,"html.parser")
    for item in soup.find_all("table",{"class":"datatable"}):
        AirportCode = item.text
        pattern  =ur'\n\n\n[\u4e00-\u9fa5].+\n[A-Z]+\n[\u4e00-\u9fa5]+'
        repattern = re.compile(pattern)
        CodeGroup = repattern.findall(AirportCode)
        for i,item in enumerate(CodeGroup):
            SingleAirportList = re.sub("\n\n\n","",item).encode("utf-8").split('\n')
            list.append(SingleAirportList)

    def getAirportList(self):
        return self.list

class Redis:

    r = redis.Redis(host='localhost',port=6379,db=0)

    def setValue(self,key,value):
        self.r.set(key,value)

    def getValue(self,key):
        return self.r.get(key)
    #添加set内容
    def setZValue(self,set,member,score):
        self.r.zadd(set,score,member)