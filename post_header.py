#!/usr/bin/env python
import urllib
import urllib2

params = {"name":"liyongliang","pwd":"*akji89*"}
data = urllib.urlencode(params)
url = "http://192.168.63.241:8000/header.php"

header = {"X-REAL-IP":"15.68.35.89","Referer":"http://www.qq.com"}
req = urllib2.Request(url,data,header)
res = urllib2.urlopen(req)

print res.read()
