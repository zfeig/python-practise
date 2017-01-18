#!/usr/bin/env python
#coding=utf8
import re
pattern = re.compile(r'.*hello')

res1 = re.match(pattern,'hello')
res2 = re.match(pattern,'okchello CQC!')
res3 = re.match(pattern,'helo CQC!')
res4 = re.match(pattern,'good hello CQC!')


if res1:
    print res1.group()
else:
    print "1匹配失败"


if res2:
   print res2.group()
else:
    print "2匹配失败"


if res3:
    print res3.group()
else:
    print "3匹配失败"


if res4:
    print res4.group()
else:
    print '4匹配失败'

