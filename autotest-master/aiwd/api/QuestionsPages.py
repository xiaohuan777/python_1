from aiwd.common.PublicIp import PublicIp
from aiwd.util.HttpRequests import doGet


def getQuestionsPages(**kw):
    url = PublicIp.jfzt + '/rjhy-ai-gateway/api/v1/questions/pages'
    #样式：{"isHot": isHot,"isKeyword": isKeyword,"isExample": isExample,"pageSize": pageSize,"pageNo": pageNo,"category": category}
    params = kw
    headers = {}
    resp_str = doGet(url, params, headers)
    return resp_str


if __name__ == '__main__':
    res1 = getQuestionsPages(isHot=1)
    print(res1)
    print(type(res1))
