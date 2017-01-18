#!/usr/bin/env python
str  ="abzfxh,Hello,world http://www.fo.com?p=2&ip=1&name=&c_fpkc=Good One OKKC"
print "capitalize: %s" % (str.capitalize())
print "count: char %s has %d times" % ('l',str.count('l'))
en = str.encode(encoding="UTF-8",errors="strict")
print "encode: %s as %s" % (str,en)

de = en.decode(encoding="UTF-8",errors="strict")
print "decode: %s as %s" % (en,de)
