# -*- coding:utf-8 -*-

import logging
import os
import time
import socket
import sys

def loginit():
    '''
    #定义日志格式，并将日志同时向屏幕输出并写入文件
    '''
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    #datefmt='%a, %d %b %Y %H:%M:%S',
                    datefmt= '%Y-%m-%d %H:%M:%S',
                    filename='tushare.log',
                    filemode='w')
    #定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)


loginit()
logger=logging.getLogger(__name__)


if __name__ == '__main__':
    logger.info('start')