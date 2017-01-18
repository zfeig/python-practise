#!/usr/bin/env python
import re

pattern = re.compile(r'\d+')
res = re.split(pattern,'one1two2three3four')
print res 
