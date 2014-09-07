# -*- coding: utf-8 -*-
import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.web import url
from tornado.options import define, options
from handlers.User import UserHandler
from sqlalchemy.orm import scoped_session, sessionmaker
from models.model import engine
from routes import handlers

define("debug", default=False, type=bool)
define("port", default=8007, help="run on the given port", type=int)

define("title", default="Pagina de prueba", help="Page title", type=str)
define("company_name", default="La compania", help="Company name", type=str)

define("db_user", default="root", help="User for database", type=str)
define("db_pass", default="123", help="User password for database", type=str)
define("db_host", default="192.168.1.100", help="Database server", type=str)
define("db_dbname", default="ifcheung", help="Database server", type=str)
define("db_port", default=3306, help="Database server", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            debug=options.debug,
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            xsrf_cookie=False,
            cookie_secret="bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
            login_url="/login",
        )
        self.session = scoped_session(sessionmaker(bind=engine))
        tornado.web.Application.__init__(self, handlers, **settings)

        # from handlers.EntityHandlers import UsersRestHandler
        # from handlers.RestHandler import RestHandler
        #
        # tornado.web.Application.__init__(self, RestHandler.getRouter(UsersRestHandler), **settings)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    print "Tornado Server Starting.... : http://127.0.0.1:" + str(options.port)
    main()