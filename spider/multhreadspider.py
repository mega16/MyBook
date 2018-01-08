#!/usr/bin/env python
# encoding: utf-8
"""
@file: multhreadspider.py    
@time: 2018/1/8 22:45
@author: mongo
@version: python3.6     
@license: Apache Licence 
@contact: mega16@aliyun.com 
"""
import threading
import queue
import re
import urllib.request
import time
import urllib.error


urlqueue = queue.Queue()
# mock header
headers = ("")
opener = urllib.request.build_opener()
opener.addheaders = [headers]

# 将opener设为全局
urllib.request.install_opener(opener)
listurl = []

def use_proxy(proxy_addr, url):
    try:
        proxy = urllib.request.ProxyHandler({'http': proxy_addr})
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode('utf-8')
        return data
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)

        if hasattr(e, 'reason'):
            print(e.reason)
        time.sleep(10)
    except Exception as e:
        print('exception:'+ str(e))
        time.sleep(1)

# 线程1 专门处理对应网址并处理为真实网址
class GetUrl(threading.Thread):
    def __init__(self, key, pagestart, pageend, proxy, urlqueue):
        threading.Thread.__init__(self)
        self.pagestart = pagestart
        self.pageend = pageend
        self.proxy = proxy
        self.urlqueue = urlqueue
        self.key = key

    def run(self):
        page = self.pagestart
        # 编码关键词key
        pagecode = urllib.request.quote(self.key)
        try:
            pass
        except urllib.error.URLError as e:
            if hasattr(e, 'code'):
                print(e.code)

            if hasattr(e, 'reason'):
                print(e.reason)
            time.sleep(10)
        except Exception as e:
            print('exception:' + str(e))
            time.sleep(1)

# 线程2 获取原文
class GetContent(threading.Thread):
    def __init__(self, urlqueue, proxy):
        threading.Thread.__init__(self)
        self.urlqueue = urlqueue
        self.proxy = proxy

    def run(self):
        pass


class Conrl(threading.Thread):
    def __init__(self, urlqueue):
        self.urlqueue = urlqueue

    def run(self):
        while True:
            print('exec...')
            time.sleep(60)
            if(self.urlqueue.empty()):
                print('success')
                exit()

if __name__ == '__main__':
    key = ''
    proxy = ''
    pagestart = 1
    pageend = 10
    t1 = GetUrl(key, pagestart, pageend, proxy, urlqueue)
    t1.start()
    t2 = GetContent(urlqueue, proxy)
    t2.start()
    t3 = Conrl(urlqueue)
    t3.start()


