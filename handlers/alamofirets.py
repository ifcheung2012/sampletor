__author__ = 'ifcheung'

from handlers import Request_Handler
from models.repository import *
from models.model import *
from utils import JSONEncoder
import json
from tornado.web import authenticated
import tornado.web


class AlamofireHandler(Request_Handler):
    def get(self):
        lsres = getjsonstr()
        self.write(lsres)
        # self.render("alamofiretest.html", lsres=lsres)

    def post(self, *args, **kwargs):
        self.redirect("/")


def getage(name):
    return 12


class Student(object):
    """docstring for Student"""

    def __init__(self, name, age, teacher):
        self.name = name
        self.age = age
        self.teacher = teacher


class Teacher(object):
    """docstring for Teacher"""

    def __init__(self, title, sex, age):
        super(Teacher, self).__init__()
        self.title = title
        self.sex = sex
        self.age = age


def object2dict(obj):
    # convert object to a dict
    d = {}
    # d['__class__'] = obj.__class__.__name__
    # d['__module__'] = obj.__module__
    d.update(obj.__dict__)
    return d


def getjsonstr():

    teach = Teacher("supteacher", "male", 34)
    tmpteach = {'tcdata': ['momocha', 'okcha', [2, 1, 3]], 'isthat': True}
    st = Student("jack", 10, tmpteach)
    # st = Student("jack", 10, teach)
    lottLst = getlottres()
    reslst = []
    resdic,resdic3,resdic2,outres = {},{},{},{}

    resdic["lottResult"] = str(lottLst)
    resdic["lottPhase"] = 127
    resdic["lottCat"] = "SuperLott"
    resdic["lottImg"] = "http://resource.feng.com/resource/h041/h26/img201410081311370.jpg"
    resdic["lottRecommend"] = 9
    reslst.append(resdic)

    resdic2["lottResult"] = str(lottLst)
    resdic2["lottPhase"] = 128
    resdic2["lottCat"] = "SuperLott"
    resdic2["lottImg"] = "http://resource.feng.com/resource/h041/h26/img201410081311370.jpg"
    resdic2["lottRecommend"] = 6
    reslst.append(resdic2)

    resdic3["lottResult"] = str(lottLst)
    resdic3["lottPhase"] = 33
    resdic3["lottCat"] = "fucai"
    resdic3["lottImg"] = "http://resource.feng.com/resource/h041/h26/img201410081311370.jpg"
    resdic3["lottRecommend"] = 6
    reslst.append(resdic3)

    outres["content"] = reslst
    resjson = json.dumps(outres, default=object2dict)

    # return resjson
    return resjson


import numpy as np


def getlottres():
    a1 = [1, 2, 2, 2, 3, 4, ]
    a2 = [3, 5, 6, 7, 8, 8, ]
    a3 = [3, 4, 7, 8, 9, 9, ]
    a4 = [2, 3, 5, 7, 8, 9, ]

    complete = np.concatenate((a1, a2, a3, a4))
    uvals, uind = np.unique(complete, return_inverse=True)
    return uvals[np.bincount(uind).argsort()[-4:]][::-1].tolist()


if __name__ == '__main__':
    teach = Teacher("supteacher", "male", 34)
    tmpteach = {'tcdata': ['momocha', 'okcha', [2, 1, 3]], 'isthat': True}
    st = Student("jack", 10, tmpteach)
    motmp = getjsonstr()
