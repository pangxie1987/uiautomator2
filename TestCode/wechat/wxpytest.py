'''
wxpy基于itchat，使用了 Web 微信的通讯协议，，
通过大量接口优化提升了模块的易用性，并进行丰富的功能扩展。
实现了微信登录、收发消息、搜索好友、数据统计等功能。
'''
'''
https://bbs.51cto.com/thread-1501477-1.html
解决认证问题
'''

from wxpy import *
# from pyecharts import Pie
from pyecharts.charts import Pie

bot = Bot(cache_path=True)  #扫码登陆，cache_path=True缓存，不用每次都登陆
friends = bot.friends()

attr = ['男朋友', '女朋友']
value = [0, 0]
for friend in friends:
    if friend.sex == 1:
        value[0] +=1
    elif friend.sex == 2:
        value[1] += 1

pie = Pie('螃蟹的朋友们')
pie.add("", attr, value, is_label_show=True)
pie.render('sex.html')