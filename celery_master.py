# coding=utf-8


import time
from celery import Celery

broker = 'redis://127.0.0.1:6379/1'
backend = 'redis://127.0.0.1:6379/2'
app = Celery('celery_worker', broker=broker, backend=backend)


@app.task
def add(a, b):
    pass


flag = True
delta= 0
while delta < 10:
    print(app.control.ping(timeout=0.5))    # 发送ping包，看是否能访问目标地址
    result = add.delay(delta, delta)    # 发送具体的任务和值
    print ("ID: %s" % result.id)
    if result.failed():
        flag = False
    print ("Flag: %s" % flag)
    delta = delta + 1
    time.sleep(2)

    flag = False


