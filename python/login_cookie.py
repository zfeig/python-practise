#!/usr/bin/env python
import urllib
import urllib2
import cookielib

filename = 'login.txt'
cookie = cookielib.MozillaCookieJar()
cookie.load(filename,ignore_discard=True,ignore_expires=True)


opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

postdata = urllib.urlencode({
   'user':'zfeig',
   'pwd':'123456'
})

loginUrl = "http://192.168.63.241:8000/cookie.php"
result = opener.open(loginUrl,postdata)
print result.read()


