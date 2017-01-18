#!/usr/bin/env python
import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
   'user':'zfeig',
   'pwd':'123456'
})

loginUrl = "http://192.168.63.241:8000/cookie.php"
result = opener.open(loginUrl,postdata)
cookie.save(ignore_discard=True,ignore_expires=True)
print result.read()


