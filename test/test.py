# -*- coding: utf-8 -*-
from  models.model import User
from utils import JSONEncoder
import json
from sqlalchemy.orm import scoped_session, sessionmaker
from models.model import *

# def addspam(fn):
#     def new(*args):
#         print "spam,spam,spam"
#         return fn(*args)
#     return new
#
# @addspam
# def useful(a, b):
#     print a*2+ b
# useful(3,4)


# +_++++++++++++++++++++++++++
# def flaz(self): return 'flaz'     # Silly utility method
# def flam(self): return 'flam'     # Another silly method
#
# def change_methods(new):
#     "Warning: Only decorate the __new__() method with this decorator"
#     if new.__name__ != '__new__':
#         return new  # Return an unchanged method
#     def __new__(cls, *args, **kws):
#         cls.flaz = flaz
#         cls.flam = flam
#         if hasattr(cls, 'say'): del cls.say
#
#         return super(cls.__class__, cls).__new__(cls, *args, **kws)
#     return __new__
#
# class Foo(object):
#     @change_methods
#     def __new__(): pass
#     def say(self): print "Hi me:", self
#
# foo = Foo()
# print foo.flaz()  # prints: flaz
#
# foo.say()         # AttributeError: 'Foo' object has no attribute 'say'
# +++++++++++++++++++++


# def elementwise(fn):
#     def newfn(arg):
#         if hasattr(arg,'__getitem__'):  # is a Sequence
#             return type(arg)(map(fn, arg))
#         else:
#             return fn(arg)
#     return newfn
#
# @elementwise
# def compute(x):
#     return x**3 - 1
#
# print compute(5)        # prints: 124
# print compute([1,2,3])  # prints: [0, 7, 26]
# print compute((1,2,3))  # prints: (0, 7, 26)
# def rest(Service):
#     class B(object):
#         def __init__(self,cls):
#             self.cls = cls
#             self.service= Service
#         def __call__(self, *args, **kwargs):
#             obj = self.cls(*args,**kwargs)
#
#             super(self.cls, obj).__init__(*args,**kwargs)
#             setattr(obj,"_service",self.service())
#             setattr(obj,"_eservice",self.service())
#             print obj.__dict__,type(obj)
#             return obj
#     return B
# def service(user):
#     class A(object):
#         def __init__(self, cls):
#             self.func = cls
#             self.cls = cls
#
#         def __call__(self, *args, **kwargs):
#             # print user
#             obj = self.cls(*args, **kwargs)
#             # obj._meta = self
#             # obj._entity = user
#             # print obj, type(obj)
#             methodsfield = ["insert","add","update"]
#             for method in methodsfield:
#                 if not hasattr(obj,method):
#                     setattr(obj,method,getattr(self,method))
#             # print obj.__dict__
#             return obj
#         def insert(self):
#             print "method insert"
#         def add(self):pass
#         def update(self):pass
#     return A
#
#
# @service("admin")
# class userservice(object):
#     pass
#
# @rest(userservice)
# class userrest(object):
#     pass
#
# # u = userservice()
# # u.insert()
# r = userrest()
# # print r.__dict__
# r._service.insert()

# def func1(x):
#     if not x:
#         return None
#     return True
#
# print func1(1)
# print func1(0)


# operator
# import operator
# import UserList
#
# def dump(data):
#     print type(data), "=>",
#     if operator.isCallable(data):
#         print "CALLABLE"
#     if operator.isMappingType(data):
#         print "MAPPING"
#     if operator.isNumberType(data):
#         print "NUMBER"
#     if operator.isSequenceType(data):
#         print "SEQUENCE"
#
# print dump(UserList.UserList)

# seq = 1,2,4
# print "add","=>",reduce(operator.add,seq)
# print "sub","=>",reduce(operator.sub,seq)
# print "mul","=>",reduce(operator.mul,seq)
# print "concat","=>",operator.concat("spam","eggs")
# print "repeat","=>",operator.repeat("spma",5)
# print "spma"*5
# print "getitem",'=>',operator.getitem(seq,2)


# #shadow copy
# import copy
# a =[[1],[[1],[2]],[3]]
# b = copy.copy(a)
# print "before","=>"
# print "a","=>",a
# print "b","=>",b
# print "after","=>"
# a[0][0] = 0
# a[1][1][0] = None
# print "a","=>",a
# print "b","=>",b
# #deep copy
# a =[[1],[[1],[2]],[3]]
# b = copy.deepcopy(a)
# print "before","=>"
# print "a","=>",a
# print "b","=>",b
# print "after","=>"
# a[0][0] = 0
# a[1][1][0] = None
# print "a","=>",a
# print "b","=>",b

import sys
# print type(sys.path)
# print "sys path has", len(sys.path), "members"
# print sys.builtin_module_names
# # print sys.modules.keys()
# print sys.platform
# def test(n):
#     j = 0
#     for i in xrange(n):
#         j = j + i
#     return j,n
#
# def profiler(frame,event,arg):
#     print event,frame.f_code.co_name,frame.f_lineno,"->",arg
# sys.setprofile(profiler)
# test(4)
# sys.setprofile(None)
# print "============="
# def tracer(frame, event, arg):
#     print event, frame.f_code.co_name, frame.f_lineno, "->", arg
#     return tracer
# sys.settrace(tracer)
# test(1)
# sys.settrace(None)
# print "============="
# test(2)

#
# import getpass
# usr = getpass.getuser()
# print "getuser()"
# pwd = getpass.getpass("enter password for user %s:" % usr)
# print usr,pwd


# import urllib
# fp = urllib.urlopen("http://www.baidu.com")
# fp.read()
# print fp.headers

# import urlparse
#
# url = "http://item.taobao.com/item.htm?spm=a230r.1.14.33.ufYN9r&id=26617820141&_u=s3pki0lcbdc"
# scheme,host,path,params,query,fragment =\
# urlparse.urlparse(url)
#
# print scheme,host,path,params,query,fragment

import Cookie
import os,time
# cookie = Cookie.SimpleCookie()
# cookie["users"]="ifcheung"
# cookie["timestamp"] = time.time()
# print cookie

# import robotparser
# r = robotparser.RobotFileParser()
#
# r.set_url("http://127.0.0.1:8007/register")
# r.read()

# import ftplib
#
# ftp = ftplib.FTP("192.168.1.1")
# ftp.login("jamix","xpendif")
# print ftp.dir()
# ftp.quit()

# import httplib
#
# USER_AGENT="test.py"
# class Error:
#     def __init__(self,url,errcode,errmsg,headers):
#         self.url = url
#         self.errcode = errcode
#         self.errmsg = errmsg
#         self.headers =headers
#     def __repr__(self):
#         return ("<Error for %s: %s %s>" % (self.url,self.errcode,self.errmsg))
#
# class Server:
#     def __init__(self,host):
#         self.host =host
#
#     def fetch(self,path):
#         http = httplib.HTTP(self.host)
#         http.putheader("GET",path)
#         http.putheader("User-Agent",USER_AGENT)
#         http.putheader("Host",self.host)
#         http.putheader("Accept","*/*")
#         http.endheaders()
#
#         errcode, errmsg, headers = http.getreply()
#         if errcode != 200:
#             raise Error(errcode,errmsg,headers)
#         file = http.getfile()
#         return file.read()
# server = Server("www.baidu.com")
# print server.fetch("/index.html")


# import smtplib
# import string ,sys
#
# HOST="localhost"
# FROM = "auditor1982@hotmail.com"
# TO ="auditor1982@hotmail.com"
# SUBJECT = "FOR UR INFOR"
# BODY = " NEXT WEEK:HOW TO FILING AN OTHER"
# bd = string.join(("from: %s" % FROM,"To: %s" % TO,\
#                   "Subject: %s" % SUBJECT,\
#                   "",\
#                   BODY),\
#                  "\r\n")
# srv = smtplib.SMTP(HOST)
# srv.sendmail(FROM,[TO],bd)
# srv.quit()



# import webbrowser
# import time
# webbrowser.open("http://127.0.0.1:8007")


# import locale
# print "locale","=>",locale.setlocale(locale.LC_ALL,"")
# value =47.11
# print locale.format("%d",value,1)
# info = locale.localeconv()
# print info
# print info["int_curr_symbol"]

# language, encoding = locale.getdefaultlocale()
# print language, encoding


import math
import string
import time









if __name__ == '__main__':
    # usr = User()

    # import models.repository
    # session = scoped_session(sessionmaker(engine))
    # name = 'jamix'
    # res = session.query(User).filter(User.name.like('%' + name + '%'))
    # print type(res)
    # for r in res:
    #     print json.dumps(r,cls=JSONEncoder)

    pass


