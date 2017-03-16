import redis

class Redis:
    r = redis.Redis(host='localhost',port=6379,db=0)

    def setValue(self,key,value):
        self.r.set(key,value)

    def getValue(self,key):
        self.r.get(key)