# -*- coding: utf-8 -*-
__author__ = 'ifcheung'

def check(name):
    def checkwrapper(func):
        def checking(self):
            print "check is %s." % name
            print "start checking"
            result = func(self)
            print "end checking"
            return result
        return checking
    return checkwrapper

def log(name):
    def logwrapper(func):
        def logging(self):
            print "log is %s ." % name
            print "start loging."
            result = func(self)
            print " end logging ."
            return  result
        return logging
    return logwrapper


class Myclass():
    @check("checkname")
    @log("logname")
    def process(self):
        print 'proccessing in class'

m = Myclass()
m.process()
if __name__ == '__main__':
    pass