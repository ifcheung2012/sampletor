# -*- coding: utf-8 -*-

__author__ = 'ifcheung'

from handlers import Request_Handler
from models.repository import *
from models.model import *
from utils import JSONEncoder
import json
from tornado.web import authenticated
import tornado.web


class UserHandler(Request_Handler):
    @authenticated
    def get(self):
        rep = user_repository(self.db)
        usr = rep.getsinglebyname(self.current_user)
        permitinfo = rep.getuserpermit(usr)
        algorithminfo = rep.getuseralgorithms(usr)
        self.render("index.html", data=self.current_user,permits= permitinfo,algorithms=algorithminfo)

    def post(self, *args, **kwargs):
        self.redirect("/")

class RegisterHandler(Request_Handler):
    def get(self, *args, **kwargs):
        self.render("register.html")

    def post(self, *args, **kwargs):
        uri = self.request.body
        dict = {}
        for i in uri.split('&'):
            data = i.split('=')
            dict[data[0]] = data[1]

        usr = User()
        for k in dict.keys():
            usr.__dict__[k] = dict[k]

        rep = user_repository(self.db)
        if rep.saveuseraddrole(usr,['normal','diaosi']):
            name,passwd = dict['name'],dict['passwd']
            self.set_secure_cookie("name",  name)
            usr = rep.getsinglebyname(name)
            self.current_user = usr             #todo it doesn't take effect,why?
            self.render("okregister.html", data= [name,passwd])
        else:
            msg_err = "Username is invalid! please input other!!"

class CheckUserHandler(Request_Handler):
    def get(self, *args, **kwargs):
        rep = user_repository(self.db)
        user = User(name=self.param('name'))
        if rep.checkuserexists(user):
            self.write("1")
            self.finish()
        else:
            self.write("0")
            self.finish()


class LoginHandler(Request_Handler):
    @tornado.web.asynchronous
    def get(self):
        if not self.current_user:
            self.render("login.html")
        else:
            name = self.get_secure_cookie("user")
            self.redirect("/")

    def post(self, *args, **kwargs):
        rep = user_repository(self.db)
        name, role = rep.validateuser(self.param('name'), self.param('passwd'))
        if name == None:
            self.redirect("login.html")
        self.set_secure_cookie("user", name)
        usr = rep.getsinglebyname(self.param('name'))
        self.current_user = usr
        self.redirect("/")


class LogoutHandler(Request_Handler):
    @authenticated
    def get(self):
        self.clear_cookie("user")
        self.redirect("/login")


if __name__ == '__main__':
    pass