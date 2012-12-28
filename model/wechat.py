# coding:utf-8
'''
Created on 2012-12-27

@author: fenceer
'''
import web
import hashlib
from xml.dom import minidom
import config

msgDict = config.msgDict
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
        text = msgDict[10004] + msgDict[10002] + msgDict[10001] 
    elif content in ['H', 'h']:
        text = msgDict[10005] + msgDict[10002] + msgDict[10001]
    elif content.startswith('#') or content.startswith('﹟'):
        db.proposal.insert(wmsg)
        text = msgDict[10006]
    elif content == '第三画':
        text = '耶稣爱你，我也爱你~/调皮'
    else:
        text = None
    return text
