
def f1():
    result = 0
    def f2(x):
        # 解决在函数内部，result在等号左边被认为局部变量的问题
        nonlocal result
        result += x
        return result
    return f2

f = f1()
print(f(2))
print(f(3))
print(f(5))