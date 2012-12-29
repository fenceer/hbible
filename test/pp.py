# coding:utf-8
'''
Created on 2012-12-29

@author: fenceer
'''

import urllib2
import urllib
import re
import cookielib
import hashlib
import json
'''
微信公共平台API
'''
class WeiXinAPI():
 
    def __init__(self):
        pass
 
    '''
    登录平台
    '''
    def login(self, account, password):
        self.account = account
        self.password = password
        self.cookies = self.get_login()
        return self.cookies
    '''
    进行md5加密，并输出16进制值
    '''
    def hex_md5hash(self, strr):
        return hashlib.md5(strr).hexdigest().upper()
 
    '''
    发送消息给指定ID的粉丝好友
    '''
    def postMessage(self, data, fans_id):
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        opener.addheaders = [('User-agent', 'Opera/9.23')]
        urllib2.install_opener(opener)
        url = 'http://mp.weixin.qq.com/cgi-bin/singlesend?t=ajax-response&lang=zh_CN'
 
        formdata = {
            'tofakeid':fans_id,
            'content':data,
            'error':'false',
            'type':1,
            'ajax':1
        }
        post_data = urllib.urlencode(formdata)
        send = urllib2.Request(url, post_data)
        send.add_header("Referer", "http://mp.weixin.qq.com")
        conn = urllib2.urlopen(send)
        if json.load(conn)['msg'] == 'ok':
            print 'ok'
 
    """
    获得粉丝好友的微信帐号
    """
    def getFansList(self, group_val=0):
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        opener.addheaders = [('User-agent', 'Opera/9.23')]
        urllib2.install_opener(opener)
        url = 'http://mp.weixin.qq.com/cgi-bin/contactmanagepage?t=wxm-friend&lang=zh_CN&pagesize=10000&pageidx=0&type=0&groupid=%d' % group_val
        formdata = {}
        post_data = urllib.urlencode(formdata)
        send = urllib2.Request(url, post_data)
        send.add_header("Referer", "http://mp.weixin.qq.com")
        conn = urllib2.urlopen(send)
        source_code = conn.read()
        json_str = re.findall(r'<script id="json-friendList" type="json/text">(.*?)</script>', source_code, re.S)[0].replace('\n', '')
        return json.loads(json_str)
 
    '''
        得到公共平台微信账户登录令牌
    '''
    def get_login(self):
        cookies = cookielib.MozillaCookieJar()
        url = 'http://mp.weixin.qq.com/cgi-bin/login?lang=zh_CN'
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))
        opener.addheaders = [('User-agent', 'Opera/9.23'), ('Referer', 'http://mp.weixin.qq.com')]
        urllib2.install_opener(opener)
        data = {
            'username':self.account,
            'pwd1':self.hex_md5hash(self.password[:15]).lower(),
            'pwd2':self.hex_md5hash(self.password).lower(),
            'imgcode':'',
            'f':'json',
            }
        request = urllib2.Request(url, urllib.urlencode(data))
        response = urllib2.urlopen(request)
        json_data = json.load(response)
        if json_data['ErrCode'] != 0:
            return False
        return cookies
 
    '''
        群组广播
        group_val=0为默认分组
    '''
    def broadcast(self, msg, group_val=0):
        suc = 0
        err = 0
        print '开始广播...'
        fansList = self.getFansList(group_val)
        for fans in fansList:
            try:
                self.postMessage(msg, fans['fakeId'])
                suc += 1
            except Exception, e:
                err += 1
                print e
                print '对帐号 % 广播失败' % fans['nickName']
        print '本次总共广播%d个好友，成功%d个，失败%d个。' % (len(fansList), suc, err)
 
 
if __name__ == '__main__':
    api = WeiXinAPI()
    api.login('1405034348', '3652htt')
#    api.postMessage('data1', '175605895')
#    api.postMessage('data2', '175605895')
#    api.postMessage('data3', '175605895')
    users=api.getFansList(group_val=0)
    for u in users:
        print u
#        print u['fakeId'],u['nickName']
        
#    print api.broadcast('hello world !')
