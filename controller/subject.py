# coding:utf-8
'''
Created on 2013-1-12

@author: fenceer
wiki 编辑条目
'''

import web

import config
from modules import common, base
import time
import model
import urllib

render = common.render('subject')
db = web.config.db
msgDict = config.msgDict
session = web.config._session

class Edit:
    def GET(self):
        data = web.input()
        sbjId = data.get('sbjId', 0)
        subject = db.subject.find_one({'_id':int(sbjId)})
        if subject is None:
            subject = {}
            subject['title'] = data.get('ss', '')
        
        return render.edit(subject=subject)
        
    def POST(self):
        data = web.input()
        desc = {
                'ip':web.ctx.ip,
                'uid':session.get('uid'),
                'text':data.text,
                'ctime':time.time()
                }
        subject = db.subject.find_one({'title':data.title})
        if subject:
            db.subject.update({'_id':subject['_id']}, {'$push':{'history':subject['desc']}})
            db.subject.update({'_id':subject['_id']}, {'$set':{'desc':desc}})
        else:
            subject = {
                    '_id':base.getLastID('subject'),
                    'title':data.title,
                    'desc':desc,
                    'history':[]
                 }
            db.subject.insert(subject)
        
        raise  web.seeother('/search?ss=' + urllib.quote(data.title.encode('utf-8')))

class History:
    def GET(self):
        pass
        return  render.histiry()

class Search:
    def GET(self):
        data = web.input()
        ss = data.get('ss')
        if ss:
            ss = ss.strip()
            chapter = model.word.checkChapter(ss)
            if chapter:
                subject = chapter.replace('\n', '<br/>') 
            else:
                subject = db.subject.find_one({'title':ss})
            return render.subject(subject=subject)
        else:
            return render.search()
