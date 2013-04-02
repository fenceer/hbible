# coding:utf-8
'''
Created on Nov 29, 2012

@author: xen
'''
import os

data = {}
mddType = ['古镇', '温泉', '滑雪', '都市', '名胜', '其他']
data['img_domain'] = 'http://kapian.b0.upaiyun.com'
data['domain'] = 'http://back.zobei.com:8080'
data['mddType'] = mddType
WIKI_URL = 'http://www.weibible.org/s/edit?ss='

pp = os.environ.get('OPENSHIFT_REPO_DIR')
pp = pp  if pp else ''

msgDict = {
         10001:'回复h查看使用帮助\n',
         10002:'回复“#建议”提出您的建议\n',
         10003:'微圣经努力学习中\n',
         10004:'耶稣爱你~/微笑\n感谢您的关注！\n\n微圣经将竭力为您提供快捷的圣经查询服务.\n\n',
         10005:'微圣经查询语法：\n章和小节用任意标点隔开(冒号，斜杠等都可以)\n例如：“约翰福音3:16”\n\t\t\t  “约翰福音3:16”\n小节之间用"-"连接\n例如：“马太福音6:9-13”\n\t\t\t  “加5:22-23”\n\n温馨提示：\n书卷名可以用简写或拼音首字母缩写哦\n例如：“约3/16”\n\t\t\t  “太6/9-13”\n\t\t\t  “mtfy6/9-13”\n',
         10006:'感谢您宝贵的建议，微圣经将努力完善/微笑\n',
         10007:'\n回复"n"或者"下一页"查看下一页',
         10008:'欢迎登录' + WIKI_URL,
         10009:'\n帮助微圣经学习\n以便为大家提供更好的圣经查询服务\n',
         10010:'回复“?耶稣”查询圣经名词\n',
         10011:'感谢您的使用/可爱\n'
         }

errorDesc = {
             10001:'system error',
             10010:'value error',
             10011:'mdb error',
             10012:'rdb error',
             10013:'youpai error',
             
             10404:'not found',
             
             # user
             20001:'not login',
             20010:'invalid email or password',
    
    }
