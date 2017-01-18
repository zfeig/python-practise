#!/usr/bin/env python
#coding=utf8
import urllib2
url = "http://www.qq.com"
req = urllib2.Request(url)
res = urllib2.urlopen(req)
data = res.read()

f= open("qq.txt","a+")
f.write(data)
f.close()

