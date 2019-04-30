
# 模拟switch

day = 6
switcher = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
    3: 'Tursday'
}

day_time = switcher.get(day, 'unknow')
# print(day_time)

# print(type(None))
# print(None == False)
print(bool(None))

class Test():
    def __len__(self):
        return True
    def __bool__(self):
        return True

print(len(Test()))