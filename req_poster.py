#usr/bin/env python
#coding:utf-8
import requests
import json
url ="http://127.0.0.1:8000/post.php"
params = {"user":"zfeig","pwd":"123456"}
r =requests.post(url,data = json.dumps(params))
print r.text
print r.json()
