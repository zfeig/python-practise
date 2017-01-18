#!/usr/bin/env python
import urllib
import urllib2

params = {"name":"xiaohe","pwd":"akji89#"}
data = urllib.urlencode(params)
url = "http://192.168.63.241:8000/get.php?" + data

req = urllib2.Request(url)
res = urllib2.urlopen(req)

print res.read()
