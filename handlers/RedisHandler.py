# -*- coding: utf-8 -*-

__author__ = 'ifcheung'

from handlers import Request_Handler
from models.repository import *
from models.model import *
from utils import JSONEncoder
import json
from tornado.web import authenticated
import tornado.web

import redis

r = redis.Redis('localhost')
class UserHandler(Request_Handler):
    @authenticated
    def get(self):
        lottrep = lottery_repository(self.db)
        lotteryinfo=lottrep.list()
        res = []
        for a in lotteryinfo:
            r.lpush("lotterylst",a.redball)
            r.lpush("lotterylst","+")
            r.lpush("lotterylst",a.blueball)
        res = r.getrange("lotterylst",0,-1)
        self.render("redisinfo.html",lottsuperlst=res)

    def post(self):
        pass