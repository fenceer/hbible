#coding:utf-8
'''
Created on Aug 3, 2012

@author: fenceer
'''
import web
from PIL import Image,ImageDraw,ImageFont
import random,StringIO

session = web.config._session

class CodeNum:
    def GET(self):
        web.header("Content-Type",'image/gif')
        """
        background  #随机背景颜色
        line_color #随机干扰线颜色
        img_width = #画布宽度
        img_height = #画布高度
        font_color = #验证码字体颜色
        font_size = #验证码字体尺寸
        font = I#验证码字体
        """
         
        string = {'number':'12345679',
                  'litter':'ACEFGHKMNPRTUVWXY'}
        background = (random.randrange(230,255),random.randrange(230,255),random.randrange(230,255))
        line_color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        img_width = 80
        img_height = 32
        font_color = ['black','darkblue','darkred']
        font_size = 40
        font = ImageFont.truetype('resource/FreeMono.ttf',font_size)
        session.verify = ''
     
        #新建画布
        im = Image.new('RGB',(img_width,img_height),background)
        code = random.sample(string['litter'],4)
        #新建画笔
        draw = ImageDraw.Draw(im)
     
        #画干扰线
        for i in range(random.randrange(3,10)):
            xy = (random.randrange(0,img_width),random.randrange(0,img_height),
                  random.randrange(0,img_width),random.randrange(0,img_height))
            draw.line(xy,fill=line_color,width=1)
         
        #写入验证码文字
        x = 8
        for i in code:
            y = random.randrange(-10,0)
            draw.text((x,y), i, font=font, fill=random.choice(font_color))
            x += 15
            session.verify += i
        del x
         
        del draw
        buf = StringIO.StringIO()
        im.save(buf,'gif')
        buf.closed
        return buf.getvalue()
