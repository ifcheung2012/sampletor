# -*- coding: utf-8 -*-
__author__ = 'ifcheung'
from celery import Celery

celery = Celery('hello', broker='amqp://guest@localhost//')

@celery.task
def hello():
    return 'hello world'


if __name__ == '__main__':
    pass