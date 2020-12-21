'''
@Description: 
@Autor: liu
@Date: 2019-03-20 15:48:38
@LastEditors: liu
@LastEditTime: 2020-12-21 09:01:19
'''
# -*- coding:utf-8 -*-
'''
上网权限认证 自动登录脚本
'''
import requests
import os
import json

# url = "http://192.168.255.254/ac_portal/login.php"
false = 'false'
true = 'true'
# datas = {"opr":"pwdLogin","userName":"temp-liupb", "pwd":"liupb123456","rememberPwd":"0"}

headers = {
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    # "Referer":"http://192.168.2.254/ac_portal/20101201010101/pc.html?template=20101201010101&tabs=pwd&vlanid=0&_ID_=0&url=",
    "Cookie":"Sessionid=379667194-1; AUTHSESSID=3ff76688e7f9"
}

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

def connect():
    '''
    办公网登陆
    '''
    info = read('userinfo.json')
    netnow = network()
    while True:
        if netnow:
            print('*'*20+'网络不通，正在登录上网账号'+'*'*20)
            r = requests.post(url=info['url']+'/ac_portal/login.php', data=info['userinfo'], headers=headers)
            print(r.text)
            if (eval(r.text)['success'] == 'false'):
                print('登录失败!,失败原因:',(eval(r.text['msg']).encode('utf-8')))
                break
            elif (eval(r.text)['success'] == 'true'):
                print('*'*20+'登录成功!'+'*'*20)
                break
            else:
                print('登录异常，请检查！')
                break
        else:
            print('*'*20+'网络正常!'+'*'*20)
            break

if __name__ == '__main__':
    # read("userinfo.json")
    connect()
    input()

