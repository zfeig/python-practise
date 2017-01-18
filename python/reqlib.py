#/usr/bin/env python
#coding:utf-8
import requests
r = requests.get("http://www.tmall.com")
print type(r)

print r.status_code
print r.encoding
