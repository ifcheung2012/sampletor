import functools
from sqlalchemy.exc import IntegrityError
from tornado.web import HTTPError
from settings import globalsets

__author__ = 'Rubens Pinheiro'
__date__ = "03/07/13 22:26"


def REST(Service):
    class RestHandlerMeta(object):
        def __init__(self, cls):
            self.cls = cls
            self.Service = Service

        def __call__(self, application, request, **kwargs):
            obj = self.cls(application, request, **kwargs)
            super(self.cls, obj).__init__(application, request, **kwargs)

            setattr(obj, "_service", self.Service())
            return obj

    return RestHandlerMeta


def service(Entity):
    class ServiceMeta(object):
        def __init__(self, cls):
            self.cls = cls
            self.Entity = Entity
            globaldb = globalsets()
            self.session = globaldb.db

        def __call__(self, *args, **kwargs):
            obj = self.cls(*args, **kwargs)
            obj._meta = self
            obj._entity = self.Entity

            availableMethods = ['list', 'findById', 'create', 'save', 'delete']

            for method in availableMethods:
                if not hasattr(obj, method):
                    setattr(obj, method, getattr(self, method))

            return obj

        def commitChanges(self):
            try:
                self.session.commit()
                self.session.flush()

            except IntegrityError as e:
                self.session.rollback()
                raise e.message

        def list(self, limit=None, orderBy=None):
            record = self.session.query(Entity)
            if type(orderBy) is list:
                for order in orderBy:
                    record = record.order_by(order)

            elif orderBy is not None:
                record = record.order_by(orderBy)

            if limit:
                record = record.limit(limit)

            return record.all()

        def findById(self, id):
            return self.session.query(Entity).filter(Entity.id == id).first()

        def create(self, dict_attrs):
            obj = self.Entity()
            obj.from_dict(dict_attrs)
            self.session.add(obj)
            self.commitChanges()

        def save(self, dict_attrs):
            obj = self.Entity.get_by(id=dict_attrs["id"])
            obj.from_dict(dict_attrs)
            self.commitChanges()


        def delete(self, id):
            obj = self.Entity.get_by(id=id)
            obj.delete()
            self.commitChanges()

        def add_or_update_relation(self, relationattrname, relateEntities):
            if not hasattr(self.Entity, relationattrname):
                return
            try:
                for relation in relateEntities:
                    getattr(self.Entity, relationattrname).append(relation)
                self.session.commit()
            except Exception as e:
                self.session.rollback()
            finally:
                self.session.close()

    return ServiceMeta


def authenticated(method):
    """
    A default REST authenticate annotation
    If user isn't logged (using as reference the handler current_user),
    raises a 403 HTTP error. Doesn't redirects.
    """

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        # options = Options()
        # if options.custom_validation:
        #     if not options.custom_validation():
        #         raise HTTPError(403)
        #
        # elif not self.get_current_user():
        #     raise HTTPError(403)

        return method(self, *args, **kwargs)

    return wrapper


if __name__ == '__main__':
    pass