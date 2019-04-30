# coding:utf-8
from multiprocessing import process
# 进程
def foo(i):
    print('this is a process', i)

for i in range(5):
    p = process(target=foo, args=(i,))
    p.start()

# 线程
import threading
def show(i):
    print('this is thread', i)

for i in range(5):
    t = threading.Thread(target=show, args=(i,))
    t.start()

# 协程
import gevent
def fun():
    print('start_foo')
    gevent.sleep(2)
    print('end_foo')

def bar():
    print('start_bar')
    gevent.sleep(0)
    print('end_bar')

gevent.joinall(
    [
        gevent.spawn(fun),
        gevent.spawn(bar),
    ]
)