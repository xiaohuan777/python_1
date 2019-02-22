# encoding:'utf-8'
import xlrd
import xlwt
from xlutils.copy import copy

class OperationExcel():
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '/Users/xiaohuan/Desktop/face/xiaohuan/python/python_files/interface/excel_file/case1.xls'
            self.sheet_id = 0
        self.data = self.get_data()

    # 获取sheet内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        table = data.sheet_by_index(self.sheet_id)
        return table

    # 获取单元格行数
    def get_lines(self):
        lines = self.data.nrows
        return lines
    
    # 获取单元格的内容
    def get_cell_value(self, row, col):
        cell_value = self.data.cell(row, col).value
        return cell_value

    # 写入数据
    def write_value(self, row, col, value):
        table = xlrd.open_workbook(self.file_name)
        table_copy = copy(table)
        sheet_copy = table_copy.get_sheet(0)
        sheet_copy.write(row, col, value)
        table_copy.save(self.file_name)

        
    # 根据对应case_id，找到对应行的内容
    def get_row_data(self, case_id):
        row_num = self.get_row_num(case_id)
        row_data = self.get_row_value(row_num)
        return row_data

    # 根据对应的case_id，找到对应的行号
    def get_row_num(self, case_id):
        num = 0
        cols_data = self.get_col_data(0)
        for col_data in cols_data:
            if case_id == col_data:
                return num
            num += 1

    # 根据行号找到行内容
    def get_row_value(self, row):
        table = self.get_data()
        row_data = table.row_values(row)
        return row_data

    # 获取某一列内容
    def get_col_data(self, col):
        table = self.get_data()
        col_data = table.col_values(col)
        return col_data



if __name__ == '__main__':
    opera = OperationExcel()
    opera.write_value(1, 11, 'ceshi')
    
    

