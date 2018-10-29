# coding:utf-8

import sys
sys.path.append(r'D:\python_files\selenium_python')
from util.get_excel import ExcelOperate
from util.driver import ActionDriver

class TestCase():
    def run_main(self):
        self.handle_excel = ExcelOperate()
        case_lines =self.handle_excel.get_lines()
        for i in range(1, case_lines):
            is_run = self.handle_excel.get_cell(i,2)
            if is_run =='yes':
                method = self.handle_excel.get_cell(i,3)
                handle_value = self.handle_excel.get_cell(i,4)
                send_value = self.handle_excel.get_cell(i,5)
                self.run_method(method,handle_value)

    def run_method(self, method, handle):
        action_method = ActionDriver()
        action_function = getattr(action_method, method)
        action_function(handle)



if __name__ == '__main__':
    test = TestCase()
    test.run_main()