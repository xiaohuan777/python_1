# coding:utf-8
'''
json文件读取
'''

import json
fire_path = r'/Users/xiaohuan/Desktop/face/xiaohuan/python/interface/excel_file/login.json'


class JsonRead():
    def __init__(self, file_name):
        self.file_name = file_name

    def get_read(self):
        fp = open(self.file_name, 'r', encoding='utf-8')            #单纯打开文件
        json_data = fp.read()                                       #读取文件
        fp.close()                                                  #关闭文件
        return json_data

if __name__ == '__main__':
    jp = JsonRead(fire_path)
    result = jp.get_read()
    print(type(result))
