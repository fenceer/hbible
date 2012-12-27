#coding:utf-8
'''
Created on Dec 27, 2012

@author: xen
微信接口
'''

import web

from modules import common
import hashlib

render = common.render('wechat')
db = web.config.db
rdb = web.config.redis
pipe = rdb.pipeline()
session = web.config._session
TOKEN = '3652htt'

class Query():
    '''
    POST(query)
    RETURN String
    '''
    def GET(self):
        data = web.input()
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr
        
        print 'signature:', signature
        print 'timestamp:', timestamp 
        print 'nonce:', nonce
        print 'echostr:', echostr 
        
        
        ll = []
        ll.append(timestamp)
        ll.append(TOKEN)
        ll.append(nonce)
        ll.sort()
        ss = hashlib.sha1(''.join(ll)).hexdigest()
        if ss == signature:
            return echostr
        else:
            return None
    
    def POST(self):
        data = web.input()
        print data
        
#        ss = data.query.split(' ')
#        if ss[1].find(':'):
#            ind = ss[1].split(':')
#            num = ind[1].split('-')
#            start = int(ind[0]) * 1000 + int(num[0])
#            end = int(ind[0]) * 1000 + int(num[1])
#        elif ss[1].find('/'):
#            ind = ss[1].split('/')
#            num = ind[1].split('-')
#            start = int(ind[0]) * 1000 + int(num[0])
#            end = int(ind[0]) * 1000 + int(num[1])
#        print start, end
#        
#        bb = db.GB.find({'book':ss[0], '$and':[
#                                           {'index':{'$gte':start}},
#                                           {'index':{'$lte':end}}]})
        
        return render.text(bb='bb')
