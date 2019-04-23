# coding:utf-8

‘’‘

’‘’

import json
import operator
class CaseAssert():
    def is_contain(self, str1, str2):
        if str1 in str2:
            return True
            print('true')
        else:
            return False
            print('false')

    # 把json字符串转化成字典比较
    def is_dict(self, dict_one, dict_two):
        if isinstance(dict_one, str):
            dict_one = json.loads(dict_one)
        if isinstance(dict_two, str):
            dict_two = json.loads(dict_two)
        result = operator.eq(dict_one, dict_two)
        return result


