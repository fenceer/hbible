# coding:utf-8
'''
Created on Dec 27, 2012

@author: xen
微信接口
'''

import web
import time

import model
from modules import common

render = common.render('wechat')
db = web.config.db
rdb = web.config.redis
pipe = rdb.pipeline()
session = web.config._session


class Query():
    '''
    POST(query)
    RETURN String
    '''
    def GET(self):
        data = web.input()
        if model.wechat.checkSignature(data):
            return data.echostr
        else:
            return None
    
    def POST(self):
        data = web.input()
        if not model.wechat.checkSignature(data):return None
        
        print 'xdate', web.ctx.data
        xmsg = model.wechat.getMsgObj(web.ctx.data)
        content = xmsg['Content'].strip()
        if content == 'Hello2BizUser':
            text = '''
                                                    耶稣爱你~
                                                    回复书卷名、章、节查询圣经                                
                                                    例如：“约翰福音3:16”或者 “创世记1/1-4”
                                                    书卷名支持中英文简写
                '''
        elif content in ['H', 'h']:
            text = '''
                                                    耶稣爱你~
                                                    回复书卷名、章、节查询圣经                                
                                                    例如：“约翰福音3:16”或者 “创世记1/1-4”
                                                    书卷名支持中英文简写
                ''' 
        elif content =='梁佳':
            text = '''
                                                    耶稣爱你，我也爱你~
                ''' 
        else: 
            text = model.word.checkChapter(content)
#        ss = xmsg['Content'].split(' ')
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
#        
#        if start > end:
#            start = end
#            end = start
#        
#        sn = model.word.getBook(ss[0])
#        bb = db.GB.find({'book':sn, '$and':[
#                                           {'index':{'$gte':start}},
#                                           {'index':{'$lte':end}}]})
#        text = ''
#        for b in list(bb):
#            text += b['text']
        
        
        xmsg['CreateTime'] = time.time()
        xmsg['MsgType'] = 'text'
        xmsg['Content'] = text if text else "^o^"
        return render.text(xmsg=xmsg)
