# coding:utf-8
'''
Created on Dec 10, 2012

@author: xen
'''

import web
import time
from datetime import datetime
from web.contrib.template import render_jinja

import config
from modules import filter

'''
return a render instance
set session to globals
'''
def render(tmp_dir):
    gconf = config.data
    gconf['uptime'] = serverInfo()
    render = render_jinja([config.pp + 'templates/', config.pp + 'templates/' + tmp_dir], encoding='utf-8')
    render._lookup.globals.update(session=web.config._session, gconf=gconf)
    render._lookup.filters.update(filter.filters)

    return render

def serverInfo():
    dt = datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
    return dt
