#coding: utf-8

'''
加载目录下的所有url配置文件。
url配置文件是一个python源代码文件，以url_开头，里面定义了urls（list类型）变量。
interceptor:后面定义了当前url的拦截器
'''

import os
urls = []
INTERCEPTOR = 'interceptor:'
global_interceptors = ['access.AutoLogin']
#global_interceptors = []
interceptors = {}

for f in os.listdir(os.path.split(__file__)[0]):
    module_name, ext = os.path.splitext(f)
    if module_name.startswith('url_') and ext == '.py':
        module = __import__(__name__ + '.' + module_name, fromlist=module_name)
        for i, url in enumerate(module.urls):
            if url.startswith(INTERCEPTOR):
                interceptors[module.urls[i - 2]] = global_interceptors + url.replace(INTERCEPTOR, '').split(',')
            else:
                #如不是拦截器配置，则加进urls
                urls.append(url)
                if url.startswith('/') :
                    interceptors[url] = global_interceptors + module.local_interceptor

#        urls.extend(module.urls)
