#!/usr/bin/env python
import re
pattern = re.compile(r'hello\s(.*)+')

match = re.search(pattern,"hello good!")
if match:
    print match.group()
else:
    print "match failed!"

