# coding:utf-8
'''
Created on Dec 27, 2012

@author: xen
微信接口
'''

import web
import time

import model
import config
from modules import common

render = common.render('wechat')
db = web.config.db
msgDict = config.msgDict
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
        wmsg = model.wechat.getMsgObj(web.ctx.data)
        db.wmsg.insert(wmsg)
        
        content = wmsg['Content']
        if content == 'news':
            wmsg['Articles'] = ['a', 'b', '1', '2', '3']
            return render.news(wmsg=wmsg)
        if content == 'test':
            return render.test(wmsg=wmsg)
        
        text = model.wechat.quick(wmsg)
        if not text: 
            chapter = model.word.checkChapter(content)
            '''如果查不到经文就搜索数据库和wiki'''
            text = chapter if chapter else model.wechat.search(content)
            if not text:
                text = msgDict[10003] + msgDict[10001]
                db.doubt.insert(wmsg)
        
        '''如果太长则要分割'''
        if len(text) > 700:
            cache = {
                     '_id':wmsg['FromUserName'],
                     'text':text[700:],
                     'ctime':time.time()
                     }
            db.cache.save(cache)
            text = text[:700] + msgDict[10007]

        wmsg['CreateTime'] = time.time()
        wmsg['MsgType'] = 'text'
        wmsg['Content'] = text if text else msgDict[10003] + msgDict[10001]
        return render.text(wmsg=wmsg)
