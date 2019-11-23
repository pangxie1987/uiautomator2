# -*- coding:utf-8 -*-

'''
协程greenlet学习
gevent可以实现协程，不过每次都要人为去指向下一个执行的协程，太过麻烦
推荐使用gevent
'''

import time
from greenlet import greenlet


def A():
    while 1:
        print('---A---')
        time.sleep(0.5)
        g2.switch()

def B():
    while 1:
        print('---B---')
        time.sleep(0.5)
        g1.switch()

g1 = greenlet(A)    # 创建协程g1
g2 = greenlet(B)

g1.switch()     # 跳转至协程g1