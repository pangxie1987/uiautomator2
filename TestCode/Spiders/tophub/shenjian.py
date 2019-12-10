'''
免费API
神箭手云 https://www.shenjian.io/
'''

import requests

url = 'https://api.shenjian.io/'
datas = {'appid': '1'}

def market_data():
	'大盘指数行情查询API'
	datas['appid'] = '7c52cdb011754816d21467577d0ecdc5'
	r = requests.get(url=url, params=datas)
	print(r.text)

def tikets():
	'股票实时行情查询API'
	datas['appid'] = '3c05d21ae2768192efa61782a49f6790'
	r = requests.get(url=url, params=datas)
	print(r.text)


if __name__ == '__main__':
	tikets()
