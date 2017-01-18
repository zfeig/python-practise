#!/usr/bin/env python
class Hook(object):
    def __init__(self,name,mod):
         self.name = name
         self.mod = mod

    def __enter__(self):
         print "====begin to enter====\n\r"
         self.open_file = open(self.name,self.mod)
         return self.open_file


    def __exit__(self,*others):
         self.open_file.close()
         print "~~~~file closed~~~~\n\r"

    




with  Hook("read.txt","r") as reader:
        print "read linline:"
        for line in reader:
          print line
