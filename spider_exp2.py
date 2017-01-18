#!/usr/bin/env python
#coding=utf8
import re
str = '<li class="reply_num" title="纯原创我心中的NBA2014-2015赛季现役50大"><span>纯原创我</span>心中的<span>NBA</span>2014-2015赛季现役50大</li>'

pattern = re.compile(r'<li class="reply_num.*?><span>(.*?)</span>.*?<span>(.*?)</span>(.*?)</li>')
res = re.search(pattern,str)
if res:
    print res.group(1).strip() +"****"+ res.group(2).strip() +"****"+ res.group(3).strip() 
else:
    print "match failed!"


print "items by find!"

items = re.findall(pattern,str)
for item in items:
    print item

