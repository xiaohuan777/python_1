from urllib import parse
from urllib import request
from urllib.request import urlopen

url = 'http://reg/hiabian.com/login/ajax_login'
data = {}
data['loginname'] = 'student'
data['password'] = '111111'
#对请求数据进行编码
data = parse.urlencode(data).encode('utf-8')
request = request.Request(url, data)
response = urlopen(request)
print(response.read())