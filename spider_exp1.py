#!/usr/bin/env python
#encoding=utf8
import re
str = '<h1 class="core_title_txt" title="纯原创我心中的NBA2014-2015赛季现役50大" style="width: 396px">纯原创我心中的NBA2014-2015赛季现役50大</h1>'

pattern = re.compile(r'<h1 class="core_title_txt.*?>(.*?)</h1>')
res = re.search(pattern,str)
if res:
    print res.group(1).strip()
else:
    print "match failed!"
