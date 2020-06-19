# -*- coding:utf-8 -*-

'''
自动协程gevent学习
gevent每次遇到io操作，需要耗时等待时，会自动跳到下一个协程继续执行
https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868328689835ecd883d910145dfa8227b539725e5ed000
'''

# ----------Test1----------
# import time
# import gevent

# def A():
#     while 1:
#         print('-------A--------')
#         gevent.sleep(1) # 用来模拟一个耗时操作

# def B():
#     while 1:
#         print('-------B--------')
#         gevent.sleep(0.5) # 每当碰到耗时操作，会自动跳转到其他协程

# g1 = gevent.spawn(A) # 创建一个协程
# g2 = gevent.spawn(B)
# g1.join()   #等待协程执行结束
# g2.join()

# ----------Test2----------
# from gevent import monkey; monkey.patch_all()
# import gevent
# from urllib.request import urlopen

# def f(url):
#     print('GET:%s' % url)
#     resp = urlopen(url)
#     data = resp.read()
#     print('%d bytes received from %s' % (len(data), url))

# gevent.joinall([
#     gevent.spawn(f, 'https://www.python.org/'),
#     gevent.spawn(f, 'https://www.baidu.com/'),
#     gevent.spawn(f, 'https://github.com/'),
# ])

# # ----------Test3----------
# import gevent
# import socket

# urls = ['www.baidu.com', 'www.gevent.org', 'www.python.org']
# jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]

# gevent.joinall(jobs, timeout=5)

# print ([job.value for job in jobs])

# # ----------Test4----------
from gevent import monkey; monkey.patch_all()
import gevent
import socket

urls = ['www.baidu.com', 'www.gevent.org', 'www.python.org']
jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
gevent.joinall(jobs, timeout=5)

print ([job.value for job in jobs])