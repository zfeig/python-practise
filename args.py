#!/usr/bin/env python

class AA:
    def __init__(self,*args):
         print "list:",args
         for v in args:
            print v



o = AA(1,2,3,4,5)
