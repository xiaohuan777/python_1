import requests,json

def doPost(url, params, headers):
    response = requests.post(url, data=json.dumps(params), headers=headers)
    return json.loads(response.text)

def doGet(url, params, headers):
    response = requests.get(url, params=params, headers=headers)
    return json.loads(response.text)


