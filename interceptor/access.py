#coding:utf-8
'''
Created on 2012-9-29

@author: fenceer
'''

'''
class Interceptor:
    def intercept(self, nextIntercept):
        if string:
            return string
        if json
            return json
        if ok
            return nextIntercept()
'''
import  web
import  model
from modules import  util, base

db = web.config.db
session = web.config._session

'''
权限认证
'''
class CheckAuthority:
    def intercept(self, nextIntercept):
        if session.get('uid') is None:
            environ = web.ctx.environ
            if environ.get('HTTP_X_REQUESTED_WITH') is None:
                raise web.seeother('/login?h=' + web.ctx.path)
            else:
                return base.rtjson(20001, redict=web.ctx.path)
        else:
            return nextIntercept()
    
'''
自动登录
'''
class AutoLogin:
    def intercept(self, nextIntercept):
#        自动登录  所有非ajax请求过来 都要能够自动登录
#
#        has uid?
#            yes - ->next
#                
#            no - ->cookie is  AutoLogin?
#                    yes - ->get cookie sessionid - ->login
#                    no - ->next

        environ = web.ctx.environ
        if environ.get('HTTP_X_REQUESTED_WITH') is None:
            if session.get('uid') is None and web.cookies().get('al') :
                uid = util.hex_int(web.cookies().get('al'))
                user = db.admin.find_one({'_id':uid})
                if user:
                    model.user.login(user)
                else:
                    raise web.seeother('/login')
            
        return nextIntercept()


