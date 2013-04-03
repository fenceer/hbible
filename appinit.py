#coding:utf-8
'''
Created on Oct 24, 2012

@author: xen
'''
import re
import web

import urls
from modules.interceptorChain import Chain
from modules import common

# define hooks
def my_processor(handler): 
    web.header("Content-Type",'')
    path = web.ctx.path
    interceptors = urls.interceptors.get(path)
    if interceptors is None:
        for k in urls.interceptors:
            if  re.match('^' + k + '$', path):
                interceptors = urls.interceptors[k]
    
    if interceptors is None:
        raise web.notfound()
    else:
        chain = Chain(handler, interceptors[:])
    result = chain.do()
    return result

def notfound():
    return web.notfound(common.render('framework').notfound())

def internalerror():
    return web.internalerror(common.render('framework').internalerror())

