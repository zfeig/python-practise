#!/usr/bin env python
import urllib2
import time
#url ="https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p2394573821.jpg"
url= "https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p2406829205.jpg"


req = urllib2.Request(url)

res = urllib2.urlopen(req)

data = res.read()

#rename file name
t = time.strftime("%Y-%m-%d-%M-%H-%S")
filename ='http/img/' + str(t) + ".jpg"

#write data to file
f = open(filename,'w+')
f.write(data)
f.close()




