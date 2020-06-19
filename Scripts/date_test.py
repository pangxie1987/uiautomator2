# # -*- coding:utf-8 -*- 
# '''
# 判断当天星期几
# '''
import datetime
import time

d = datetime.datetime.now()
print(d)
print(d.weekday())  #0-周一，6-周日

nowtime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
print(nowtime)

print(datetime.datetime.now().hour)

print(type(time.strftime("%H%I%M%S")))

d = datetime.datetime.now()
print(d.weekday())  #0-周一，6-周日
nowtime = time.strftime("%H%I%M%S")
print(nowtime)
if d.weekday() not in (5, 6):
    if (nowtime>'090000' and nowtime <'170000'):
        print('不需要发送手机验证码')

    else:
        print('发送手机验证码')
        
else:
    print('发送手机验证码')
