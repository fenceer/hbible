#coding:utf-8
'''
Created on Oct 25, 2012

@author: xen
'''

import web
import time

from modules import util

db = web.config.db
session = web.config._session
cookie_expires = 24 * 60 * 60

def login(user):
    session.uid = user['_id']
    session.role = user['role']
    session.username = user['username']
    web.setcookie('al', util.int_hex(user['_id']), cookie_expires)
    db.admin.update({'_id':user['_id']}, {'$set':{'ltime':time.time()}})


    
