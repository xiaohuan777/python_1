# coding:utf-8

import sys
sys.path.append('/Users/xiaohuan/Desktop/face/xiaohuan/python/interface')

from data_file.get_data import GetData
from base.run_main import RunMethod
from case_assert import CaseAssert
from data_file.depend_data import DependData
from util.send_email import SendEmail
import json

class RunTest():
    def __init__(self):
        self.data = GetData()           
        self.run_method = RunMethod()
        self.assert_method = CaseAssert()
        self.send_email = SendEmail()
    
    # 执行主入口
    def go_run(self):
        res = None
        rows_count = self.data.get_case_len()
        pass_count = []
        fail_count = []
        for i in range(5, rows_count):
            url = self.data.get_url(i)
            # method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            # expect = self.data.get_expect_data(i)
            expect = self.data.get_expect_sql(i)
            request_data = self.data.get_requst_data(i)
            header = self.data.is_header(i)
            case_id = self.data.is_depend(i)
            is_cookie = self.data.is_cookie(i)
            
            # 判断请求数据是否为空，不为空就要json转换
            if request_data != None:
                request_data = self.data.get_json_data(i)
                # request_data被加载进来是一个json字符串，故要转换成字典。否则拼接post请求数据时失败
                request_data = json.loads(request_data)

            # 判断是否可执行
            if is_run:
                data_depend = DependData(case_id);

                # 判断是否有case依赖
                if case_id != '':
                    depend_value = data_depend.get_depend_keyValue(i)
                    depend_key = self.data.get_depend_field(i)
                    request_data[depend_key] = depend_value
                res = self.run_method.run_main(url, header=header, data=request_data, cookies=is_cookie)

                # 根据断言，判断case是否通过
                if self.assert_method.is_dict(expect, res):
                    self.data.write_data(i, 'pass')
                    pass_count.append(i)
                else:
                    self.data.write_data(i, res)
                    fail_count.append(i)
        # self.send_email.main(pass_count, fail_count)
        return res

if __name__ == '__main__':
    run = RunTest()
    run.go_run()