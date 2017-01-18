#!/usr/bin/env python
__metaclass__ = type
class Person:
    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name


    def info(self,msg):
        print " name:%s has msg: %s" % (self.name,msg)



s = Person("zfeig")
print s.name

s.info("hello,world!")

