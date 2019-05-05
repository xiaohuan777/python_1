# coding:utf-8
'''
将Excel表中的字段与实际请求参数关联起来
'''
import sys
sys.path.append('/Users/xiaohuan/Desktop/face/xiaohuan/python/interface')


from util.excel_operate import OperationExcel
from data_file.data_config import Global_var
from util.json_operate import JsonRead
import xlrd
from util.sqldb import OperationMysql

class GetData():
    def __init__(self):
        self.get_excel = OperationExcel()

    # 获取Excel行数，即case执行的个数
    def get_case_len(self):
        return self.get_excel.get_lines()

    # 获取是否执行
    def get_is_run(self, row):
        flag = None
        col = int(Global_var.run)
        cell_val = self.get_excel.get_cell_value(row, col)
        if cell_val == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 是否携带header
    def is_header(self, row):
        headers = {
            'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        col = int(Global_var.header)
        header_val = self.get_excel.get_cell_value(row, col)
        if header_val == 'yes':
            return Global_var.header
        else:
            return headers

    # 获取请求方式
    def get_request_method(self, row):
        col = int(Global_var.request_way)
        request_val = self.get_excel.get_cell_value(row, col)
        return request_val

    # 获取URL
    def get_url(self, row):
        col = int(Global_var.url)
        url = self.get_excel.get_cell_value(row, col)
        return url

    # 获取请求数据
    def get_requst_data(self, row):
        col = int(Global_var.data)
        request_data = self.get_excel.get_cell_value(row, col)
        if request_data == '':
            return None
        return request_data

    # 通过关键字获取json_data
    def get_json_data(self, row):
        fp = self.get_requst_data(row)
        json_opera = JsonRead(fp)
        request_data = json_opera.get_read()
        return request_data

    # 获取预期结果
    def get_expect_data(self, row):
        col = int(Global_var.expect)
        expect = self.get_excel.get_cell_value(row, col)
        if expect == '':
            return None
        return expect

    # 通过sql获取预期结果
    def get_expect_sql(self, row):
        op_mysql = OperationMysql()
        sql = self.get_expect_data(row)
        result = op_mysql.search_one(sql)
        return result

    # 写入数据
    def write_data(self, row, value):
        col = int(Global_var.result)
        result = self.get_excel.write_value(row, col, value)
        return result

    # 获取被依赖case的key
    def get_depend_key(self, row):
        col = int(Global_var.data_depend)
        key = self.get_excel.get_cell_value(row, col)
        if key == '':
            return None
        return key

    # 获取是否有case依赖
    def is_depend(self, row):
        col = int(Global_var.case_depend)
        depend_value = self.get_excel.get_cell_value(row, col)
        return depend_value

    # 获取依赖case的key值
    def get_depend_field(self, row):
        col = int(Global_var.field_depend)
        depend_field = self.get_excel.get_cell_value(row, col)
        return depend_field

    # 是否携带cookie
    def is_cookie(self, row):
        col = int(Global_var.cookie)
        cookie = self.get_excel.get_cell_value(row, col)
        if cookie == '':
            return None
        return cookie

    


if __name__ == "__main__":
    get_datas = GetData()
    print(GetData.is_cookie(1,2))