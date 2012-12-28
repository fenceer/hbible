# coding:utf-8
'''
Created on 2012-12-27

@author: fenceer
'''
import web
import hashlib
from xml.dom import minidom

db = web.config.db
TOKEN = '3652htt'

def getMsgObj(xdata):
    xobj = {}
    xdata = minidom.parseString(xdata)
    for node in xdata.getElementsByTagName('xml')[0].childNodes:
        if node.nodeName != '#text':
            xobj[node.nodeName] = getValue(xdata, node.nodeName)
    return xobj

def getValue(dom, key):
    return dom.getElementsByTagName(key)[0].firstChild.data.strip()

def checkSignature(data):
    ll = []
    ll.append(data.timestamp)
    ll.append(TOKEN)
    ll.append(data.nonce)
    ll.sort()
    ss = hashlib.sha1(''.join(ll)).hexdigest()
    return True if ss == data.signature else False

def quick(wmsg):
    content = wmsg['Content']
    if content == 'Hello2BizUser':
        text = '耶稣爱你~/微笑\n感谢您的关注！\n\n微圣经将竭力为您提供快捷的圣经查询服务.\n\n回复“#建议”提出宝贵的建议\n回复H查看使用帮助' 
    elif content in ['H', 'h']:
        text = '回复书卷名、章、节查询\n例如：“约翰福音3:16”或者 “马太福音6/9-13”\n书卷名支持中英文简写\n\n回复“#建议”提出宝贵的建议\n回复H查看使用帮助' 
    elif content.startswith('#'):
        db.proposal.insert(wmsg)
        text = '感谢您宝贵的建议，微圣经将努力完善/微笑'
    elif content == '第三画':
        text = '耶稣爱你，我也爱你~/调皮'
    else:
        text = None
    return text
