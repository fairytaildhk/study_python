import base64
import json

import requests


def doPost(url, params):
    headers = {'Content-Type': "application/json", }
    response = requests.request("POST", url, data=json.dumps(params), headers=headers)
    status_code = response.status_code
    if status_code == 200:
        return json.loads(str(response.content, "utf-8"))
    else:
        raise Exception("接口请求失败\n" + "状态码：" + str(status_code) + "\n" + response.text)


def doPost_str(url, params):
    headers = {'Content-Type': "application/json", }
    response = requests.request("POST", url, data=json.dumps(params), headers=headers)
    status_code = response.status_code
    if status_code == 200:
        return response.text
    else:
        raise Exception("接口请求失败\n" + "状态码：" + str(status_code) + "\n" + response.text)


def doPostBase64Decode(url, params):
    headers = {'Content-Type': "application/json", }
    response_base64 = requests.post(url, data=json.dumps(params), headers=headers)
    status_code = response_base64.status_code
    if status_code == 200:
        response = str(base64.b64decode(response_base64.content), 'utf-8')
        return json.loads(response)
    else:
        raise Exception("接口请求失败\n" + "状态码：" + str(status_code) + "\n" + response_base64.text)


def doPostBase64Decode_str(url, params):
    headers = {'Content-Type': "application/json", }
    response_base64 = requests.post(url, data=json.dumps(params), headers=headers)
    status_code = response_base64.status_code
    if status_code == 200:
        return str(base64.b64decode(response_base64.content), 'utf-8')
    else:
        raise Exception("接口请求失败\n" + "状态码：" + str(status_code) + "\n" + response_base64.text)
