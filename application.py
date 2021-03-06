#!/usr/bin/env python
# coding:utf-8
'''
Created on Sep 21, 2012

@author: xen
'''
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

import web
import urls
import pymongo


web.config.debug = False
# web.config.session_parameters.timeout = 6000 #100 Minutes
web.config.mongo = pymongo.Connection(os.environ.get('OPENSHIFT_MONGODB_DB_HOST'), 27017)
web.config.mongo.admin.authenticate('admin', os.environ.get('OPENSHIFT_MONGODB_DB_PASSWORD'))
web.config.db = web.config.mongo['hbible']

app = web.application(urls.urls, globals())
web.config._session = web.session.Session(app, web.session.DiskStore('sessions'), {'count': 0})
# web.config._session = web.session.Session(app, rediswebpy.RedisStore(), initializer={'count': 0})

import appinit
app.add_processor(appinit.my_processor)
# app.internalerror = appinit.internalerror
# app.notfound = appinit.notfound



application = app.wsgifunc()

if __name__ == "__main__":
    web.wsgi.runwsgi = lambda func, addr = None: web.wsgi.runfcgi(func, addr)
    app.run()
