#!/usr/bin/env python
# encoding: utf-8
"""
@file: picspider.py    
@time: 2018/1/8 22:29
@author: mongo
@version: python3.6     
@license: Apache Licence 
@contact: mega16@aliyun.com 
"""

import re
import urllib.request

def craw(url,page):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    pat1 = '<div id="plist",+? <div class="page clearfix">'
    result1 = re.compile(pat1).findall(html1)
    result1 = result1[0]
    pat2 = '<img width='
    imagelist = re.compile(pat2).findall(result1)
    x = 1
    for imageurl in imagelist:
        image_name =  ''
        image_url = 'http://' + imageurl
        try:
            urllib.request.urlretrieve(image_url, filename=image_name)
        except urllib.error.URLError as e:
            if hasattr(e, 'code'):
                x += 1
            if hasattr(e, 'reason'):
                x += 1
        x +=1

for i in range(10):
    url = ''
    craw(url, i)