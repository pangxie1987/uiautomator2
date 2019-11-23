#! /usr/bin/env python
#coding=utf-8
#pywinauto自动化操作微信号
from WeiXin import WinChat
import sys

url = sys.argv[1]
groupid = sys.argv[2]
print('url====%s'%url)
print('groupid====%s'%groupid)
chat = WinChat(url,groupid)
chat.send_msg()
