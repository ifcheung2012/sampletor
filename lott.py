__author__ = 'IfCheung'
# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json
import json

apikey = "dd8de301fb09d7b589ac2ef9c8d30a58"



# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json

url = 'http://apis.baidu.com/keng7/soccerlottery/lottery?num=10'


req = urllib2.Request(url)

req.add_header("apikey", apikey)

resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    print(content)



# expect":"2015151","openCode":"15,16,18,30,35+01,07","openTime":"2015-12-26