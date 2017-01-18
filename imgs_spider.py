#!/usr/bin env python
import urllib2
import time

urls = ['https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p2393044761.jpg','https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p2391556881.jpg','https://img5.doubanio.com/view/movie_poster_cover/lpst/public/p2402162306.jpg','https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p2402824160.jpg','https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p2403319543.jpg','https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p2396092735.jpg']




def download(url):
    req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    data = res.read()

    #rename file name
    t = time.strftime("%Y-%m-%d-%H-%M-%S")
    filename ='http/img/' + str(t) + ".jpg"

    #write data to file
    f = open(filename,'w+')
    f.write(data)
    f.close()



for i in urls:
   download(i)
   print "download:"+i



print "~~~done~~~"
