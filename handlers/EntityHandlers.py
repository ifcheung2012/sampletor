# -*- coding: utf-8 -*-
__author__ = 'ifcheung'
from utils.srvdecorators import service, REST
from models.model import User
from RestHandler import RestHandler


@service(User)
class UserService(object):
    pass


@REST(UserService)
class UsersRestHandler(RestHandler):
    pass
    # def __init__(self, application, request, **kwargs):
    #     super(UsersRestHandler, self).__init__( application, request, **kwargs)


if __name__ == '__main__':
    pass