# -*- coding: utf-8 -*-
import sys
from bs4 import BeautifulSoup
import re
import urllib2
import requests
import chardet
import json
import time
import random
import string
from CommonUnits import Redis
reload(sys)
sys.setdefaultencoding('gb2312')

class Ticket:
    count =0
    errcount = 0
    #获取包含机票信息的dict
    def GetTicketInfo(self,Dep,Arr,Date):
        #baseUrl = "http://flights.ctrip.com/booking/%s-%s-day-1.html?ddate1=2017-04-13"%(Arr,Des)
        url = "http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1="+Dep+"&ACity1="+Arr+"&SearchType=S&DDate1=2017-"+Date+"&IsNearAirportRecommond=0&LogToken=5fce7bea0392403fa35c77255ee95382&rk=1.8219278893756763093732&CK=020BB483F657E6F1D86136E48C4BC7E1&r=0.32218029023851888860518"
        req_header = {'Accept-Encoding':'gzip, deflate, sdch',
                        'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
                        'Cache-Control':'max-age=0',
                        'Connection':'keep-alive',
                        'Content-Type':'application/x-www-form-urlencoded',
                        'charset':'utf-8',
                        'Cookie':'_abtest_userid=74a7e635-a939-4ac1-aaf5-d7d6f4bf158a; DomesticUserHostCity=XMN|%cf%c3%c3%c5; Union=SID=155952&AllianceID=4897&OUID=baidu81|index|||; Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; adscityen=Xiamen; traceExt=campaign=CHNbaidu81&adid=index; appFloatCnt=5; page_time=1489651420547%2C1489651460731%2C1489651471982%2C1489653783619%2C1489653810913%2C1489653813677%2C1489653837433%2C1489653841120%2C1489653848045%2C1489654391767%2C1489654411529%2C1489654420972%2C1489654430617%2C1489654441256%2C1489654454140%2C1490015888757%2C1490015893882%2C1490015902280%2C1490017713031%2C1490059924347%2C1490230385186%2C1490230390179%2C1490230655043%2C1490230802123%2C1490231202992; _RF1=463093010; _RGUID=47cf9558-ee6e-4011-baca-4f0d71cd4b90; _ga=GA1.2.453564941.1489651343; _jzqco=%7C%7C%7C%7C%7C1.483421984.1489651344210.1490230803860.1490231205026.1490230803860.1490231205026.0.0.0.27.27; __zpspc=9.6.1490230385.1490231205.5%231%7Cbaidu%7Ccpc%7Cbaidu81%7C%25E6%2590%25BA%25E7%25A8%258B%25E6%2597%2585%25E8%25A1%258C%25E7%25BD%2591%7C%23; MKT_Pagesource=PC; _bfi=p1%3D101027%26p2%3D101027%26v1%3D35%26v2%3D34; FD_SearchHistorty={"type":"S","data":"S%24%u6B66%u6C49%28WUH%29%24WUH%242017-04-12%24%u6D77%u53E3%28HAK%29%24HAK"}; _bfa=1.1489651333488.3fz6tg.1.1490230382884.1490231202024.7.36; _bfs=1.2',
                        'DNT':'1',
                        'Host':'flights.ctrip.com',
                        'If-Modified-Since':'Thu, 01 Jan 1970 00:00:00 GMT',
                        'Referer':'http://flights.ctrip.com/booking/WUH-HAK-day-1.html?DDate1=2017-04-12',
                        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
                        }
        req = requests.get(url)
        respjson = req.text.decode("GB2312")
        try:
                jsondict = json.loads(respjson, encoding='utf-8')
                return jsondict
        except Exception,e:
                print ("***********")
                print e
                print ("***********")
                return ;

    #根据dcit，解析其中包含的相关机票的信息
    def ParseDict(self,dict,set):
        self.count +=1
        try:
            fis = dict['fis']
            lp = dict['lp']
            for item in fis:
                arr = item['acn']
                arrairport = item['apbn']
                arraircode = item['acc']
                arrflightInc = item['alc']
                arrflighttime = item['at']
                dep = item['dcn']
                depairport = item['dpbn']
                depaircode = item['dcc']
                depflighttime = item['dt']
                fn = item['fn']
                price = item['lp']
                # print fn
                # print price
            print (u'  从 '+dep+u' 到 '+arr+u' 的 最低票价为 ')
            print (lp)
            self.Add(set,depaircode,arraircode,price)
        except Exception ,e:
            self.count +=1

    #将机票信息存储到redis中的set里，set名为输入的set，set里面的score为票价，member为出发地+目的地
    def Add(self,set,dep,arr,price):
        member = dep+arr
        score = price
        Redis().setZValue(set,score,member)
    #输入起始地与目的地，获取并存储机票信息的入口
    def GetLowTicketInfo(self,Idsalt,dep,arr,date,size):
         dict = self.GetTicketInfo(dep,arr,date)
         self.ParseDict(dict,Idsalt)
         if (self.count == size):
             print "共查询了到达%d个城市的航班，其中有%d个机场查询不到对应的航班信息"%(self.count,self.errcount)