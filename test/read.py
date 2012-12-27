#coding:utf-8
'''
Created on Dec 27, 2012

@author: xen
'''
import redis
import pymongo
import time

ts = time.time()
mdb = pymongo.Connection('192.168.1.131', 27017)
mdb.admin.authenticate('fenceer', 'fenceer')
db = mdb['hbible']

rdb = redis.StrictRedis(host='192.168.1.131', port=6379, db=3)
pipe = rdb.pipeline()

fl = open("../resource/bible/GB.txt")
ss = ''.split()
c = 0
bbs = []
for line in fl:
    ll = line.split(' ')
    Chapter = ll[1].split(':')
    index = int(Chapter[0]) * 1000 + int(Chapter[1])
    bb = {
        'book':ll[0],
        'index':index,
        'text':ll[2]
        }
    bbs.append(bb)

print len(bbs)
db.GB.insert(bbs)

print time.time() - ts
