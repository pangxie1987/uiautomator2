# -*- coding:utf-8 -*-
'''
获取当前季度的数据
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

quarter = datetime.now().month
print(quarter)
if quarter in [1,2,3]:
    nowquarter = 1
elif quarter in [4,5,6]:
    nowquarter = 2
elif quarter in [7,8,9]:
    nowquarter = 3
else:
    nowquarter = 4
print(nowquarter)
t1 = threading.Thread(target=reportdata, args=(nowyear, nowquarter), name='thread_reportdata')
t1.start()
t2 = threading.Thread(target=profitdata, args=(nowyear, nowquarter), name='thread_profitdata')
t2.start()
t3 = threading.Thread(target=operationdata, args=(nowyear, nowquarter), name='thread_operationdata')
t3.start()
t4 = threading.Thread(target=growthdata, args=(nowyear, nowquarter), name='thread_growthdata')
t4.start()
t5 = threading.Thread(target=deptpaydata, args=(nowyear, nowquarter), name='thread_deptpaydata')
t5.start()
t6 = threading.Thread(target=cashflowdata, args=(nowyear, nowquarter), name='thread_cashflowdata')
t6.start()

t7 = threading.Thread(target=getstocks, args=(), name='thread_getstocks')
t7.start()