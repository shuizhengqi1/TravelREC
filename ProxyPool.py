import sys
import requests
from bs4 import BeautifulSoup
import urllib2

class Pool:
    def KuaiGetProxy(url):

        req = urllib2.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',)
        response =urllib2.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html,'html.parser')
        print soup

    KuaiGetProxy('http://www.kuaidaili.com/proxylist/4/')