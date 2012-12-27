#coding:utf-8
'''
Created on 2012-9-21

@author: fenceer
'''

import web
import time
from datetime import datetime

from modules import util, rdbKey

db = web.config.db
rdb = web.config.redis
rpipe = rdb.pipeline()
session = web.config._session

def ftime(timestamp, fromat='%Y-%m-%d', short=True):
    timestamp = float(timestamp)
    if not short:
        return datetime.fromtimestamp(timestamp).strftime(fromat)

    fdate = ''
    diff = (time.time() - timestamp)
    if diff < (60 * 1):
        fdate = '刚刚'
    elif diff < (60 * 60 * 1):
        fdate = str(int(diff / 60)) + '分钟前'
    elif diff < (60 * 60 * 24 * 1):
        fdate = str(int(diff / (60 * 60))) + '小时前'
    elif diff < (60 * 60 * 24 * 7):
        fdate = str(int(diff / (60 * 60 * 24))) + '天前'
    else:
        fdate = datetime.fromtimestamp(timestamp).strftime(fromat)
    return fdate

def flwerCount(uid):
    return rdb.zcard(rdbKey.flwerZet(uid))

def flwingCount(uid):
    return rdb.zcard(rdbKey.flwingZet(uid))

def avatar(uid, typ='user', size=0):
    if typ == 'group':
        return '/' + util.getGroupIconPath(uid, size)
    else:
        return '/' + util.getAvatarPath(uid, size)

def groupName(group_id):
    #小组名
    gname = rdb.hget(rdbKey.groupHash(group_id), 'gname')
    if gname is None:
        group = db.team.find_one({'_id':int(group_id)}, {'gname':1})
        gname = group['gname'] if group else '未命名小组'
        rdb.hset(rdbKey.groupHash(group_id), 'gname', gname)
    return gname

def mddName(mdd_id):
    '''目的地名字'''
    mddName = rdb.get(rdbKey.mddName(mdd_id))
    if not mddName:
        mdd = db.mdd.find_one({'_id':int(mdd_id)}, {'name':1})
        if mdd:
            mddName = mdd['name'] 
            rdb.set(rdbKey.mddName(mdd_id), mddName)
        else:
            mddName = ''
            
    return mddName

def styleName(style_id):
    '''旅行风格'''
    styleName = rdb.hget(rdbKey.StyleHash(), style_id)
    if not styleName:
        style = db.style.find_one({'_id':int(style_id)}, {'name':1})
        if style:
            styleName = style['name'] 
            rdb.hset(rdbKey.StyleHash(), style_id, styleName)
        else: 
            styleName = ''
    
    return styleName

def topicNum(group_id):
    topic_num = rdb.hget(rdbKey.groupHash(group_id), 'topic_num')
    if topic_num is None:
        topic_num = db.topic.find({'group_id':group_id, 'del':0}).count()
        rdb.hset(rdbKey.groupHash(group_id), 'topic_num', topic_num)
    return int(topic_num)
    
def nick(user_id):
    nick = rdb.hget(rdbKey.userHash(user_id), 'nick')
    if nick is None:
        user = db.user.find_one({'_id':int(user_id)}, {'nick':1})
        nick = user['nick'] if user else '匿名用户'
        rdb.hset(rdbKey.userHash(user_id), 'nick', nick)
    return nick

def isMark(topic_id):
    ts = rdb.zscore(rdbKey.markedZet(session.get('uid', 0)), util.int_hex(topic_id))
    return True if ts else False

def isLike(post_id):
    like = db.like.find_one({'post_id':int(post_id), 'user_id':session.get('uid', 0)})
    return True if like else False

def isMember(group_id):
    ts = rdb.zscore(rdbKey.userGroupZet(session.get('uid', 0)), util.int_hex(group_id))
    return True if ts else False

def isfollow(fid):
    ts = rdb.zscore(rdbKey.flwingZet(session.get('uid', 0)), util.int_hex(fid))
    return True if ts else False 

def grpCount(group_id, count):
    num = 0
    if count == 'member':
        num = rdb.hget(rdbKey.groupHash(group_id), 'member_num')
    elif count == 'topic':
        num = rdb.hget(rdbKey.groupHash(group_id), 'topic_num')
    elif count == 'post':
        num = rdb.zcard(rdbKey.groupShareZet(group_id))
        
    return num if num else 0

filters = {
            'nick':nick,
            'ftime':ftime,
            'gname':groupName,
            'grpCount':grpCount,
            'topicNum':topicNum,
            'avatar':avatar,
            'isMark':isMark,
            'isLike':isLike,
            'isfollow':isfollow,
            'isMember':isMember,
            'mddName':mddName,
            'styleName':styleName,
            'flwerCount':flwerCount,
            'flwingCount':flwingCount
            }
