from aiwd.common.PublicIp import PublicIp
from aiwd.util.HttpRequests import doGet


def getQueryAiInfotByAppCode(isHot="", isKeyword="", isExample="", pageSize="", pageNo="", category=""):
    url = PublicIp.jfzt + '/rjhy-ai-gateway/api/v1/aiInfo/ios/queryAiInfotByAppCode'
    params = {}
    headers = {"appcode": "com.rjhy.uranus"}   # 九方智投APP
    resp_str = doGet(url, params, headers)
    return resp_str


if __name__ == '__main__':
    res1 = getQueryAiInfotByAppCode()
    print(res1)
    print(type(res1))
