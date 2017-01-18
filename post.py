#!/usr/bin/env python
import urllib
import urllib2

params = {"name":"liyongliang","pwd":"*akji89*"}
data = urllib.urlencode(params)
url = "http://192.168.63.241:8000/post.php"

req = urllib2.Request(url,data)
res = urllib2.urlopen(req)

print res.read()
