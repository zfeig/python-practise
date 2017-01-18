#!/usr/bin/env python
#coding=utf8
import urllib2
url = "http://www.baidu.com"
res = urllib2.urlopen(url)
data = res.read()

f= open("baidu.txt","a")
f.write(data)
f.close()

