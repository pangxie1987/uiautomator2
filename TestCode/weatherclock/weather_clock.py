# -*- coding: UTF-8 -*-
'''
https://blog.52itstyle.vip/archives/3952/
根据天气，智能闹钟
pip3 install pygame
pip3 install baidu-aip
'''

__blog__ = "https://blog.52itstyle.vip/"
import time
import random
import os
import pygame
import requests
import json
import chardet
from aip import AipSpeech

def get_weather(cityid):
	'获取天气信息'
	# 上海区域id : 101020100
	# 查询区域信息，点击要查询的城市：http://www.weather.com.cn/forecast/
	url = "http://www.weather.com.cn/data/cityinfo/{}.html".format(cityid)
	r = requests.get(url=url)
	print(r)
	weatherinfo = r.text.encode('ISO-8859-1').decode('utf-8')
	weatherinfo = json.loads(weatherinfo)
	weatherinfo = weatherinfo['weatherinfo']
	print(weatherinfo)
	weather = '今天{}的温度是{}到{}，天气{}'
	weather = weather.format(weatherinfo['city'], weatherinfo['temp1'], weatherinfo['temp2'], weatherinfo['weather'])
	if '雨' in weather:
		weather += '今天会下雨，带伞'
	du_say(weather)

def du_say(weather):
	'文字转语音'
	app_id = '15422825'
	api_key = 'DhXGtWHYMujMVZZGRI3a7rzb'
	secret_key = 'PbyUvTL31fImGthOOIP5ZbbtEOGwGOoT'
	client = AipSpeech(app_id, api_key, secret_key)
    # per 3是汉子 4是妹子，spd 是语速，vol 是音量
	result = client.synthesis(weather, 'zh', 1, {
        'vol': 5, 'per': 4, 'spd': 4
    })
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
	if not isinstance(result, dict):
		with open('weather.mp3', 'wb') as f:
			f.write(result)
	py_game_player('weather.mp3')

def py_game_player(file):
	'播放天气和音乐'
	pygame.mixer.init()
	print('播报天气')
	pygame.mixer.music.load(file)
	pygame.mixer.music.play(loops=1, start=0.0)
	print('播放音乐')
	while True:
		if pygame.mixer.music.get_busy() == 0:
			mp3 = str(random.randint(1, 2)) + ".mp3"
			# Linux 配置定时任务要设置绝对路径
			pygame.mixer.music.load(mp3)
			pygame.mixer.music.play(loops=1, start=0.0)
			break
	while True:
		if pygame.mixer.music.get_busy() == 0:
			print("播报完毕")
			break

if __name__ == '__main__':
	get_weather(101020100)