#coding:utf-8
'''
Created on 2012-6-25

@author: Administrator
'''
import time
import string
import random
from random import choice
from bson.objectid import ObjectId

AVATAR_PATH = 'static/avatar/'
GROUP_ICON_PATH = 'static/groupIcon/'

def int_hex(num):
    return hex(int(num))[2:]

def str_int_List(strList):
    intList = [int(s) for s in strList]
    return intList

def hex_int(shex):
    return int('0x' + shex, 16)

def hex_int_list(hexList):
    intList = [hex_int(shex) for shex in hexList]
    return intList

def uniqueName():
    t = time.time()
    r = random.randint(1, 10000)
    s1 = str(hex(int(t * 1000))).replace('0x', '').replace('L', '')
    s2 = str(hex(r)).replace('0x', '')
    name = s2 + s1
    return name

def genRandomStr(length=8, chars=string.letters + string.digits):
    return ''.join([choice(chars) for i in range(length)])

def getAvatarPath(uid, size=0):
    if size == 0:
        return AVATAR_PATH + str(uid) + '.jpg'
    else:
        return AVATAR_PATH + str(size) + '/' + str(uid) + '.jpg'
    
def getGroupIconPath(group_id, size=0):
    if size == 0:
        return GROUP_ICON_PATH + str(group_id) + '.jpg'
    else:
        return GROUP_ICON_PATH + str(size) + '/' + str(group_id) + '.jpg'
    
def cpage(total, pagenum=1, pagesize=20):
    pagenum = int(pagenum)
    ptotal = 0
    if total % pagesize != 0:
        ptotal = total / pagesize + 1
    else:
        ptotal = total / pagesize
    re = {
          'pagesize': pagesize,
          'pagenum' : pagenum, #请求页码
          'total'   : total, #记录总数
          'ptotal'  : int(ptotal), #页数 
          'start'   : (pagenum - 1) * pagesize,
          'end'     : pagenum * pagesize - 1
          }
    return re

def pageList(docs, pagenum, pagesize=20):
    pager = cpage(docs.count(), pagenum, pagesize)
    docList = list(docs.skip(pager['start']).limit(pager['pagesize']))
    return docList, pager

def pageList_bak(data, collection, query, pagesize=20):
    pageSize = int(pagesize)
    pid = data.get('pid')
    pagenum = int(data.get('pagenum', 1))    #请求页码
    curnum = int(data.get('curnum', 1)) if pid else 1 #如果没有ID 则当前页为1
    
    pager = cpage(collection.find(query).count(), pagenum, pageSize)
    if pagenum < curnum:
        skip = (curnum - pagenum - 1) * pageSize
        query['_id'] = {'$gt':ObjectId(pid)}
        cs = collection.find(query).sort('_id', 1).skip(skip).limit(pageSize)
        cList = list(cs)[::-1]
    else:
        skip = (pagenum - curnum) * pageSize
        query['_id'] = {'$lte':ObjectId(pid)}
        cs = collection.find(query).sort('_id', -1).skip(skip).limit(pageSize)
        cList = list(cs)
        
    if len(cList) > 0:
        pager['pid'] = cList[0]['_id']
    
    return cList, pager
