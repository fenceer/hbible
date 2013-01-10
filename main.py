#!/usr/bin/env python
# coding:utf-8
'''
Created on Sep 21, 2012

@author: xen
hbible
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import web
import pymongo
import urls

# 配置体系，整个web的所有资源全部在这里配置
# web.config.debug = False
web.config.session_parameters.timeout = 6000  # 100分钟
web.config.mongo = pymongo.Connection('192.168.1.131', 27017)
web.config.mongo.admin.authenticate('fenceer', 'fenceer')
web.config.db = web.config.mongo['hbible']

app = web.application(urls.urls, globals())

# store session for debug mode
if web.config.get('_session') is None:
    web.config._session = web.session.Session(app, web.session.DiskStore('sessions'), {'count': 0})
#    web.config._session = web.session.Session(app, rediswebpy.RedisStore(), initializer={'count': 0})

import appinit
app.add_processor(appinit.my_processor)
# app.internalerror = appinit.internalerror
# app.notfound = appinit.notfound

if __name__ == "__main__":
#    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app.run()
