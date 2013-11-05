# -*- coding: utf-8 -*-
from sqlalchemy.orm import scoped_session, sessionmaker
from models.model import engine


def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class globalsets:
    def __init__(self):
        self.db = scoped_session(sessionmaker(bind=engine))

    @property
    def session(self):
        return self.db

if __name__ == '__main__':
    pass