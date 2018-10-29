

result = 0
def fun1 (step):
    # 解决result被认为局部变量问题
    global result
    result += step
    return result

print(fun1(2))
print(fun1(3))
print(fun1(5))