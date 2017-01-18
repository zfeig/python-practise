#!/usr/bin/env python

with open("read.txt") as read_file,open("write.txt","a+") as write_file:
   write_file.write("=================begin to write===========\n\r") 
   for line in read_file.readlines():
        write_file.write(line)
   write_file.write("~~~~~~~~~~~~~~~end to write~~~~~~~~~~~~~~~~~~\n\r")
