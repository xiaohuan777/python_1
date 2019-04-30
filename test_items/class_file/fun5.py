
# 命令式编程

# def,if else, for 
# 函数式编程
# map
# reduce
# filter
# lambda

# 装饰器
import time

def decorator(func):
    # **kw:关键字参数
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)
    return wrapper

@decorator
def f1(name1, name2, **kw):
    print('this is a function')
    print(kw)

f1('lisa', 'sdya', a=1, b=2, c='123')
