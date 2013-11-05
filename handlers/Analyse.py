# -*- coding: utf-8 -*-

from handlers import Request_Handler
from models.repository import *
from models.model import *
from utils import JSONEncoder
import json
from tornado.web import authenticated
import tornado.web

class AnalyseHandler(Request_Handler):
    def get(self, *args, **kwargs):
        pass

        # import tornado.httpclient
        # client = tornado.httpclient.HTTPClient()
        # response = client.fetch("http://127.0.0.1:8008/long")
        # self.write(str(response.body))
        # self.finish()
        # client = tornado.httpclient.AsyncHTTPClient()
        # client.fetch("http://127.0.0.1:8008/long", callback=self.on_response)




if __name__ == '__main__':
    pass