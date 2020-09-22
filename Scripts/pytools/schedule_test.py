'''
python 轻量级的定时任务调度的库：schedule
https://www.cnblogs.com/anpengapple/p/8051923.html
pip install schedule
'''
import time
import schedule
import datetime
import threading

# =======================================基本用法演示=====================================
# def job():
#     print('I am working')

# # 设置定时时间
# # schedule.every(1).minutes.do(job)
# schedule.every(10).seconds.do(job)

# while True:
#     schedule.run_pending()

# =======================================单线程演示=====================================

def job1():
    print('I am Job1')
    time.sleep(2)
    print('Job1:', datetime.datetime.now())

def job2():
    print('I am Job2')
    time.sleep(2)
    print('Job2:', datetime.datetime.now()) 

def run_job():
    schedule.every(10).seconds.do(job1)
    schedule.every(10).seconds.do(job2)

    while True:
        schedule.run_pending()

# =======================================多线程演示=====================================

def job1():
    print('I am Job1')
    time.sleep(2)
    print('Job1:', datetime.datetime.now())

def job2():
    print('I am Job2')
    time.sleep(2)
    print('Job2:', datetime.datetime.now()) 

def job1_task():
    threading.Thread(target=job1).start()

def job2_task():
    threading.Thread(target=job2).start()

def run_jobtask():
    schedule.every(10).seconds.do(job1_task)
    schedule.every(10).seconds.do(job2_task)

    while True:
        schedule.run_pending()

if __name__ == '__main__':
    run_jobtask()