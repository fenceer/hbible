# coding:utf-8
'''
Created on 2012-7-15

@author: Xen
'''

pre = 'controller.'
INTERCEPTOR = 'interceptor:'
local_interceptor = []

urls = [
        '/tmp'                  , pre + 'test.Temp',
        '/test'                 , pre + 'test.Test',
        '/init'                 , pre + 'test.Init',
        '/apidoc'               , pre + 'test.Apidoc',
        '/apidoc/(\w+)'         , pre + 'test.Apidoc',
        '/wechat/bb'            , pre + 'wechat.Query',
        '/wechat'               , pre + 'wechat.Query',
        
        '/code'                 , pre + 'verify.CodeNum'
]
