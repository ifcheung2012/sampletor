# -*- coding: utf-8 -*-
from tornado.escape import json_encode, json_decode
from datetime import datetime, date, timedelta
from sqlalchemy.orm.collections import InstrumentedList
import json
from models import DeclarativeBase


class JSONEncoder(json.JSONEncoder):
    """ This encoder will serialize all entities that have a to_dict
    method by calling that method and serializing the result. """

    def encode(self, obj):
        if hasattr(obj, 'to_dict'):
            obj = obj.to_dict()
        return super(JSONEncoder, self).encode(obj)

    def objToDict(self, obj):
        attrs, attrvalues = dir(obj), obj.__dict__
        return dict([(attr, attrvalues[attr]) for attr in attrs if not isinstance(getattr(obj, attr), InstrumentedList) \
                                                                       and not attr.startswith('_') and attr != 'metadata'])

    def default(self, obj):
        if hasattr(obj, 'as_dict'):
            return obj.as_dict()
        elif isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, DeclarativeBase):
            return self.objToDict(obj)
        elif hasattr(obj, 'to_dict'):
            return obj.to_dict()
        raise TypeError("%r is not JSON serializable" % obj)


if __name__ == '__main__':
    pass
#todo related source code:  http://elixir.ematia.de/trac/browser/elixir/tags/0.7.0/elixir/entity.py#L1054