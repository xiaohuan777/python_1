
# 方法和函数的区别
# 方法：设计层面；
# 函数：程序运行，过程式的一种称谓

from c1 import Student
class Child(Student):
    def __init__(self, name, age, gender, score):
        self.score = score
        super(Child, self).__init__(name, age, gender)

    def do_homework(self):
        print('english homework')


child1 = Child('zhansan', 23, 'nan', 20)
child1.do_homework()