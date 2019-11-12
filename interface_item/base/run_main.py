# coding: utf-8

from urllib import request, parse
import json
from http import cookiejar

'''
# 这是python2.0的方法

class RunMethod():
    # post请求
    def post_main(self, url, data, header=None):
        data = parse.urlencode(data).encode('utf-8')
        request_obj = request.Request(url, data=)
        res = request.urlopen(request_data).read().decode('utf-8')
        res = json.loads(res)
        return res

    # get请求
    def get_main(self, url, data=None, header=None):
        if header != None:
        res = request.urlopen(url, data, header).read().decode('utf-8')
        else:
            res = request.urlopen(url, data).read().decode('utf-8')
        return res

    # 入口请求判断
    def run_main(self, url, method, data=None, header=None):
        if method == 'post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return res
'''

# 现改用python3.0方法
class RunMethod():
    def __init__(self):
        self.cookie_file = r'/Users/xiaohuan/Desktop/face/xiaohuan/python/interface/excel_file/cookie.txt'

    def run_main(self, url, header, data=None, cookies=None):      
        # response = json.loads(response)
        # res = json.dumps(response, indent=2, sort_keys=True)
        if data:
            data = parse.urlencode(data).encode('utf-8') 
        request_obj = request.Request(url, data=data, headers=header)

        if cookies == 'write':
            cookie_jar = cookiejar.MozillaCookieJar(self.cookie_file)
            handler = request.HTTPCookieProcessor(cookie_jar)
            opener = request.build_opener(handler)
            response = opener.open(request_obj).read().decode('utf-8')
            cookie_jar.save(ignore_discard=True, ignore_expires=True)
        elif cookies == 'yes':
            cookie_jar = cookiejar.MozillaCookieJar()
            cookie_jar.load(self.cookie_file, ignore_discard=True, ignore_expires=True)
            handler = request.HTTPCookieProcessor(cookie_jar)
            opener = request.build_opener(handler)
            response = opener.open(request_obj).read().decode('utf-8')
        else:
            response = request.urlopen(request_obj).read().decode('utf-8')

        return response

