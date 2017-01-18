#!/usr/bin/env python
import random
f = open("test.txt","a")
msg = "this is msg:"+ str(random.randint(0,10)) +"\n"
f.write(msg)
f.close()
