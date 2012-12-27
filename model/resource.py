#coding:utf-8
'''
Created on Dec 11, 2012

@author: xen
'''

import web
from xml.dom import minidom

rdb = web.config.redis

def provinceList():
    if not rdb.exists('province'):
        doc = minidom.parse("resource/LocList.xml")
        prvs = {}
        state_name_list = []
        state_list = doc.getElementsByTagName('State')
        for state in state_list:
            state_name = state.getAttribute("Name")
            state_name_list.append(state_name)
        
            city_name_list = []
            city_list = state.getElementsByTagName('Select')
            
            for city in city_list:
                city_name = city.getAttribute("Name")
                city_name_list.append(city_name)
                
                region_name_list = []
                region_list = city.getElementsByTagName('Region')
                for region in region_list:
                    region_name_list.append(region.getAttribute("Name"))
                if len(region_name_list) > 0:
                    prvs[city_name] = '|'.join(region_name_list)
                    
            prvs[state_name] = '|'.join(city_name_list)
        prvs['prvnames'] = '|'.join(state_name_list)
            
        rdb.hmset('province', prvs)
    
    provinces = rdb.hget('province', 'prvnames').split('|')
    
    return provinces