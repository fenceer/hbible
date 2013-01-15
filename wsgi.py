#!/usr/bin/env python
# coding:utf-8
'''
Created on Sep 21, 2012

@author: xen
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import web
import urls
import pymongo

web.config.debug = False
# web.config.session_parameters.timeout = 6000 #100 Minutes
web.config.mongo = pymongo.Connection('10.0.29.251', 25891)
web.config.mongo.admin.authenticate('dae0b0b5-c5b7-4d41-baff-140bd47deba2', '51d36d8a-3025-49b9-95b8-755cc41be01b')
web.config.db = web.config.mongo['db']

app = web.application(urls.urls, globals())
web.config._session = web.session.Session(app, web.session.DiskStore('sessions'), {'count': 0})
# web.config._session = web.session.Session(app, rediswebpy.RedisStore(), initializer={'count': 0})

import appinit
app.add_processor(appinit.my_processor)
# app.internalerror = appinit.internalerror
# app.notfound = appinit.notfound

application = app = app.wsgifunc()

if __name__ == "__main__":
    web.wsgi.runwsgi = lambda func, addr = None: web.wsgi.runfcgi(func, addr)
    app.run()
