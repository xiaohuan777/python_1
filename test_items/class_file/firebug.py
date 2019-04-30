

# 正则表达式：一个特殊的字符序列，一个字符串是否与我们所设定的这样字符序列，相匹配
# 快速检索文本，实现一些替换文本的操作

# 1.检查一串数字是否是电话号码
# 2.检测一个字符串是否符合email
# 3.把一个文本里指定的单词替换为另外一个单词

# 元字符：/d：匹配数字
#  /D：匹配非数字
# 概括字符集
#  /w：匹配单词字符
#  /W：匹配非单词字符
#  /s：匹配空白字符(&,\r,\h)
# 普通字符：python
# 匹配*之前的字符0次或者多次
#+:匹配1次或者无限多次
# ？:匹配0次或者1次
# 边界匹配
# .匹配除换行符\n之外的其他所有字符

import re

a = 'c|python|java|java01pythonn2s  cript\n23456'
s = 'acc, afc, dfg, cdk, cfk'
r = re.findall('java', a)
r2 = re.findall('\d', a)
# 匹配中间是c或者f
r3 = re.findall('a[cf]c', s)
# 匹配中间是c到f

r4 = re.findall('a[c-f]c', s)


# 数量词，匹配连续多个字符

r5 = re.findall('[a-z]{3}', s)
# 贪婪和非贪婪，python倾向贪婪

r6 = re.findall('[a-z]{3,6}', a)
# 非贪婪
r7 = re.findall('[a-z]{3,6}?', a)

r8 = re.findall('python*', a)
r9 = re.findall('python+', a)
r10 = re.findall('python?', a)

qq = '1019023084'
# 完全匹配（边界匹配），从字符开头和结尾来匹配
r11 = re.findall('^\d{4,8}$', qq)

# 忽略大小写
we = 'fhksHKdsjkJDJf'
r12 = re.findall('j', we, re.I)

# 替换
s2 = 'python123riwoeipy2346thon'
r13 = re.sub('python', 'ok', s2)
# 替换所有匹配项
r13 = re.sub('python', 'ok', s2, 0)
# 只替换一个
r13 = re.sub('python', 'ok', s2, 1)

# 自定义正则匹配函数
def convert(value):
    # 传入的value是一个对象
    matched = value.group()
    return '!!' + matched + '!!'

r14 = re.sub('python', convert, s2)
# match从第一个字符比较，若第一个不匹配，后面有匹配项也不会再去一一匹配
r15 = re.match('\d', s2)
# search 会去匹配整个字符串，直到匹配到第一个字符即可终止
r16 = re.search('\d', s2)

# 爬虫截取中间数据
s3 = 'life is short, i use python, i love python'
# r17 = re.findall('life(.*)python', s3)
r17 = re.search('life(.*)python(.*)python', s3)

r18 = r17.group(0,1,2)
r19 = r17.groups(0)

print(bool(None))
# print(r19)

