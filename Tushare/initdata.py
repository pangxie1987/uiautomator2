# -*- coding:utf-8 -*-
'''
初始化所有数据（1989-至今）
'''
import threading
from datetime import datetime
from stockbasic import getstocks
from stockbasic import reportdata
from stockbasic import profitdata
from stockbasic import operationdata
from stockbasic import growthdata
from stockbasic import deptpaydata
from stockbasic import cashflowdata

nowyear = datetime.now().year
t7 = threading.Thread(target=getstocks, args=(), name='thread_getstocks')
t7.start()
# 初始化执行一次，获取1989年之后所有数据
for year in range(1989, nowyear+1):  #获取从1989年之后的数据
    for quarter in [1,2,3,4]:
        t1 = threading.Thread(target=reportdata, args=(year, quarter), name='thread_reportdata')
        t1.start()
        t2 = threading.Thread(target=profitdata, args=(year, quarter), name='thread_profitdata')
        t2.start()
        t3 = threading.Thread(target=operationdata, args=(year, quarter), name='thread_operationdata')
        t3.start()
        t4 = threading.Thread(target=growthdata, args=(year, quarter), name='thread_growthdata')
        t4.start()
        t5 = threading.Thread(target=deptpaydata, args=(year, quarter), name='thread_deptpaydata')
        t5.start()
        t6 = threading.Thread(target=cashflowdata, args=(year, quarter), name='thread_cashflowdata')
        t6.start()