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
                    text = "微圣经努力学习中/奋斗\n回复H查看使用帮助" 
                    db.doubt.insert(wmsg)
                    
        wmsg['CreateTime'] = time.time()
        wmsg['MsgType'] = 'text'
        wmsg['Content'] = text if text else "微圣经努力学习中/奋斗\n\n回复H查看使用帮助"
        return render.text(wmsg=wmsg)
