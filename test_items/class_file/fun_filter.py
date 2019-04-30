

# filter:保留结果为真的值
list1 = [1,0,1,1,0,0]
# r = filter(lambda x: True if x == 1 else False, list1)
r = filter(lambda x: x, list1)

print(list(r))