# coding:utf-8
'''
Created on 2012-12-27

@author: fenceer
'''
import web
import hashlib
from xml.dom import minidom
import config
import urllib
import model

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

def quick(content):
    if content == 'Hello2BizUser':
        text = msgDict[10004] + msgDict[10002] + msgDict[10001] 
    elif content in ['H', 'h']:
        text = msgDict[10005] + msgDict[10002] + msgDict[10001]
    elif content.startswith('?') or content.startswith('？'):
        content = content[1:]
        text = search(content)
        if not text:
            text = msgDict[10003] + msgDict[10008] + urllib.quote(content.encode('utf-8')) + msgDict[10009] + msgDict[10001]
    elif content == '第三画':
        text = '耶稣爱你，我也爱你~/调皮'
    else:
        text = None
    return text

def search(content):
    chapter = model.word.checkChapter(content)
    '''如果查不到经文就搜索数据库和wiki'''
    if chapter:
        text = chapter 
    else:
        subject = db.subject.find_one({'title':content})
        if subject:
            text = subject['desc']['text']
        else:
#            req = urllib2.Request(config.WIKI_URL + content)
#            resp = urllib2.urlopen(req)
#            body = resp.read()
#            xwiki = minidom.parseString(body)
#            rev = xwiki.getElementsByTagName('rev')
#            text = rev[0].firstChild.data.strip()  if rev else None
            text = None
    return text
