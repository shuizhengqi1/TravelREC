import redis
from XIECHENGParse import Ticket
class Redis:
    ticker = Ticket
    r = redis.Redis(host='localhost',port=6379,db=0)

    def setValue(self,key,value):
        self.r.set(key,value)

    def getValue(self,key):
        self.r.get(key)



    # print (r.get('sss'))