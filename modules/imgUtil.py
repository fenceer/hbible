#coding:utf-8
'''
Created on 2012-10-14

@author: fenceer
'''
from PIL import Image
import urllib

def resizeImg(img, size, path):
    img = img.resize(size, Image.ANTIALIAS)
    img.save(path, quality=100) 

'''返回Image对象'''
def imgCut(filePath, coord=None):
    img = Image.open(filePath)
    width, height = img.size
    if coord:
        #HTML页面图片宽度为330PX 等比例缩放
        scale = width / 330.0 
        box = (int(coord[0] * scale), int(coord[1] * scale), int(coord[2] * scale), int(coord[3] * scale))
        cutImg = img.crop(box)
    else:
        if width == height:
            cutImg = img
        else:
            if width > height:
                fix = int((width - height) / 2)
                box = (fix, 0, fix + height, height)
            else:
                fix = int((height - width) / 2)
                box = (0, fix, width, fix + width)
            cutImg = img.crop(box)
            
    return cutImg.convert('RGB')

def saveWebImg(url, savepath):
    img = urllib.urlopen(url).read()
    output = open(savepath, 'wb+')  
    output.write(img)  
    output.close()
