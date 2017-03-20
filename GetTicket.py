# -*- coding: utf-8 -*-
import sys
from bs4 import BeautifulSoup
import re
import urllib2
import requests

class Ticket:
    def GetTicketInfo(Arr,Des,Date):
        baseUrl = "http://flights.ctrip.com/booking/%s-%s-day-1.html?ddate1=2017-04-13"%(Arr,Des)
        req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                        'Accept':'text/html;q=0.9,*/*;q=0.8',
                        'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                        'Accept-Encoding':'gzip',
                        'Connection':'close',
                        'Referer':None
                        }
        req = urllib2.Request(baseUrl,None,req_header)
        resp = urllib2.urlopen(req)
        res = resp.read()
        soup = BeautifulSoup(res,"html.parser")
        flight_list = soup.find("div",{"id":"base_bd"})
        print soup
    GetTicketInfo('xmn','can',1)