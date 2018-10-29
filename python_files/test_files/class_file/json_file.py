
import json

# json 字符串必须是双引号，最外层用单引号，是因为里面用了双引号；
json_str = '{"name":"qiyue", "age": 18, "flag": false}'

# 反序列化
s1 = json.loads(json_str)
# print(type(s1))     返回字典dict
# print(s1)
# print(s1['name'])


# 序列化
s2 = [{"name": "qiyue", "age": 18}, {"flag": False, "gender": "male"}]
s3 = {'name': 'qiyu', 'age': 18}
j1 = json.dumps(s3, indent=2)
print(type(j1))
print(s1['name'])