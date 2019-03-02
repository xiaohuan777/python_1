Python常用API

字符串

str.title()     修改字符串首字母为大写
str.upper()     字符串改写全部大写
str.lower()     字符串改写全部小写
str1 + str2     字符串拼接
\n              字符串中加\n换行
str.rstrip()    删除字符串末尾空白，不能删除原变量，需要将结果赋值给原变量
str.lstrip()    删除字符串开头空白，不能删除原变量，需要将结果赋值给原变量
str.strip()     同时删除两端空白，不能删除原变量，需要将结果赋值给原变量
str(23)        将非字符串转化成字符串 =》‘23’




列表    list1 = [1,'name',22,'age']

list1[0]                    返回下标为0的元素
list1[-1]                   返回最后一个元素
list1.append('sex')         在列表的最后添加一个'sex'元素
list2 = []                  创建空列表
list1.inset(0,'bike')       在列表的第0个位置插入‘bike’
list1[0] = 'lalala'         修改列表第0个元素为'lalala'
del list1[0]                删除列表中第0个元素，但该元素不能被使用，原列表不存在该元素
list1.pop()                 弹出（删除）列表中最后一个元素，且该元素还能继续被使用,last_one = list1.pop()原列表不存在该元素

list1.remove('age')         根据值删除元素，也可以接着使用它的值
list1.sort()                对列表进行正序永久性排序；数字从小到大，字符串按首字母排序
list1.sort(reverse=True)    对列表进行反序永久性排序
sorted(list1)               对列表进行临时正序排序，不改变原列表的顺序
sorted(reverse=True)        对列表进行临时反序排序，不改变原列表的顺序
reverse(list1)              反转列表元素的排列顺序，永久性的
len(list1)                  确定列表长度，其实就是数元素的个数



操作列表

range(1,5)                  生成从1~4这个序列，一般结合for语句使用
range(2,11,3)               指定步长为3
list(range(1,6))            将序列变成列表[1,2,3,4,5]
min(list2)                  找出数字列表的最小值
max(list2)                  找出数字列表的最大值
sum(list2)                  对数字列表求和
list[0:3]                   对列表切片，取出从第0~3位的元素，左闭右开
list[-3:]                   取出从倒数第3个到末尾的所有元素
copy_list1 = list1[:]       复制了一个list1的副本，两个列表相互独立
copy_list1 = list1          这样操作，两个列表都指向了同一个列表，其中一个列表发生改变另一个也会改变




元组 tuple

t1 = (20,3,7,10,67)

t1[0]                       通过下标去元素
t1[0] = 2                   ！！！！错误的写法，不能修改元组内部元素


### 字典:键值对
dict1 = {'name':'linda','age':22}

dict1['name']                   访问字典中的值
dict1['sex'] = 'femail'         添加键值对
dict2 = {}                      创建一个空字典
dict1['name'] = 'Rosa'          修改字典中的值
del dict1['sex']                删除键值对

#### 遍历键值对
for key,value in dict1.items():
    print('\nkey:'+ key)
    print('value:' + value)
