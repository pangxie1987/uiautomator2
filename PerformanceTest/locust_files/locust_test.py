# -*- coding:utf-8 -*-
'''
locust是一个可扩展的，分布式的，性能测试的吗，开源的，Python编写的性能测试框架
pip install locustio
pip install pyzmq  分布式运行locust
'''

from locust import HttpLocust, TaskSet

def login(l):
    l.client.post("/login", {"username":"ellen_key", "password":"education"})

def logout(l):
    l.client.post("/logout", {"username":'ellen_key', "password":"education"})
    
def index(l):
    l.client.get("/")

def profile(l):
    l.client.get("/profile")

class UserBehavior(TaskSet):
    tasks = {index:2, profile:1}

    def on_start(self):
        login(self)

    def on_stop(self):
        logout(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000