
# reduce:做连续计算，在这里连续调用lambda

from functools import reduce

list1 = [1,2,3,4,5]

# r = reduce(lambda x,y: x + y*2, list1, 10)
r = reduce(lambda x,y: x*y, list1)
print(r)
