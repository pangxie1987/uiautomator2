# -*- coding:utf-8 -*-
'''
psutil 系统监控
'''
import psutil

print(psutil.cpu_count())   #CPU逻辑数量
print(psutil.cpu_count(logical=False))  #CPU物理核数

# print(psutil.net_connections()) #获取网络连接信息

print(psutil.pids())