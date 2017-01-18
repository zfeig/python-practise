#!/usr/bin/env python

while 1:
        print "this is a division programe!"
        c = raw_input("input char'D'  to contniue...\n")
        if c.lower() == "d":
            a = raw_input("first num:")
            b = raw_input("second num:")
            try:
               print float(a)/float(b)
               print "********************************\n\r"           
            except ZeroDivisionError:
               print "the second num can't be zero!"
               print "********************************\n\r"
            except ValueError:
               print "input value must be number! "
               print "********************************\n\r"
        else:
            print "input error!"
            break
