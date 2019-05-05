#coding:utf-8
'''
给Excel表的每个单元格编号，并且定义为类属性
了解类属性引用
'''


class Global_var():
	
	# 通过类属性 定义表格的字段；引用方法 ：Global_var.id 这样可避免定义许多全局变量
	Id = '0'
	request_name = '1'
	url = '2'
	run = '3'
	request_way = '4'
	header = '5'
	cookie = '6'
	case_depend = '7'
	data_depend = '8'
	field_depend = '9'
	data = '10'
	expect = '11'
	result = '12'