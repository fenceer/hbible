#coding:utf-8
'''
Created on 2012-7-21

@author: Xen
'''
import re
import web
import json

import config
db = web.config.db

errorDesc = config.errorDesc

def getLastID(name):
    #获取某个集合的自增ID
    ids = db['ids'].find_and_modify(query={'name':name}, update={'$inc':{'id':1}})
    if ids:
        return ids['id']
    else:
        db['ids'].insert({'name':name, 'id':100000})
        return db['ids'].find_and_modify(query={'name':name}, update={'$inc':{'id':1}})['id']
    
def importName(modulename, name):
    try:
        module = __import__(modulename, fromlist=[name])
    except ImportError:
        return None
    return getattr(module, name)

def rtjson(code=1, **args):
    '''return json'''
    if code == 1:
        args['status'] = 1
    else:
        args['status'] = 0
        args['error_code'] = code
        args['msg'] = errorDesc.get(code)
        
    return json.dumps(args)

def rtjsonp(callback, **args):
    '''return jsonp'''
    #web.header('Access-Control-Allow-Origin', '*') 
    return callback + '(' + json.dumps(args) + ');'

def checkData(data, pattern):
    '''数据正则校验'''
    errorValue = []
    for key, regex in pattern.items():
        value = data.get(key)
        if value is None:
            errorValue.append((key, 'null'))
        
        if regex:
            match = re.match(regex, value.decode('utf8'))
            if match is None:
                errorValue.append((key, 'error'))
                
    return errorValue
