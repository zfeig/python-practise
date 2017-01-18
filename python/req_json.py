#/usr/bin/env python
#coding:utf-8
import requests
#j = requests.get('./test.json')
j = requests.get('https://github.com/timeline.json')
print j.text
print j.json()

