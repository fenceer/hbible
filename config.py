#coding:utf-8
'''
Created on Nov 29, 2012

@author: xen
'''

data = {}
mddType = ['古镇', '温泉', '滑雪', '都市', '名胜', '其他']
data['img_domain'] = 'http://kapian.b0.upaiyun.com'
data['domain'] = 'http://back.zobei.com:8080'
data['mddType'] = mddType


errorDesc = {
             10001:'system error',
             10010:'value error',
             10011:'mdb error',
             10012:'rdb error',
             10013:'youpai error',
             
             10404:'not found',
             
             #user
             20001:'not login',
             20010:'invalid email or password',
    
    }
