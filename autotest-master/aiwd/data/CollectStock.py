import tushare as ts
import pandas as np

pro = ts.pro_api('d98c11f98bc8cb2ce6712eda20e2be85b91189f16ce70e2790c2e1f6')
#list_status上市状态： L上市 D退市 P暂停上市
data = pro.query('stock_basic', exchange='', list_status='L', fields='symbol,name')

symbol = data.to_csv('stock.txt', index=False, header=False)

print(type(data))
print(data)