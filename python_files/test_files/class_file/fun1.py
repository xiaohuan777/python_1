
# 函数式编程
# 闭包：函数 + 环境变量。在f1函数内部引用外部函数f2变量，且该变量不能在f1内部重新赋值！

def fun1():
    a = 5
    def fun2(x):
        # a = 10    此时a =10 会被认为是一个局部变量。若加上这句就不是闭包！！
        return a *x
    return fun2
a = 3
f = fun1()
print(f(2))


