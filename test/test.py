#coding:utf-8
'''
Created on Dec 13, 2012

@author: xen
'''
import time
import hashlib

TOKEN = '3652htt'
signature = '73227ad34daf3a68ba114011088d6ecd110ad10b'
timestamp = '1356589386'
nonce = '1355964664'
echostr = '5823823814753773919'

dc = {}
dc['token'] = 'TOKEN'
dc['nonce'] = 'nonce'
dc['timestamp'] = time.time()
ll = []
ll.append(timestamp)
ll.append(TOKEN)
ll.append(nonce)
print ll
ll.sort()
print ll
ss = hashlib.sha1(''.join(ll)).hexdigest()

print ss
