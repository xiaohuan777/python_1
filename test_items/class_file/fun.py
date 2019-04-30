
from enum import Enum
from enum import IntEnum

class Vip(Enum):
    # 枚举：不能更改,一个枚举下不能有相同的标签
    YELLOW = 1
    # 若两个value相等，其实BLACK 是GREEN 的别名
    GREEN = 2
    BLACK = 2
    BLUE = 'str'

class Vip1(Enum):
    # 枚举,不能更改
    YELLOW = 1
    GREEN = 2   

yellow_value = Vip.YELLOW.value

# for v in Vip:
#     print(v)

# 枚举类型不支持大小比较

# result = Vip.GREEN == 2           False
# result = Vip.GREEN > Vip.YELLOW     报错，不能比较
# result = Vip.GREEN == Vip1.GREEN      False

# 将一个数字转换成枚举
a = 1
a_1 = Vip(a)

# IntEnum枚举类型，value只能是数字
class Vip3(IntEnum):
    # GREEN = 'srt'     会报错
    pass

print(a_1)