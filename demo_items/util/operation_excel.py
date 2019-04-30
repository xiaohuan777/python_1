#coding:utf-8
import xlrd
from xlutils.copy import copy
class OperationExcel:
	def __init__(self,file_name=None,sheet_id=None):
		if file_name:
			self.file_name = file_name
			self.sheet_id = sheet_id	
		else:
			self.file_name = r'/Users/xiaohuan/Desktop/face/xiaohuan/python/python_files/interface/excel_file/case2.xlsx'
			self.sheet_id = 0
		self.data = self.get_data()

	#获取工作表sheets的内容，通过索引获取
	def get_data(self):
		data = xlrd.open_workbook(self.file_name)	#打开Excel文件
		tables = data.sheets()[self.sheet_id]		#获取工作表，这里是获取了第一张
		return tables

	#获取单元格的行数
	def get_lines(self):
		tables = self.data
		return tables.nrows

	#获取某一个单元格的内容
	def get_cell_value(self,row,col):
		return self.data.cell_value(row,col)

	#写入数据
	def write_value(self,row,col,value):
		'''
		写入excel数据
		row,col,value
		'''
		read_data = xlrd.open_workbook(self.file_name)		#打开Excel文件
		write_data = copy(read_data)						#复制一张工作表
		sheet_data = write_data.get_sheet(0)
		sheet_data.write(row,col,value)
		write_data.save(self.file_name)


	#目的：根据caseid 找到对应行的内容（事先知道所属列）
	def get_rows_data(self,case_id):
		row_num = self.get_row_num(case_id)
		rows_data = self.get_row_values(row_num)
		return rows_data

	# 1.获取整列的值（是一个数组）
	def get_cols_data(self,col_id=None):
		if col_id != None:
			cols = self.data.col_values(col_id)			# .row_values(i) 获取整行的值
		else:
			cols = self.data.col_values(0)
		return cols


	# 2.根据caseid找到对应的行号
	def get_row_num(self,case_id):
		num = 0
		clols_data = self.get_cols_data()
		for col_data in clols_data:
			if case_id in col_data:
				return num
			num = num+1


	# 3.根据行号，找到该行的内容
	def get_row_values(self,row):
		tables = self.data
		row_data = tables.row_values(row)			# 获取整行内容
		return row_data

	


if __name__ == '__main__':
	opers = OperationExcel()
	print (opers.get_cell_value(1,2))