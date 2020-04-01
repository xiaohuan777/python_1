from aiwd.common.PublicIp import PublicIp
from aiwd.util.HttpRequests import doPost


def postChat(question, context=""):
    url = PublicIp.jfzt + '/rjhy-ai-gateway/api/v1/chat'
    params = {"question": question,
              "context": context
              }
    headers = {"Content-Type": "application/json"}
    resp_str = doPost(url, params, headers)
    return resp_str


if __name__ == '__main__':
    res1 = postChat('张江高科属于什么地区')
    print(res1)
    print(type(res1))
