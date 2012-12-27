#coding:utf-8
'''
Created on 2012-9-29

@author: fenceer
'''
import base

class Chain:
    def __init__(self, handler, interceptors=[]):
        self.interceptors = interceptors
        self.handler = handler
        
    def do(self):
        self.interceptors.append(self.handler)
        self.interceptors.reverse()
        return self.next()
        
    def next(self):
        if len(self.interceptors) == 1:
            return self.handler()
        else:
            interceptor = self.interceptors.pop()
            idx = interceptor.find('.')
            modulename = 'interceptor.' + interceptor[:idx]
            name = interceptor[idx + 1:]
            HandlerClass = base.importName(modulename, name)
            hanlder = HandlerClass()
            return hanlder.intercept(self.next)
        

        
