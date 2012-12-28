# coding:utf-8
'''
Created on Nov 29, 2012

@author: xen
'''

data = {}
mddType = ['古镇', '温泉', '滑雪', '都市', '名胜', '其他']
data['img_domain'] = 'http://kapian.b0.upaiyun.com'
data['domain'] = 'http://back.zobei.com:8080'
data['mddType'] = mddType

msgDict = {
         10001:'回复h查看使用帮助\n',
         10002:'回复“#建议”提出您宝贵的建议\n',
         10003:'微圣经努力学习中/可爱\n',
         10004:'耶稣爱你~/微笑\n感谢您的关注！\n\n微圣经将竭力为您提供快捷的圣经查询服务.\n\n',
         10005:'回复书卷名、章、节查询\n例如：“约翰福音3:16”或者 “马太福音6/9-13”\n书卷名支持中英文简写\n\n',
         10006:'感谢您宝贵的建议，微圣经将努力完善/微笑\n'
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
