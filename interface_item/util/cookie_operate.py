# coding:utf-8
from urllib import request,parse
from http import cookiejar
import json

url1 = 'http://mp.eastday.com/login'
url2 = 'http://mp.eastday.com/getuserinfo'
data = {
    "mobile": "13764236295",
    "password": "A1164821471",
    "authcode": "",
    "freelogin": 0,
}

headers = {
    'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

# 以变量的形式存储cookie
cookie_jar = cookiejar.CookieJar()
handler = request.HTTPCookieProcessor(cookie_jar)
opener = request.build_opener(handler)


data = parse.urlencode(data).encode('utf-8')
request_data = request.Request(url1,data=data, headers=headers)
res1 = opener.open(request_data).read().decode('utf-8')
for item in cookie_jar:
    print(item.name + ':' + item.value)

request2 = request.Request(url2, headers=headers)
res2 = opener.open(request2).read().decode('utf-8')
print(res2)

