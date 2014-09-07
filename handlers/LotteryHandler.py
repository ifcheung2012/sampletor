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
        lotteryinfo=lottrep.list()
        res = []
        for a in lotteryinfo:
            res.append(a.redball)
            res.append(('/r'))
            res.append(a.blueball)
        # self.write(str(res))
        self.render("/lotterylist.html",lottsuperlst=res)
        # rep = user_repository(self.db)
        # usr = rep.getsinglebyname(self.current_user)
        # permitinfo = rep.getuserpermit(usr)
        # algorithminfo = rep.getuseralgorithms(usr)
        # self.render("index.html", data=self.current_user,permits= permitinfo,algorithms=algorithminfo)

    def post(self, *args, **kwargs):
        self.redirect("/")
