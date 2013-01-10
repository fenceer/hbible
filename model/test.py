#coding:utf-8
'''
Created on Dec 4, 2012

@author: xen
'''
import web


db = web.config.db
session = web.config._session


def getSession():
    print session.uid
    return session
