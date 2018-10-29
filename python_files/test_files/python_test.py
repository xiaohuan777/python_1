
#闭包1
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
    
# f1,f2,f3= count()
# print f1(), f2(), f3()      #结果9,9,9


#闭包2
def count():
    fs = []  
    for i in range(1, 4):
        
        def f(j):
            def g():
                return j * j
            return g
        r = f(i)
        fs.append(r)
    return fs
   
f1, f2, f3 = count()
print (f1(), f2(), f3())          #结果1,4,9