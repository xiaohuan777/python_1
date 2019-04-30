# coding:utf-8

from util.excel_operate import OperationExcel
from data_file.get_data import GetData
from base.run_main import RunMethod
from jsonpath_rw import jsonpath,parse
import json

class DependData():
    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel()
        self.data = GetData()
        self.run_method = RunMethod()

    # 通过case_id，获取该整行的内容
    def get_depend_case(self):
        case_data = self.opera_excel.get_row_data(self.case_id)
        return case_data

    # 执行被依赖case，获取结果
    def run_depend(self):
        row_num = self.opera_excel.get_row_num(self.case_id)
        url = self.data.get_url(row_num)
        is_run = self.data.get_is_run(row_num)
        expect = self.data.get_expect_data(row_num)
        request_data = self.data.get_requst_data(row_num)
        header = self.data.is_header(row_num)
        is_cookie = self.data.is_cookie(row_num)

        if request_data != None:
            request_data = self.data.get_json_data(row_num)
            # request_data被加载进来是一个json字符串，故要转换成字典。否则拼接post请求数据时失败
            request_data = json.loads(request_data)

        res = self.run_method.run_main(url, header=header, data=request_data, cookies=is_cookie)
        return res

    # 根据被依赖case的key，去获取响应value值
    def get_depend_keyValue(self, row):
        depend_key = self.data.get_depend_key(row)
        depend_res = self.run_depend()
        depend_res = json.loads(depend_res)
        json_exe = parse(depend_key)
        madle = json_exe.find(depend_res)
        depend_value = [math.value for math in madle][0]
        return depend_value

if __name__ == '__main__':
    path = r'/Users/xiaohuan/Desktop/face/xiaohuan/python/python_files/interface/excel_file/autoresponse.json'
    fp = open(path, 'r', encoding='utf-8')
    json_obj = fp.read()
    json_obj = json.loads(json_obj)
    # json_obj = {"err_no": 0,"student":[{"male":176,"female":162},{"male":174,"female":159}]}
    # jsonpath_expr = parse("student[*].male")
    jsonpath_expr = parse("data[*].dongtai_list[0].dongtai_cell.dongtai.base.answer.ansid")
    male = jsonpath_expr.find(json_obj)
    val = [match.value for match in male][0]
    print(val,type(val))

    