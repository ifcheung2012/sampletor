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


class RedisHandler(Request_Handler):

    def get(self):
        r = redis.Redis('127.0.0.1')
        r.delete("lotterylst")
        lottrep = lottery_repository(self.db)
        lotteryinfo=lottrep.list()
        res = []
        for a in lotteryinfo:
            r.lpush("lotterylst",a.redball)
            r.lpush("lotterylst","+")
            r.lpush("lotterylst",a.blueball)

        # r2 = redis.Redis('127.0.0.1')
        res = r.lrange("lotterylst",0,-1)
        self.render("redisinfo.html",lottsuperlst=res)

    def post(self):
        pass