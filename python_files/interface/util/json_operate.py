# coding:utf-8
import json
fire_path = 'D:\python_files\interface\excel_file\login.json'


class JsonRead():
    def __init__(self, file_name):
        self.file_name = file_name

    def get_read(self):
        fp = open(self.file_name, 'r', encoding='utf-8')
        json_data = fp.read()
        fp.close()
        return json_data

if __name__ == '__main__':
    jp = JsonRead(fire_path)
    result = jp.get_read()
    print(type(result))
