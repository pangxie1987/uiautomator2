# -*- coding:utf-8 -*-
'''
VPN登录守护
'''
import os
from time import sleep

# 要执行的脚本
filepath = os.path.join(os.path.dirname(__file__), 'EConnect.vbs')

def netconnect():
    '判断当前网络情况'
    cmd = 'ping 172.16.100.20'
    # 如果ping正常，则net==0，否则非0
    net = os.system(cmd)
    print(net)
    return net


def VPNconnect():
    '启动VPN连接'
    while True:
        netnow = netconnect()
        if netnow:
            print('**********内网不通，正在登录VPN**********')
            # 如果内网不通，则调用脚本登录VPN
            result = os.system(filepath)
            sleep(3)
        else:
            print('**********内网连接正常**********')
            sleep(5)
            continue

if __name__ == '__main__':

    VPNconnect()
