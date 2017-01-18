#!/usr/bin/env python

import MySQLdb
conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='test',charset='utf8')
cursor =conn.cursor()
sql = "SELECT * FROM article"
cursor.execute(sql)
result = cursor.fetchall()
for item in result:
    print "id:%d  title:%s" % (item[0],item[1])




