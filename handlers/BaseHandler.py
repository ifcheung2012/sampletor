from tornado.web import RequestHandler


class Request_Handler(RequestHandler):
    def param(self, name):
        return self.get_argument(name)

    def params(self, name):
        return self.get_arguments(name)

    def initialize(self):
        self.db = self.application.session

    def on_finish(self):
        self.db.close()

    def get_current_user(self):
        return self.get_secure_cookie("user")