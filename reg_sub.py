#/usr/bin/env python
import re

pattern = re.compile(r'(\w+) (\w+)')
s = 'hello world good!'
print re.sub(pattern,r'\2 \1',s)

def Upper(m):
    return m.group(1).title() + ' ' + m.group(2).title()


print re.sub(pattern,Upper,s)
