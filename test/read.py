# coding:utf-8
'''
Created on Dec 27, 2012

@author: xen
'''
import pymongo
import time

ts = time.time()
mdb = pymongo.Connection('192.168.1.131', 27017)
mdb.admin.authenticate('fenceer', 'fenceer')
db = mdb['hbible']


fl = open("../resource/bible/GB2.txt")
ss = ''
c = 0
bbs = []
for line in fl:
    if line.startswith(' '):
        ss = line.split('（')[0].strip()
        print ss
        bbs.append(ss)
#    ll = line.split(' ')
#    Chapter = ll[1].split(':')
#    index = int(Chapter[0]) * 1000 + int(Chapter[1])
#    bb = {
#        'book':ll[0],
#        'index':index,
#        'text':ll[1] + ' ' + ll[2]
#        }
#    if ll[0] in bbs:
#        pass
#    else:
#        bbs.append(ll[0])

# print len(bbs)
# db.GB.insert(bbs)

print bbs
print time.time() - ts
