#/usr/bin/env python
#coding:utf-8
from bs4 import BeautifulSoup
soup = BeautifulSoup("<html><head><title>hello,world!</title></head><body><a href='http://www.ifeng.com'>ifeng</a><p class='link' style='height:200px;'>爬虫测试</p><div class='test'><a href='http://www.qq.com'>link</a><li><a href='http://www.qq.com'>link1</a></li></div><p>hello,world</p></body></html>")
title = soup.title
p = soup.p
print soup.prettify()
print "title %s" % (title)
print "p %s"%(p)
print "p name:%s" % (p.name)
print "p value:%s" % (p.string)
print "p class:%s" % (p["class"])
print "p style:%s" % (p["style"])
print "a link:%s" % (soup.a)
print "find_all a link:%s" % (soup.find_all('a'))
print "find_all p:%s" % (soup.find_all('p'))
print "find_all div:%s" % (soup.find_all('div'))
print "head :%s" % (soup.head.contents)
print "head :%s" % (soup.head.string)
print "=========================================="
for link in soup.find_all('a'):
    print link.get('href')
