#coding:utf-8
'''
Created on 2012-7-19

@author: bubusy
'''

import time
import random
from modules import upyun

'''
constant define
'''
UPYUN_BUCKET = 'bailuobo'
UPYUN_USERNAME = 'blb'
UPYUN_PASSWORD = '123321blb'
UPYUN_APIDOMAIN = 'v0.api.upyun.com'


def uniqueName():
    t = time.time()
    r = random.randint(1, 10000)
    s1 = str(hex(int(t * 1000))).replace('0x', '').replace('L', '')
    s2 = str(hex(r)).replace('0x', '')
    name = s2 + s1
    return name

def uploadImgToUpyun(data, filename='', updir=''):
    '''
    #######Example:########
    
    from lib.uploader import uploadImgToUpyun
    
    data = open('static/w.jpg', 'rb')
    result, info = uploadImgToUpyun(data,'','share')
    print result
    print info
    '''
    fname = ''
    path = ''
    info = {}
    def getPath():
        _isrecover = False
        if filename != '':
            fname = filename
            _isrecover = True
        else:
            fname = uniqueName()
        if updir != '':
            path = '/' + updir + '/' + fname
        else:
            path = fname
        return fname, path, _isrecover
    fname, path, isrecover = getPath()
    u = upyun.UpYun(UPYUN_BUCKET, UPYUN_USERNAME, UPYUN_PASSWORD)
    u.setApiDomain(UPYUN_APIDOMAIN)
    try:
        times = 0#check exists 3 times
        if not isrecover:
            while True:
                fi = u.getFileInfo(path)
                if fi:
                    times += 1
                    fname, path = getPath()
                    print times
                else:
                    break
                if times > 3:
                    return False, info
        result = u.writeFile(path, data, True, {})
        if result:
            info['name'] = fname
            info['path'] = path
            info['width'] = u.getWritedFileInfo('x-upyun-width')
            info['height'] = u.getWritedFileInfo('x-upyun-height')
            info['frames'] = u.getWritedFileInfo('x-upyun-frames')
            info['type'] = u.getWritedFileInfo('x-upyun-file-type')
    except upyun.UpYunException:
        return False, info
    return result, info
