from bs4 import BeautifulSoup
import requests
import urllib2
import sys


class CNList:
    list = []
    url = "http://www.fnetravel.com/airports-in-china-cn.html"
    req = urllib2.urlopen(url)
    resp = req.read();
    soup = BeautifulSoup(resp,"html.parser")
    for item in soup.find_all("table",{"class":"datatable"}):
        AirportCode = item.find("td",{'class':'center'})
        print AirportCode

