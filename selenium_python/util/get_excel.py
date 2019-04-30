# coding:utf-8

import xlrd

class ExcelOperate():
    def __init__(self, file_path=None, sheet_id=0):
        if file_path:
            self.file_path = file_path
        else:
            self.file_path = r'/Users/xiaohuan/Desktop/face/xiaohuan/python/python_files/selenium_python/file/case1.xlsx'
        self.sheet_id = sheet_id
        self.data = self.get_excel()
        

    # 获取Excel的sheet
    def get_excel(self):
        table = xlrd.open_workbook(self.file_path)
        sheet = table.sheet_by_index(self.sheet_id)
        return sheet

    # 获取行数
    def get_lines(self):
        lines = self.data.nrows
        return lines

    # 获取单元格内容
    def get_cell(self, row, col):
        cell_value = self.data.cell(row, col).value
        return cell_value


    


