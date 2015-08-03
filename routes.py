# -*- coding: utf-8 -*-
from handlers.User import *
from handlers.LotteryHandler import *
from handlers.RedisHandler import *
from handlers.Analyse import *
from handlers.Longconnect import *
from handlers.alamofirets import *

handlers = [
    (r"/", UserHandler),
    (r"/login", LoginHandler),
    (r"/logout", LogoutHandler),
    (r"/register", RegisterHandler),
    (r"/long", longhandler),
    (r"/cloud/analyse/algo/([0-9]+)", AnalyseHandler),
    (r"/checkuser", CheckUserHandler),
    (r"/lottery", LotteryHandler),
    (r"/redisinfo", RedisHandler),
    (r"/alamofire", AlamofireHandler),
]

if __name__ == '__main__':
    pass
