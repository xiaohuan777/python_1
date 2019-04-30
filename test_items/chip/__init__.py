# 包的概念
# 包和模块是不会重复导入
# 避免循环导入

# 在用*导入时，只会导入__init__.py里的__all__中的内容
__all__ = ['c2']

# a = 'this is file'
# print(a)

import sys
import datetime
import os

class Main ():
    pass