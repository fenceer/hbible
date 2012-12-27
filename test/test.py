# coding:utf-8
'''
Created on Dec 13, 2012

@author: xen
'''
import re

pattern = ur'^(\D{1,20})(\d{1,3})\s{0,3}(?:\/|:){0,1}\s{0,3}(\d{0,3}\s{0,3}-{0,1}\s{0,3}\d{0,3})$'
# match = re.search(r'\d', ss)
ss = '太  2'
match = re.match(pattern, ss)
if match:
    print match.group()
else:
    print None
