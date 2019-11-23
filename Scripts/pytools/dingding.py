'''
python对接dingding
https://open-doc.dingtalk.com/microapp/serverapi2/eev437
https://open-doc.dingtalk.com/microapp/dev/epcw4e#a-nameamimdwa%E8%8E%B7%E5%8F%96%E4%BC%9A%E8%AF%9D%E4%BF%A1%E6%81%AF
'''

import requests
from urllib3 import encode_multipart_formdata
import os

appkey = 'ding7a05491d2e914134'
appsecret='OYFbUI-ZtYLrokWJMnMfX4jsubSZwTyJivSgIKjY0FBw16GXLhWMZyRvrStRC3HZ'
url_key='https://oapi.dingtalk.com/gettoken?appkey=%s&appsecret=%s'%(appkey, appsecret)
url_send='https://oapi.dingtalk.com/topapi/message/corpconversation/asyncsend_v2?access_token='

def get_access_token():
    '获取授权码，一般有效时间为200s'
    r = requests.get(url=url_key)
    access_token = r.json()['access_token']
    print(access_token)
    return access_token

def dingding_send():
    '发送工作通知消息'
    send_data = {
        "agent_id":"20248674",
        "userid_list":"18516292278",
        "to_all_user":"false",
        "msg":{
                "msgtype":"text",
                "text":
                {
                    "content":"消息内容"
                }
        }
    }
    url = url_send+get_access_token()
    r = requests.post(url=url, json=send_data)
    print(r.text)

def cretegroup():
    '创建群组'
    url = "https://oapi.dingtalk.com/chat/create?access_token="
    url = url+get_access_token()
    data = {
        "name": "lpb-test",
        "owner": "18516292278",
        "useridlist": ["18516292278","15221839787"]
    }
    r = requests.post(url=url, json=data )
    print(r.text)

def sendgroup():
    '发送群消息'
    url = "https://oapi.dingtalk.com/chat/send?access_token="
    url = url+get_access_token()
    data = {
        "chatid": "chat5ba2a9b25537d0995289d2d69dd4f6ac",
        "msgtype": "text",
        "text": {
        "content": "张三的请假申请"
                }
            }
    r = requests.post(url=url, json=data )
    print(r.text)

def uploadfile():
    '媒体文件上传接口'
    url = "https://oapi.dingtalk.com/media/upload?type=image&access_token="
    url = url+get_access_token()
    path = os.path.dirname(__file__)
    print(path)
    fileid = os.path.join(path, "123.png")
    filedata = {"filename":'1',"filelength":"1", "content-type":"multipart/form-data"}
    filedata['filename'] = (open(fileid,'rb'))
    # encode_data = encode_multipart_formdata(filedata)
    # #print(encode_data)
    # filedata = encode_data[0]
    # header = {'Content-Type':"1"}
    # header['Content-Type'] = encode_data[1]
    # print(header)
    # data = {
    #     "type":"image",
    #     "media":filedata
    # }
    r = requests.post(url=url, data={'media':filedata})
    print(r.text)

def sendgroupfile():
    '发送群消息-图片'
    url = "https://oapi.dingtalk.com/chat/send?access_token="
    url = url+get_access_token()
    data = {
        "chatid": "chat5ba2a9b25537d0995289d2d69dd4f6ac",
        "msgtype": "file",
        "file":{
             "media_id": "@lAzPDeC2uMmjZ_nOCfeqYc471H3G"
        }
            }
    r = requests.post(url=url, json=data)
    print(r.text)

if __name__ == '__main__':
    # dingding_send()
    # cretegroup()
    # get_access_token()
    # sendgroup()
    uploadfile()
    # sendgroupfile()