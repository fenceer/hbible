# coding:utf-8
'''
Created on 2013-1-10

@author: fenceer
'''

from modules import common

render = common.render('home')


class Index:
    def GET(self):
        pass 
        return render.index()
        
