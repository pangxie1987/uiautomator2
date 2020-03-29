'''
疫情增长趋势动态图--海外
参考：https://mp.weixin.qq.com/s?__biz=MzA5NDk4NDcwMw==&mid=2651389307&idx=2&sn=8bf8aaa4597a5336eea7c41648e3a2fd&chksm=8bba1debbccd94fd8dbb900f305fea43994d87eb87a28784d36396b38e3c95b4422e28d5b7c1&scene=126&sessionid=1585387515&key=61c257cd8ca493f98df98132aaea78ac250d81ca318e265ba4378db2ba2b7c0130cc5f705e8de9e1b9765f1510399d7f74ba6412606ee5c511539744cff4004b58db91a0a8355c933249e38b1ec94ede&ascene=1&uin=MjU1MjExMjgxNw%3D%3D&devicetype=Windows+10&version=62080079&lang=zh_CN&exportkey=AdygyIyfJk%2BGq445lx3GLQg%3D&pass_ticket=2JV9zXhMUETFb4ql5Qovi41a52QJ4Pjyx71z%2FQJYay3trikwEgsCd62NcWUqSpel
疫情数据来源：https://news.qq.com/zt2020/page/feiyan.htm?from=timeline&isappinstalled=0#/global
获取数据

'''

import requests
import json
import xlwt
import xlrd

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}

base_url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign"			# 海外国家信息
url = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist'		# 海外当日发布信息
url_country = "https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list"	# 每个国家的历史信息
all_data = {}	# 保存所以国家疫情数据

filename = '1.xls'


def get_today_data():
	'获取当日海外疫情数据'
	r = requests.get(url=url)
	print(r.text)
	for data in r.json()['data']:
		print(data['name'], data['confirm'])

def sortdate(today):
	'将日期02.01转成2020年2月1日'
	list1 = today.split('.')
	print(list1)
	today = '2020年'+list1[0].replace('0', '')+'月'+list1[1]+'日'
	return today

def get_his_data():
	'获得各个国家历史数据'
	r = requests.get(url=base_url, headers=headers)
	foreignList = json.loads(r.json()['data'])['foreignList']	# 国家列表
	for infos in foreignList:
		res = requests.post(url=url_country, data={'country': infos['name']}, headers=headers)
		data = res.json()['data']
		all_data[infos['name']] = data
# print(all_data)

def wirte_excel():
	'将疫情数据写入Excel'
	get_his_data()
	workbook = xlwt.Workbook(encoding='utf-8')	# 创建一个workbook
	worksheet = workbook.add_sheet('issuedata')	# 创建一个sheet
	for i in all_data.keys():
		print('i======',i)
		wb = xlrd.open_workbook(filename)
		tablesheet = wb.sheets()[0]
		k = tablesheet.nrows
		# print(all_data[i])
		for t, j in enumerate(all_data[i]):
			print('t,j====',t, j)
			worksheet.write(k+t, 0, i)

			worksheet.write(k+t, 1, sortdate(str(j['date'])))
			worksheet.write(k+t, 2, j['confirm'])
		workbook.save(filename)

if __name__ == '__main__':
	wirte_excel()