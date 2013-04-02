# coding: utf-8
'''
Created on 2013-2-25

@author: bubusy
'''

import MySQLdb
from jinja2.loaders import FileSystemLoader
from jinja2.environment import Environment

host = '192.168.1.131'
port = 3306
name = 'viva'
password = 'vivame'
dbname = 'pmsdb'
table_name = 'pms_t_block_nodecontent'

conn = MySQLdb.connect(host=host, port=port, user=name, passwd=password, db=dbname)
cur = conn.cursor()
cur.execute("SELECT column_name, data_type, character_maximum_length, is_nullable FROM information_schema.columns WHERE table_schema='" + dbname + "' AND table_name='" + table_name + "'")
rows = cur.fetchall()
cols = list(rows)

'''
methods
'''
def rename(cols):
    res = []
    for col in cols:
        # name
        words = col[0].split('_')
        nwords = [word.capitalize() for word in words]
        nword = ''.join(nwords)
        fs = nword[0:1]
        nfs = fs.lower()
        nword = nword.replace(fs, nfs, 1)
        ncol = {}
        ncol['name'] = nword
        ncol['colname'] = col[0]
        # length
        if col[2] != None:
            ncol['length'] = col[2]
        # null
        ncol['notnull'] = 'true' if col[3] == 'NO' else 'false'
        # type
        ctype = col[1]
        clen = col[2]
        ncol['type'] = 'Object'
        if ctype == 'int':
            if clen >= 10:
                ncol['type'] = 'Long'
                ncol['type2'] = 'long'
            else:
                ncol['type'] = 'Integer'
                ncol['type2'] = 'int'
        if ctype == 'varchar':
            ncol['type'] = 'String'
            ncol['type2'] = 'string'
        if ctype == 'datetime':
            ncol['type'] = 'Date'
            ncol['type2'] = 'timestamp'
        if ctype == 'float':
            ncol['type'] = 'Float'
            ncol['type2'] = 'float'
            
        res.append(ncol)
    return res



fields = rename(cols)
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('pojo.template')
print template.render(fields=fields)
template = env.get_template('pojo.hbm.xml')
print template.render(fields=fields)
