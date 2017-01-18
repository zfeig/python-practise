#/usr/bin/env python

import md_test

print md_test.hello("lisi")
print "%d add %d is %d " % (2,5,md_test.sum(2,5))
print "cur time is %s" % (md_test.getTime())
