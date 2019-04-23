## Python常用API

### 字符串

1. str.title()     修改字符串首字母为大写
2. str.upper()     字符串改写全部大写
3. str.lower()     字符串改写全部小写
4. str1 + str2     字符串拼接
5. \n              字符串中加\n换行
6. str.rstrip()    删除字符串末尾空白，不能删除原变量，需要将结果赋值给原变量
7. str.lstrip()    删除字符串开头空白，不能删除原变量，需要将结果赋值给原变量
8. str.strip()     同时删除两端空白，不能删除原变量，需要将结果赋值给原变量
9. str(23)        将非字符串转化成字符串 =》‘23’




### 列表    list1 = [1,'name',22,'age']

1. list1[0]                    返回下标为0的元素
2. list1[-1]                   返回最后一个元素
3. list1.append('sex')         在列表的最后添加一个'sex'元素
4. list2 = []                  创建空列表
5. list1.inset(0,'bike')       在列表的第0个位置插入‘bike’
6. list1[0] = 'lalala'         修改列表第0个元素为'lalala'
7. del list1[0]                删除列表中第0个元素，但该元素不能被使用，原列表不存在该元素
8. list1.pop()                 弹出（删除）列表中最后一个元素，且该元素还能继续被使用, last_one = list1.pop()原列表不存在该元素

10. list1.remove('age')         根据值删除元素，也可以接着使用它的值
11. list1.sort()                对列表进行正序永久性排序；数字从小到大，字符串按首字母排序
12. list1.sort(reverse=True)    对列表进行反序永久性排序
13. sorted(list1)               对列表进行临时正序排序，不改变原列表的顺序
14. sorted(reverse=True)        对列表进行临时反序排序，不改变原列表的顺序
15. reverse(list1)              反转列表元素的排列顺序，永久性的
16. len(list1)                  确定列表长度，其实就是数元素的个数


### 操作列表
1. range(1,5)                  生成从1~4这个序列，一般结合for语句使用
2. range(2,11,3)               指定步长为3
3. list(range(1,6))            将序列变成列表[1,2,3,4,5]
4. min(list2)                  找出数字列表的最小值
5. max(list2)                  找出数字列表的最大值
6. sum(list2)                  对数字列表求和
7. list[0:3]                   对列表切片，取出从第0~3位的元素，左闭右开
8. list[-3:]                   取出从倒数第3个到末尾的所有元素
9. copy_list1 = list1[:]       复制了一个list1的副本，两个列表相互独立
10. copy_list1 = list1          这样操作，两个列表都指向了同一个列表，其中一个列表发生改变另一个也会改变




### 元组 tuple

1. t1 = (20,3,7,10,67)

2. t1[0]                       通过下标去元素
3. t1[0] = 2                   ！！！！错误的写法，不能修改元组内部元素


### if语句

1. ==                          相等号
2. !=                          不等号
3. and,or                      使用and,or检查多个条件
4. in                          判断特定的值是否已包含在列表中
5. if-elif-else
6. if-else


### 字典:键值对

   dict1 = {'name':'linda','age':22}

1. dict1['name']                   访问字典中的值
2. dict1['sex'] = 'femail'         添加键值对
3. dict2 = {}                      创建一个空字典
4. dict1['name'] = 'Rosa'          修改字典中的值
5. del dict1['sex']                删除键值对

   #### 遍历字典中键值对
```
for key,value in dict1.items():
    print('\nkey:'+ key)
    print('value:' + value)
```

   #### 遍历字典中所有的键
```
for key1 in dict1.keys():
    print(key1.title())
```

   #### 按顺序遍历字典中所有的键
```
for key1 in sorted(dict1.keys()):
    print(key1)
```

   #### 遍历字典中所有的值
```
for val in dict1.values():
    print(val)
```

   ### set()对重复列表去重
```
for val in set(dict1.values()):
    print(val)
```

## 嵌套：将一系列字典存储在列表中，或将列表作为值存储在字典中

### 在列表中存储字典

```
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
   print(alien)
```

### 在字典中存储列表
```
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese']
}
```

### 在字典中存储字典
```
users = {
   'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
        },
   'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
        },
}
```

## 用户输入 input 和 while 循环

### input()

```
name = input("Please enter your name: ")
print("Hello, " + name + "!")

***********

Please enter your name: Eric
Hello, Eric!
```

#### 用 int() 来获取数值输入

#### 求模运算
   4 % 3          将两个数相除并返回余数


### while 循环
   使用 break 退出循环
   使用 continue 继续循环

   ```
   current_number = 0
   while current_number < 10:
      current_number += 1
      if current_number % 2 == 0:
         continue
      print(current_number)
   ```


## 使用 while 循环来处理列表和字典

### 删除包含特定值的所有列表元素   while + remove()

```
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while 'cat' in pets:
   pets.remove('cat')
print(pets)
```


## 函数

   ```
   def describe_pet(animal_type, pet_name):
      pass

   ***
   键值对实参
   describe_pet(animal_type='hamster', pet_name='harry')

   ***
   实参
   describe_pet('hamster', 'harry')
   ****

   默认值参数
   def describe_pet(pet_name, animal_type='dog'):
      pass

   describe_pet(pet_name='willie')
   ```

   
### 返回值
