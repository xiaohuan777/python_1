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




