# -*- coding: utf-8 -*-
from tornado.web import RequestHandler,HTTPError
from tornado.escape import json_decode,json_encode
from utils.serializer import JSONEncoder

class RestHandler(RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(RestHandler, self).__init__(application, request, **kwargs)
        self.serializer = JSONEncoder()
        self.set_header("Content-type", "application/json")

    def filterJsonContent(self):
        content_type = self.request.headers.get("Content-Type", "")

        if content_type.startswith("application/json"):
            return json_decode(self.request.body)

        return None

    def get(self, id, **kwargs):
        if id != "":
            id = json_decode(id)
            result = self._service.findById(id)
            if result is None:
                return json_encode(None)
            else:
                self.write(self.serializer.encode([result]))
        else:
            results = self._service.list()
            self.write(self.serializer.encode(results))

    def post(self, dict_args=None, **kwargs):
        params = self.filterJsonContent()
        if params is None:
            params = {k: ''.join(v) for k,v in self.request.arguments.iteritems()}

        try:
            self._service.create(params)

            self.write(json_encode({}))

        except Exception as e:
            self.set_status(400)
            self.finish(json_encode({'error': True, 'message': e.message}))

    def put(self, dict_args=None, **kwargs):
        params = self.filterJsonContent()
        if params is None:
            params = {k: ''.join(v) for k,v in self.request.arguments.iteritems()}

        if params is None:
            params = dict_args
        try:
            if not hasattr(params, 'id'):
                raise HTTPError(400)

            self._service.save(params)
            self.write(json_encode({}))

        except Exception as e:
            self.set_status(400)
            self.finish(json_encode({'error': True, 'message': e.message}))

    def delete(self, id, **kwargs):
        if id != "":
            id = json_decode(id)

            try:
                self._service.delete(id)
                self.write(json_encode({}))

            except Exception as e:
                self.set_status(400)
                self.finish(json_encode({'error': True, 'message': e.message}))

    @staticmethod
    def getRouter(handler):
        return [(r'/%s/?(?P<id>[0-9]*)' % handler.Service.Entity.__name__.lower(), handler)]