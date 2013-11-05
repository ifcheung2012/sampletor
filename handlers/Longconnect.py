# -*- coding: utf-8 -*-
__author__ = 'ifcheung'
from handlers import Request_Handler

class LongConnectHandler(Request_Handler):
    import tornado.web

    @tornado.web.asynchronous
    def get(self):
        import tornado.httpclient
        client = tornado.httpclient.HTTPClient()
        response = client.fetch("http://127.0.0.1:8008/long")
        self.write(str(response.body))
        self.finish()
        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch("http://127.0.0.1:8008/long", callback=self.on_response)

    def on_response(self, response):
        body = response.body
        res = str(body)
        self.write(res)
        self.finish()

class longhandler(Request_Handler):
    def get(self):
        import time

        time.sleep(1)
        self.write("ok 4 seconds ago!")
        self.finish()


if __name__ == '__main__':
    pass