
# map

list1 = [1,2,3,4,5]
list2 = [2,3,4,5,6,7]

def square(x):
    return x * x

r = map(square, list1)
# print(list(r))

r1 = map(lambda x: x*x, list1)
# print(list(r1))

r2 = map(lambda x, y: x*x + y, list1,list2)
print(list(r2))
