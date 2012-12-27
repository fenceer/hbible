#coding:utf-8
'''
Created on Nov 15, 2012

@author: xen
redis Key 管理
'''

import util

def groupHash(group_id):
    '''
    grouphash对象
        owner        组长
        gname        小组名
        managers     小组管理员
        member_num   小组成员计数器
        topic_num    小组话题计数器
    '''
    return 'GROUP:' + util.int_hex(group_id)

def groupShareZet(group_id):
    '''
    小组分享列表
    '''
    return 'SHARE:' + util.int_hex(group_id)

def topicReadSet(topic_id):
    '''
    话题浏览记录
    有效期一天:即一天之内访问统计一次
    '''
    return 'TOPIC:READ:' + util.int_hex(topic_id)

def userHash(user_id):
    '''
    userhash对象
    nick 用户名
    '''
    return 'USER:' + util.int_hex(user_id)

def markedZet(user_id):
    return 'MARK:' + util.int_hex(user_id)

def repliedZet(user_id):
    '''
    参与过的话题（回复过的）
    '''
    return 'REPLIED:' + util.int_hex(user_id)

def getSK(aid, bid):
    '''获得sessionKey'''
    return 'msg:' + util.int_hex(aid) + ':' + util.int_hex(bid)

def flwingZet(user_id):
    '''
    用户关注列表
    '''
    return 'FLWING:' + util.int_hex(user_id)

def flwerZet(user_id):
    '''用户粉丝列表'''
    return 'FLWER:' + util.int_hex(user_id)

def userGroupZet(user_id):
    '''用户加入的小组列表'''
    return 'USER:GRP:' + util.int_hex(user_id)

def mddName(mdd_id):
    '''目的地名字'''
    return 'MDD:' + util.int_hex(mdd_id)

def StyleHash():
    '''
    旅行风格
    存储id-name
    '''
    return 'Style'

def HotMddZet():
    '''
    热门目的地
    '''
    return 'MDD:HOT'

def HotGroupZet():
    '''
    热门小组
    '''
    return 'GRP:HOT'







