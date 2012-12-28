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
rdb = web.config.redis
pipe = rdb.pipeline()
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
        text = model.wechat.quick(wmsg)
        if not text: 
            text = model.word.checkChapter(content)
            if text is None:
                source = db.source.find_one({'key':content})
                if source:
                    text = source['text'] 
                else:
                    text = msgDict[10003] + msgDict[10001]
                    db.doubt.insert(wmsg)
                    
        wmsg['CreateTime'] = time.time()
        wmsg['MsgType'] = 'text'
        wmsg['Content'] = text if text else msgDict[10003] + msgDict[10001]
        return render.text(wmsg=wmsg)
