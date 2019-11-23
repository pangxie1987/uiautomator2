#-*- coding:utf-8 -*-
'''
python md5 加密
'''

import json
import requests
import hashlib
import base64
import datetime

url = "http://192.168.3.142:8777/sso/api/login"
loginname = '15854393739'
passwd = '123456'
sign = {'url':'login','loginName':"15854393739","password":'123456'}
header = {'Content-Type':"application/json"}

def md5sec():
    '对passwd进行MD5加密'
    md = hashlib.md5()
    md.update(passwd.encode())
    passmd5 =md.hexdigest()

    datas = {
        "loginName":"test001",
        "password":passmd5,
        "sign":"url=login;loginName=15854393739;password=123456"
    }

    print(datas)

    r = requests.post(url=url, json=datas, headers=header)
    print(r.text)

def base64sec():
    'base64的加密解密'
    s = '我是字符串'
    a = base64.b64encode(s.encode('utf-8'))
    b = base64.b64decode(a)
    print(a)
    print(b.decode('utf-8'))

#base64sec()
def decode_base64(data):
    'base64解码'
    missing_padding=4-len(data)%4

    if missing_padding:

        data += b'='*missing_padding

    print(base64.decodestring(data)) 

# reqcode = 'MjAxODEyMjMxMDEwMTNhZG1pbg%3D%3D'

# decode_base64(reqcode.encode('utf-8'))

def encode_base64(data):
    'base64编码'
    data = base64.b64encode(data)
    print(data)
    return data

nowtime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
# encode_base64((nowtime+'admin').encode('utf-8'))

decode_base64(b'MTM0OTk5OTk5OTktbG9naW50ZXN0')