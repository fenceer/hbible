# coding:utf-8
'''
Created on Nov 18, 2012

@author: xen
'''


import re

# \d{1,3}(\/|:)\d{1,3}-(\d{1,3}|\d{1,3}(\/|:)\d{1,3})

pattern = r'^(\D{1,20})\s{0,3}(\d{1,3})\s{0,3}(?:\/|:)\s{0,3}(\d{1,3})\s{0,3}-\s{0,3}(\d{1,3})$'
ss = '太 11/2-12'
# match = re.search(r'\d', ss)
match = re.match(pattern, ss)
if match:
    sn = match.group(1)
    chp = int(match.group(2))
    start = int(match.group(3))
    end = int(match.group(4))
    if start > end:
        start = end
        end = start
    start = chp * 1000 + start
    end = chp * 1000 + end
    print start, end
else:
    print None
 
