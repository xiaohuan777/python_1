# 面向对象
# 有意义的面向对象的代码
# 类=面向对象
# 实例化
# 类的基本作用：封装
# 面向对象的三大特性：继承性，封装性，多态性

class Student():
# 类变量
    sum = 0
    name = 'afd'
    count = 0

    # 构造函数
    def __init__(self, name, age, gender):
        # 实例变量
        self.name = name
        self.age = age
        self.__gender = gender
        self.__class__.count += 1
        print('学生总数为：' + str(self.__class__.count))

        # print(name)     这里取得是构造函数的形参
        # print(Student.name)     取得是类变量
        # print(self.__class__.name)    取得是类变量  

    # 实例方法
    def do_homework(self):
        self.do_english_homework()
        print('homework')

    def do_english_homework(self):
        pass

    def marking(self, score):
        if score < 0:
            return '不能打负分！'
        self.score = score
        print(self.name + '本学期分数：' + str(self.score))
   
    # 装饰器
    # 类方法
    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)

    # 静态方法
    @staticmethod
    def add(x, y):
        # return x + y
        print('静态方法')

    # 私有方法，前面加双下划线
    def __weight(self):
        print('这是私有方法')


s1 = Student('jack', 22, 47)
# s2 = Student('lisy', 22)
# s3 = Student('lucy', 22)


# 动态给实例创建私有变量
s1.__score = 2      
print(s1.__dict__)

# s3.marking(59)
# result = s2.marking(-1)
# print(result)



# 类方法调用
# Student.plus_sum()

# 静态方法调用
# Student.add(1,2)
# s1.add(1,2)

# s2 = Student('raok',22)
# print(s1.name)    
# print(s2.name)  

# print(s1.__dict__)      打印当前实例所有变量成员
    
# print(Student.name)
    

