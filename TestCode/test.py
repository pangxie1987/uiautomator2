__blog__ = "https://blog.52itstyle.vip/"
import time
import random
import os
# import pygame
import requests
import json
# from aip import ApiSpeech
import urllib

url = 'http://www.weather.com.cn/data/cityinfo/101120201.html'
obj = urllib.request.urlopen(url)
data_b = obj.read()
print(data_b)
data_s = data_b.decode('utf-8')
data_dict = json.loads(data_s)
rt = data_dict['weatherinfo']
print(rt)