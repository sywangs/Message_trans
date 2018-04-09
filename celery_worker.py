# coding=utf-8

import time
from celery import Celery

broker = 'redis://127.0.0.1:6379/1'
backend = 'redis://127.0.0.1:6379/2'
app = Celery('celery_worker', broker=broker, backend=backend)


@app.task
def add(a, b):
    print ('Start task' + str(a))
    time.sleep(3)
    print ('Finish task' + str(a))
    return a + b