# -*- coding: utf-8 -*-

__author__ = 'ifcheung'

from handlers import Request_Handler
from models.repository import *
from models.model import *
from utils import JSONEncoder
import json
from tornado.web import authenticated
import tornado.web


class LotteryHandler(Request_Handler):

    def get(self):
        lottrep = lottery_repository(self.db)
        lotteryinfo = lottrep.list()
        res = []
        for a in lotteryinfo:
            res.append(a.redball)
            res.append(a.blueball)

        self.render("lotterylist.html",lottsuperlst=res)

    def post(self, *args, **kwargs):
        self.redirect("/")
