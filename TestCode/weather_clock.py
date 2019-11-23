# -*- coding: UTF-8 -*-
'''
根据天气，智能闹钟
pip3 install pygame
pip3 install baidu-aip
'''

__blog__ = "https://blog.52itstyle.vip/"
import time
import random
import os
# import pygame
import requests
import json
import chardet
# from aip import ApiSpeech

def get_weather():
	'获取天气信息'
	# 上海区域id : 101020100
	# 查询区域信息，点击要查询的城市：http://www.weather.com.cn/forecast/
	url = "http://www.weather.com.cn/data/cityinfo/101020100.html"
	r = requests.get(url=url)
	weatherinfo = r.json()['weatherinfo']
	print(weatherinfo)
	cityinfo = weatherinfo['city']
	charset = chardet.detect(cityinfo.encode('utf-8'))
	print(charset)
	print(cityinfo.encode('utf-8').decode('utf-8'))
	

if __name__ == '__main__':
	get_weather()