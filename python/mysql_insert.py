#!/usr/bin/env python
#coding=utf-8
import MySQLdb
conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='test',charset='utf8')
cur =conn.cursor()
#cur.execute("insert into category(name) values ('test')")
cur.execute("insert into category(name) values ('娱乐八卦')")
conn.commit()



