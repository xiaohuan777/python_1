import pytest

# 函数装饰函数
def wrapFun(func):
    def inner(*args):
        print('function name ' + func.__name__)
        r = func(*args)
        return r
    return inner

@wrapFun
def function_add(a, b):
    return a + b

print(function_add(1, 3))


# 函数装饰类
def wrapClass(cls):
    def inner(a):
        print('class.name =', cls.__name__)
        return cls(a)
    return inner

@wrapClass
class GetName():
    def __init__(self, name):
        self.name = name

    def fun(self):
        print('self.name=', self.name)

h = GetName('haha')
h.fun()