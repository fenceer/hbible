# coding:utf-8
'''
Created on Oct 24, 2012

@author: xen
'''

import os
import web
from web import utils

import urls
from modules import common, base
import model

db = web.config.db
render = common.render('test')
session = web.config._session

class Temp:
    '''
    GET()
    '''
    def GET(self):
        return os.sys.path

class Test:
    '''
    测试类
    GET(id)
        return render.test(user,ss)
    POST(username,pwd)
        return json(user)
    '''
    def GET(self):
        data = web.input()
        user = db.test.find_one({'_id':int(data.get('id', 0))})
        if user is None:
            raise web.notfound('the user is not found')
        return render.test(user=user, ss=model.test.getSession())

    def POST(self):
        data = web.input()
        user = {
              '_id':base.getLastID('test'),
              'username':data.username,
              'pwd':data.pwd
              }
        db.test.insert(user)
        return base.rtjson(user=user)
    def hello(self):
        return '456'

class Apidoc:
    def GET(self, ctrl=None):
        apidoc = []
        controllers = []
        for f in os.listdir(os.path.split(__file__)[0]):
            module_name, ext = os.path.splitext(f)
            if not module_name.startswith('__') and ext == '.py':
                controllers.append(module_name)
        ctrl = 'controller.' + ctrl if ctrl in controllers else None
        
        for router in list(utils.group(urls.urls, 2)):
            url = router[0]
            controller = router[1]
            dot = controller.rfind('.')
            modulename = controller[:dot]
            name = controller[dot + 1:]
            
            if ctrl and ctrl != modulename:continue
            controlClass = base.importName(modulename, name)
            doc = controlClass.__doc__
            api = {
                   'url':url,
                   'controller':controller,
                   'doc':''
                   }
            if doc:
                docs = doc.split('\n')
                method = ''
                for d in docs:
                    d = d.strip()
                    if d.startswith('GET'):
                        method = 'get'
                        api['getargs'] = d[3:]
                        api['getdoc'] = ''
                    elif d.startswith('POST'):
                        method = 'post'
                        api['postargs'] = d[4:]
                        api['postdoc'] = ''
                    elif d != '':
                        api[method + 'doc'] += d + '<br/>'
            apidoc.append(api)
        return render.apidoc(apidoc=apidoc, controllers=controllers, ctrl=ctrl[ctrl.find('.') + 1:] if ctrl else None)

class Init:
    '''
    POST(a)
    RETURN json()
    '''
    def POST(self):
        print 'start'
        fl = open("resource/bible/GB.txt")
        bbs = []
        for line in fl:
            ll = line.split(' ')
            Chapter = ll[1].split(':')
            index = int(Chapter[0]) * 1000 + int(Chapter[1])
            bb = {
                'book':ll[0],
                'index':index,
                'text':ll[1] + ' ' + ll[2]
                }
            bbs.append(bb)
        db.GB.insert(bbs)
        print 'end'
        return base.rtjson()
