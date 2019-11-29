'''
爬取各个站点热门话题
https://mp.weixin.qq.com/s/WmZXm6rsMjN2wcVD6E5jQg
今日热榜：https://tophub.today/
'''
import time
import requests
import re
import json
from bs4 import BeautifulSoup

def zhihu():
	'知乎热榜信息'
	zhihu_url = 'https://www.zhihu.com/billboard'
	headers = {"user-agent":"", "Cookie":""}
	r = requests.get(url=zhihu_url, headers=headers)
	webcontent = r.text
	soup = BeautifulSoup(webcontent, "html.parser")
	script_text = soup.find("script", id="js-initialData").get_text()
	rule = r'"hotList":(.*?),"guestFeeds"'
	result = re.findall(rule, script_text)

	temp = result[0].replace("false", "False").replace("true", "True")

	hot_list = eval(temp)
	print(hot_list)

def weibo():
	'微博热榜信息'
	weibo_url = 'https://s.weibo.com/top/summary'
	headers = {"user-agent":"", "Cookie":""}
	r = requests.get(url=weibo_url, headers=headers)
	webcontent = r.text
	# print(webcontent)
	soup = BeautifulSoup(webcontent, "html.parser")
	index_list = soup.find_all("td", class_="td-01")
	title_list = soup.find_all("td", class_="td-02")
	level_list = soup.find_all("td", class_="td-03")

	topic_list = []

	for i in range(len(index_list)):
		item_index = index_list[i].get_text(strip = True)
		if item_index == "":
			item_index = "0"
		item_title = title_list[i].a.get_text(strip = True)
		if title_list[i].span:
			item_mark = title_list[i].span.get_text(strip = True)
		else:
			item_mark = "置顶"
		item_level = level_list[i].get_text(strip = True)
		topic_list.append({"index":item_index,"title":item_title,"mark":item_mark,"level":item_level,"link":f"https://s.weibo.com/weibo?q=%23{item_title}%23&Refer=top"})
		print(topic_list)
	print(topic_list)

def weibo2():
	'微博实时热点https://weibo.com/a/hot/realtime'
	weibo_url = 'https://weibo.com/a/hot/'
	useragent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
	headers = {
    'Cookie': "UOR=www.tax.sh.gov.cn,widget.weibo.com,www.tax.sh.gov.cn; Ugrow-G0=e1a5a1aae05361d646241e28c550f987; SUB=_2AkMqi6V7f8NxqwJRmP4QzGjkbI5xyQDEieKc11SgJRMxHRl-yT83qlAvtRB6AQuLlB-ZYP-ll-JHTqCXhOdpEA_WBWk6; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFSMZ8KoSBJkicW8B_TYMx9; YF-V5-G0=7a7738669dbd9095bf06898e71d6256d; WBStorage=42212210b087ca50|undefined",
    'cache-control': "no-cache",
    'Postman-Token': "bcfcdd01-137a-4ced-b529-b6c06dc54394"
    }
	r = requests.get(url=weibo_url+"realtime", headers=headers)
	webcontent = r.text
	# print(webcontent)
	soup = BeautifulSoup(webcontent, "html.parser")
	index_list = soup.find("div", class_="UG_contents")
	#print(index_list)
	content1 = index_list.find_all("h3", class_="list_title_b")
	title_list = []
	# print(content1)
	
	for content in content1:
		article = {}
		i = content.find("a", href = True)
		# print(i)
		title = i.text
		link = weibo_url + i.get('href')
		print(title, link)
		print('=='*10)
		article['title'] = title
		article['link'] = link
		title_list.append(article)
	print(title_list)


def kr36():
	'36kr24小时热榜'
	kr36_url = 'https://36kr.com'
	headers = {"user-agent":"", "Cookie":""}
	r = requests.get(url=kr36_url, headers=headers)
	webcontent = r.text
	# print(webcontent)
	soup = BeautifulSoup(webcontent, "html.parser")
	index_list = soup.find("div", class_="hotlist-main")
	#print(index_list)
	content1 = index_list.find_all("a", class_="hotlist-item-toptwo-title")
	content2 = index_list.find_all("a", class_="hotlist-item-other-title")
	#print(content1)
	# print(content2)
	title_list = []
	
	for i in content1:
		article = {}
		link = i.get('href')
		article['title'] = i.text
		article['link'] = kr36_url+link
		title_list.append(article)
	for i in content2:
		article = {}
		link = i.get('href')
		article['title'] = i.text
		article['link'] = kr36_url+link
		title_list.append(article)
	print(title_list)

def baidu():
	'百度实时热点http://top.baidu.com/?vit=1&fr=topnews'
	baidu_url = 'http://top.baidu.com/?vit=1&fr=topnews'
	headers = {"user-agent":"", "Cookie":""}
	r = requests.get(url=baidu_url, headers=headers)
	webcontent = r.text
	# print(webcontent)
	soup = BeautifulSoup(webcontent, "html.parser")
	index_list = soup.find("ul", id="hot-list")
	#print(index_list)
	content1 = index_list.find_all("a", class_="list-title")
	title_list = []
	for i in content1:
		#print(i)
		article = {}
		link = i.get('href')
		title = i.text
		article['title'] = title
		article['link'] = link
		print(article)
		title_list.append(article)

def sspai():
	'少数派https://sspai.com'
	sspai_url = 'https://sspai.com'
	headers = {"user-agent":"", "Cookie":""}
	r = requests.get(url=sspai_url, headers=headers)
	webcontent = r.text
	# print(webcontent)
	soup = BeautifulSoup(webcontent, "html.parser")
	index_list = soup.find("div", class_="articleCard-box")
	# print(index_list)
	content1 = index_list.find_all("a", class_="pc_card")
	#print(content1)
	title_list = []
	for i in content1:
		# print(i)
		# print('=='*10)
		article = {}
		link = i.get('href')
		title = i.text
		article['title'] = title
		article['link'] = sspai_url+link
		print(article)
		title_list.append(article)
	print(title_list)

def huxiu():
	'虎嗅资讯https://www.huxiu.com/article'
	huxiu_url = 'https://www.huxiu.com'
	headers = {"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", "Cookie":""}
	r = requests.get(url=huxiu_url+'/article', headers=headers)
	webcontent = r.text
	#print(webcontent)
	soup = BeautifulSoup(webcontent, "html.parser")
	index_list = soup.find("div", class_="app-main")
	#print(index_list)
	content1 = index_list.find_all("a", href=True)
	# print(content1)
	title_list = []
	for i in content1:
		# print(i)
		# print('=='*10)
		article = {}
		link = i.get('href')
		title = i.text
		article['title'] = title
		article['link'] = link
		# print(article)
		title_list.append(article)
	print(title_list)

def huxiu2():
	'虎嗅资讯：请求下拉列表的数据'
	huxiu_url = 'https://www-api.huxiu.com/v1/article/list'
	headers = {
		"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
		"Cookie":""}

	# cookie = "SERVERID=f60b85c1ffd425d843469f623dc2b612|1574384041|1574383607"
	cookie = "SERVERID=f60b85c1ffd425d843469f623dc2b612|{0}|{1}"	#根据时间戳判断下拉获取的数据
	datas = {'pagesize':10, 'recommend_time':''}
	while 1:
		nowtime = time.time()
		dateline = nowtime - 2
		cookie = cookie.format(nowtime, dateline)
		headers['Cookie'] = cookie
		print(nowtime)
		datas['recommend_time'] = nowtime
		print(headers)
		r = requests.get(url=huxiu_url, params=datas, headers=headers)
		webcontent = r.json()
		print(webcontent['data'])
		nextpage = webcontent['data']['is_have_next_page']
		last_dateline = webcontent['data']['last_dateline']
		if nextpage:
			print('继续下一页')
			time.sleep(2)
		else:
			break
		print('请求完成')

def ithome():
	'IT之家https://m.ithome.com/rankm/'
	ithome_url = 'https://m.ithome.com/rankm/'
	headers = {"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", "Cookie":""}
	r = requests.get(url=ithome_url, headers=headers)
	webcontent = r.text
	#print(webcontent)
	soup = BeautifulSoup(webcontent, "html.parser")
	rank = soup.find("div", class_="rank")	# 排行榜
	# print(day_rank)
	rank_box = rank.find_all("div", class_="rank-box")
	# print(rank_box)
	for content in rank_box:
		# print(content)
		#print('=='*20)
		article = content.find_all("div", class_="placeholder one-img-plc")
		#print(article)
		for news in article:
			# print('*'*20,news)
			title_content = news.find('p', class_="plc-title")
			title = title_content.text
			link_content = news.find('a', href=True)
			link = link_content.get('href')
			print(title, link)
	title_list = []

def jandan():
	'煎蛋首页内容http://jandan.net'
	jiandan_url = 'http://jandan.net'
	headers = {
		"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
		"Cookie":""}
	r = requests.get(url=jiandan_url, headers=headers)
	webcontent = r.text
	# print(webcontent)
	soup = BeautifulSoup(webcontent, "html.parser")
	rank = soup.find("div", id="content")	# 首页信息
	# print(rank)
	content = rank.find_all("div", class_="indexs")
	for news in content:
		
		news = news.find('a', href = True)
		# print(news)
		# print('=='*10)
		title = news.text
		link = news.get('href')
		print(title, link)

def douban():
	'豆瓣新片榜单https://movie.douban.com/chart'
	douban_url = 'https://movie.douban.com/chart'
	headers = {
		"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
		"Cookie":""}
	r = requests.get(url=douban_url, headers=headers)
	webcontent = r.text
	#print(webcontent)
	soup = BeautifulSoup(webcontent, "html.parser")
	rank = soup.find("div", class_="indent")	# 首页信息
	#print(rank)
	content = rank.find_all("a", class_="")
	# print(content)
	for news in content:
		
		# news = news.find('a', href = True)
		# print(news)
		# print('=='*10)
		title = news.text
		link = news.get('href')
		print(title, link)

def pojie52():
	'吾爱破解https://www.52pojie.cn/forum.php?mod=guide&view=hot'
	pojie_url = 'https://www.52pojie.cn/'
	headers = {
		"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
		"Cookie":""}
	datas = {'mod':'guide', 'view':'hot'}
	r = requests.get(url=pojie_url+'forum.php', params=datas, headers=headers)
	webcontent = r.text
	# print(webcontent)
	soup = BeautifulSoup(webcontent, "html.parser")
	rank = soup.find("div", id="threadlist")	# 首页信息
	# print(rank)
	content = rank.find_all("th", class_="common")
	# print(content)
	for news in content:
		# print(news)
		news = news.find('a', href = True)
		title = news.text
		link = pojie_url+news.get('href')
		print(title, link)
		print('=='*20)

def tieba():
	'贴吧热议榜http://tieba.baidu.com/hottopic/browse/topicList'
	tieba_url = 'http://tieba.baidu.com/hottopic/browse/topicList'
	headers = {
		"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
		"Cookie":""}
	datas = {'res_type':'1', 'red_tag':'v3370729790'}
	r = requests.get(url=tieba_url, params=datas, headers=headers)
	webcontent = r.text
	#print(webcontent)
	soup = BeautifulSoup(webcontent, "html.parser")
	rank = soup.find("ul", class_="topic-top-list")
	# print(rank)
	content = rank.find_all("div", class_="topic-name")
	for news in content:
		#print(news)
		title = news.text
		link = news.a.attrs['href']
		print(title, link)
		print('=='*20)

def v2ex():
	'V2EX	https://www.v2ex.com/'
	vex_url = 'https://www.v2ex.com'
	headers = {
		"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
		"Cookie":""}
	r = requests.get(url=vex_url,  headers=headers)
	webcontent = r.text
	#print(webcontent)
	soup = BeautifulSoup(webcontent, "html.parser")
	rank = soup.find("div", id="TopicsHot")
	# print(rank)
	content = rank.find_all("span", class_="item_hot_topic_title")
	for news in content:
		print(news)
		
		title = news.text
		link = vex_url + news.a.attrs['href']
		print(title, link)
		print('=='*20)

def tianya():
	'天涯	https://bbs.tianya.cn/'
	tianya_url = 'https://bbs.tianya.cn/api'
	headers = {
		"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
		"Cookie":""}
	datas = {
		'method':'bbs.ice.getHotArticleList',
		'params.pageSize':'15',	#每次请求的数量（太长了r.text解析不了）
		'params.pageNum':'1',
		'var':'apiData',
		'_r': 0.13344051421726943,
		'_': 1574681639524
	}
	r = requests.get(url=tianya_url, params=datas,  headers=headers)
	#webcontent = json.loads(r.text)
	webcontent = r.text
	webcontent = webcontent.replace('var apiData =', '')
	webcontent = json.loads(webcontent)
	content = webcontent['data']['rows']
	print(content)
	for news in content:
		print(news)
		title = news['title']
		link = news['url']
		print(title, link)
		print('=='*50)

def zhide():
	'什么值得买	https://post.smzdm.com/hot_1/'
	zhide_url = 'https://post.smzdm.com/rank/json_more/'		# 今日热榜
	headers = {
		"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
		"Cookie":""}
	datas = {'unit': 1	}
	r = requests.get(url=zhide_url, params=datas,  headers=headers)
	#webcontent = json.loads(r.text)
	webcontent = r.json()['data']
	for news in webcontent:
		title = news['title']
		content = news['content']
		link = news['article_url']
		print(title ,content, link)
		print('=='*30)

def rednotes():
	'小红书	https://www.xiaohongshu.com/explore'
	rednotes_url = 'https://www.xiaohongshu.com/fe_api/burdock/v2/homefeed/notes'		# 社区精选
	headers = {
		"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
		"X-Sign": "X0170686b081eea3b1a4368cf9f7c2199"
		}
		
	datas = {"pageSize":"20","oid":"recommend","page":"1"}
	r = requests.get(url=rednotes_url, params=datas,  headers=headers)
	#webcontent = json.loads(r.text)
	webcontent = r.json()['data']
	print(webcontent)
	for news in webcontent:
		title = news['title']
		articleid = news['id']
		link = "https://www.xiaohongshu.com/discovery/item/" + articleid
		print(title, link)
		print('=='*30)

def taobao():
	'淘宝人气榜'

def pinduoduo():
	'拼多多实时热销榜https://youhui.pinduoduo.com/search/hot-product-landing'
	pindd_url = 'https://youhui.pinduoduo.com/network/api/goods/top/list'		# 实时热销榜
	headers = {
		"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
		"content-type": "application/json; charset=UTF-8",
		"cookie": "pi_uid=CiSQIV3fEkKwSgArayQGAg==; _nano_fp=Xpd8n0UoX0EqXpPqn9_SA9l1hMT3z25lW1VhYI3I"
		}
		
	datas = {"pageNumber":1 ,"pageSize":50 ,"type":1}
	r = requests.post(url=pindd_url, json=datas,  headers=headers)
	#webcontent = json.loads(r.text)
	webcontent = r.json()['result']['list']
	# print(webcontent)
	for news in webcontent:
		print(news)
		print('=='*30)

def shuimu():
	'水木社区十大热门话题	http://www.newsmth.net/nForum/#!mainpage'
	shuimu_url = 'http://www.newsmth.net'
	headers = {
		"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
		"Cookie":""}
	r = requests.get(url=shuimu_url+'/nForum/mainpage?ajax',  headers=headers)
	webcontent = r.text
	# print(webcontent)
	soup = BeautifulSoup(webcontent, "html.parser")
	rank = soup.find("div", id="top10")
	# print(rank)
	content = rank.find_all("div")
	#print(content)
	for news in content:
		title = news.text
		link = news.select('div > a')[1]['href']
		link = shuimu_url + link
		print(title, link)
		print('=='*30)

def zhihu_daily():
	'知乎日报	https://daily.zhihu.com/'
	zhihudaily_url = 'https://daily.zhihu.com'
	headers = {
		"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
		"Cookie":""}
	r = requests.get(url=zhihudaily_url,  headers=headers)
	webcontent = r.text
	# print(webcontent)
	soup = BeautifulSoup(webcontent, "html.parser")
	rank = soup.find("div", class_="main-content-wrap")
	print(rank)
	content = rank.find_all("a", href = True)
	for news in content:
		print(news)
		title = news.text
		link = zhihudaily_url + news.get('href')
		print(title, link)
		print('--'*30)

def baidu_zhidao_daily():
	'百度知道日报	 https://zhidao.baidu.com/daily/'
	# 返回网页乱码的处理  https://blog.csdn.net/ahua_c/article/details/80942726
	zhidao_url = 'https://zhidao.baidu.com/daily/'
	headers = {
		"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
		"Cookie":""}
	r = requests.get(url=zhidao_url,  headers=headers)
	codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	r.encoding = codestyle	# 指定正确的编码格式
	#print(r.encoding)
	webcontent = r.text
	# print(webcontent)
	soup = BeautifulSoup(webcontent, "html.parser")
	rank = soup.find("ul", class_="daily-list")
	#print(rank)
	content = rank.find_all("div", class_="daily-cont-top")
	for news in content:
		#print(news)
		news = news.select('div>h2>a')[0]
		# print(news)
		title = news.text
		#title = title.decode('ISO-8859-1').encode('utf-8')
		link = zhidao_url + news.get('href')
		print(title, link)
		print('--'*30)

def kaiyan():
	'开眼视频	https://www.kaiyanapp.com/'
	kaiyan_url = 'https://baobab.kaiyanapp.com/api/v1/feed'		# 今日热榜
	headers = {
		"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
		"Cookie":""}
	datas = {'udid': '3e7ee30c6fc0004a773dc33b0597b5732b145c04'	}
	r = requests.get(url=kaiyan_url, params=datas,  headers=headers)
	#webcontent = json.loads(r.text)
	webcontent = r.json()['dailyList']
	for datalist in webcontent:
		#print(datalist)
		for news in datalist['videoList']:
			# print(news)
			title = news['title']
			content = news['description']
			link = news['rawWebUrl']
			print(title ,content, link)
			print('=='*30)

def woshipm():
	'人人都是产品经理 	http://www.woshipm.com/'
	woshipm_url = 'http://www.woshipm.com/__api/v1/browser/popular'		# 今日热榜
	headers = {
		"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
		"Cookie":""}
	datas = {'paged': 4, 'action': 'laodpostphp'}
	for i in range (10):
		datas['paged'] = i
		r = requests.get(url=woshipm_url, params=datas,  headers=headers)
		webcontent = r.json()
		if webcontent['success'] == 'true':
			for datalist in webcontent['payload']:
				print(datalist)
				title = datalist['title']
				link = datalist['permalink']
				content = datalist['snipper']
				print(title, link, content)
				print('==='*30)
		else:
			break

def xueqiu24():
	'雪球7X24 	https://xueqiu.com/?category=livenews'
	woshipm_url = 'https://xueqiu.com'		#7X24
	headers = {
		"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
		"Cookie":"aliyungf_tc=AQAAAPM1ekz2QwoAygj3Ovj65ln7kN6G; acw_tc=2760823215749884906861019e6fbc290e8904989db72b0e6746c4814fa0e7; xq_a_token=5e0d8a38cd3acbc3002589f46fc1572c302aa8a2; xqat=5e0d8a38cd3acbc3002589f46fc1572c302aa8a2; xq_r_token=670668eda313118d7214487d800c21ad0202e141; u=611574988489796; device_id=24700f9f1986800ab4fcc880530dd0ed; Hm_lvt_1db88642e346389874251b5a1eded6e3=1574988491; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1574988685elastic-apm-traceparent: 00-e25cb674b24fd980279371db0b1597f7-860b31a5829440bb-01"
		}
	datas = {'since_id': '-1', 'max_id': '-1', 'count': '15', 'category':'-1'}
	for i in range (10):
		
		r = requests.get(url=woshipm_url+'/v4/statuses/public_timeline_by_category.json', params=datas,  headers=headers)
		webcontent = r.json()
		print(webcontent)
		datas['max_id'] = webcontent['next_max_id']
		for contents in webcontent['list']:
			article = json.loads(contents['data'])
			print(article)
			title = article['topic_desc']
			link = woshipm_url + article['target']
			content = article['description']
			print(title, link, content)

			print('==='*30)

if __name__ == '__main__':
	xueqiu24()