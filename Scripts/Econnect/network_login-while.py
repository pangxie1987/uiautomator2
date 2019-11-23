# -*- coding:utf-8 -*-
'''
上网权限认证 自动登录脚本
'''
import requests
import os
import json
import time

url = "http://192.168.2.254/ac_portal/login.php"
false = 'false'
true = 'true'

# 要执行的脚本
filepath = os.path.join(os.path.dirname(__file__), 'EConnect.vbs')

headers = {
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Referer":"http://192.168.2.254/ac_portal/20101201010101/pc.html?template=20101201010101&tabs=pwd&vlanid=0&_ID_=0&url=",
    "Cookie":"Sessionid=379667194-1; AUTHSESSID=3ff76688e7f9"
}

userinfo = {"opr":"pwdLogin","userName":"temp-liupb", "pwd":"liupb123456","rememberPwd":"0"}

def read(filename):
    '读取json文件'
    path = os.path.join(os.path.dirname(__file__), filename)
    datapath = os.path.abspath(path)
    try:
        with open(datapath, encoding='utf-8') as f:
            datas = json.load(f)
            # print(datas)
        return datas
    except FileNotFoundError:
        print('%s不存在，请检查'%filename)

def network():
    '判断当前网络情况'
    cmd = 'ping www.baidu.com'
    # 如果网络通则netnow==0
    net = os.system(cmd)
    return net

def vpntest():
    '判断VPN连接'
    cmd = 'ping 172.16.100.1'
    # 如果网络通则netnow==0
    net = os.system(cmd)
    return net

# def connect():
#     while True:
#         netnow = network()
#         if netnow:
#             print('*'*20+'网络不通，正在登录上网账号'+'*'*20)
#             r = requests.post(url=url, data=userinfo, headers=headers)
#             print(r.text)
#             if (eval(r.text)['success'] == 'false'):
#                 print('登录失败!,失败原因:',(r.text['msg']).encode('utf-8'))
#                 #break
#             elif (eval(r.text)['success'] == 'true'):
#                 print('*'*20+'登录成功!'+'*'*20)
#                 #break
#             else:
#                 print('登录异常，请检查！')
#                 #break
#         else:
#             print('*'*20+'网络连通正常'+'*'*20)
#         time.sleep(5)

def connect():
    while 1:
        print('*'*20+'网络守护，请勿关闭'+'*'*20)
        while network():
            print('='*20+'网络不通，正在登录上网账号'+'='*20)
            r = requests.post(url=url, data=userinfo, headers=headers)
            print(r.text)
        while vpntest():
            result = os.system(filepath)
        else:
            print('='*20+'网络连通正常'+'='*20)
        time.sleep(60)


if __name__ == '__main__':
    connect()
    input()

