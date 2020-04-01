from aiwd.common.PublicIp import PublicIp
from aiwd.util.HttpRequests import doGet


def getHotQuestions():
    url = PublicIp.jfzt + '/rjhy-ai-gateway/api/v1/hot/questions'
    params = {}
    headers = {}
    resp_str = doGet(url, params, headers)
    return resp_str


if __name__ == '__main__':
    res1 = getHotQuestions()
    print(res1)
    print(type(res1))
