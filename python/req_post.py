#!/usr/bin/env python
#coding:utf-8
import requests
params = {"user":"lisi","pwd":"135"}
url = "http://127.0.0.1:8000/post.php"

r = requests.post(url,data = params)
print r.text
