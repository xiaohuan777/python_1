from urllib import request, parse
import json

'''
data1 = {
    'username': 'xiaohuan',
    'password': 123456
}

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'
}

url1='http://127.0.0.1:8000/login/'
url2 = 'https://api.douban.com/v2/book/30163860'


# 模拟post请求
def send_post(url, data):
    data = parse.urlencode(data).encode('utf-8')
    # req = request.Request(url, headers=headers, data=data )
    # response = request.urlopen(req).read().decode('utf-8')
    response = request.urlopen(url, data=data).read().decode('utf-8')
    return response

# 模拟get请求
def send_get(url):
    res = request.urlopen(url)
    html = res.read().decode('utf-8')
    return html
'''

# get 和 post请求的封装
class RunMain():
    def __init__(self, url, header=None, data=None):
        self.url = url
        self.data =data
        self.header = header
        self.res = self.send_main()

    def send_main(self):
        
        # response = json.loads(response)
        # res = json.dumps(response, indent=2, sort_keys=True)

        if self.data:
            self.data = parse.urlencode(self.data).encode('utf-8')
            
        request_obj = request.Request(self.url, data=self.data, headers=self.header)
        response = request.urlopen(request_obj).read().decode('utf-8')
        return response

if __name__ == '__main__':
    url3 = 'https://www.wukong.com/user/?uid=62314569816'
    url4 = 'https://www.wukong.com/wenda/web/commit/postcomment/'
    headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    }

    data1 = {
        "text": "互撕很开心吧",
        "ansid": 6582501615322792195,
        "reply_to_comment_id": 0,
        "t": 1533098085183
    }

    r = RunMain(url4, header=headers, data=data1)
    print(r.res)

