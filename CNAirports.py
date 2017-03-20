# coding=utf-8
from bs4 import BeautifulSoup
import requests
import urllib2
import sys
import re

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
            NoSpace = re.sub("\n\n\n","",item).encode("utf-8")
            print ("这是第%d"%i+"条数据，内容为\n"+NoSpace)
            huiche = NoSpace.split('\n')
            for hcitem in huiche:
                print hcitem