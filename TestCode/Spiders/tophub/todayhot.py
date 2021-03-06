'''
爬取各个站点热门话题
https://mp.weixin.qq.com/s/WmZXm6rsMjN2wcVD6E5jQg
今日热榜：https://tophub.today/
'''
import time
import requests
import re
import json
import re
import datetime
from bs4 import BeautifulSoup

headers = {
			"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
			"Cookie":""
		  }

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
	'baidu'
	headers = {
			"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
			"Cookie":""}
	baidu_url = 'http://top.baidu.com'

	def baidu_hot():
		'百度实时热点http://top.baidu.com/?vit=1&fr=topnews'		
		r = requests.get(url=baidu_url+'/?vit=1&fr=topnews', headers=headers)
		codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		r.encoding = codestyle	# 指定正确的编码格式
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

	def tieba():
		'贴吧热议榜http://tieba.baidu.com/hottopic/browse/topicList'
		tieba_url = 'http://tieba.baidu.com'
		datas = {'res_type':'1', 'red_tag':'v1188856214'}
		r = requests.get(url=tieba_url+'/hottopic/browse/topicList', params=datas, headers=headers)
		codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		r.encoding = codestyle	# 指定正确的编码格式
		webcontent = r.text
		# print(webcontent)
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

	def baidu_zhidao_daily():
		'百度知道日报	 https://zhidao.baidu.com/daily/'
		# 返回网页乱码的处理  https://blog.csdn.net/ahua_c/article/details/80942726
		zhidao_url = 'https://zhidao.baidu.com'
		r = requests.get(url=zhidao_url+'/daily/',  headers=headers)
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

	def baidu_hotnews():
		'百度热点要闻	 http://news.baidu.com/'
		# 返回网页乱码的处理  https://blog.csdn.net/ahua_c/article/details/80942726
		hotnews_url = 'http://news.baidu.com/'
		r = requests.get(url=hotnews_url,  headers=headers)
		codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		r.encoding = codestyle	# 指定正确的编码格式
		#print(r.encoding)
		webcontent = r.text
		# print(webcontent)
		soup = BeautifulSoup(webcontent, "html.parser")
		hotnews = soup.find("div", class_="hotnews")
		hotnews = hotnews.find_all('strong')
		print("##############热点要闻##############")
		for news in hotnews:
			title = news.select('strong>a')[0].text
			link = news.select('strong>a')[0].get('href')
			print(title, link)
			print('*'*50)
		focuslistnews = soup.find_all("ul", class_="ulist focuslistnews")
		for focuslist in focuslistnews:
			news = focuslist.find_all('li')
			for new in news:
				title = new.select('li>a')[0].text
				link = new.select('li>a')[0].get('href')
				print(title, link)
				print('*'*50)

		hotwords = soup.find("ul", class_="hotwords clearfix")
		hotwords = hotwords.find_all('li')
		print("##############热搜新闻词##############")
		for news in hotwords:
			title = news.select('li>a')[0].text
			link = news.select('li>a')[0].get('href')
			print(title, link)
			print('*'*50)

		baijia = soup.find("div", class_="baijia-focus-list")
		baijia = baijia.find_all('ul',class_='ulist bdlist')
		print("##############百家号##############")
		for baijialist in baijia:
			news = baijialist.find_all('li')
			for new in news:
				title = new.select('li>a')[0].text
				link = new.select('li>a')[0].get('href')
				print(title, link)
				print('*'*50)
	return baidu_hot(), tieba(), baidu_zhidao_daily(), baidu_hotnews()
	#return baidu_hotnews()

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
	douban_url = 'https://movie.douban.com'
	headers = {
		"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
		"Cookie":""}
	def newmovie():
		'豆瓣新片榜单https://movie.douban.com/chart'
		r = requests.get(url=douban_url+'/chart', headers=headers)
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
	return newmovie()

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

def xueqiu():
	'雪球 	https://xueqiu.com/?category=livenews'
	xueqiu_url = 'https://xueqiu.com'		#7X24
	headers = {
		"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
		"Cookie":"aliyungf_tc=AQAAAPM1ekz2QwoAygj3Ovj65ln7kN6G; acw_tc=2760823215749884906861019e6fbc290e8904989db72b0e6746c4814fa0e7; xq_a_token=5e0d8a38cd3acbc3002589f46fc1572c302aa8a2; xqat=5e0d8a38cd3acbc3002589f46fc1572c302aa8a2; xq_r_token=670668eda313118d7214487d800c21ad0202e141; u=611574988489796; device_id=24700f9f1986800ab4fcc880530dd0ed; Hm_lvt_1db88642e346389874251b5a1eded6e3=1574988491; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1574988685elastic-apm-traceparent: 00-e25cb674b24fd980279371db0b1597f7-860b31a5829440bb-01"
		}
	datas = {'since_id': '-1', 'max_id': '-1', 'count': '15', 'category':'-1'}
	'雪球推荐'
	for i in range (10):
		r = requests.get(url=xueqiu_url+'/v4/statuses/public_timeline_by_category.json', params=datas,  headers=headers)
		webcontent = r.json()
		#print(webcontent)
		datas['max_id'] = webcontent['next_max_id']
		for contents in webcontent['list']:
			article = json.loads(contents['data'])
			#print(article)
			title = article['topic_desc']
			link = xueqiu_url + article['target']
			content = article['description']
			print(title, link, content)
			print('==='*30)

	'雪球7X24'
	datas['category'] = 6
	for i in range (10):
		
		r = requests.get(url=xueqiu_url+'/v4/statuses/public_timeline_by_category.json', params=datas,  headers=headers)
		webcontent = r.json()
		#print(webcontent)
		datas['max_id'] = webcontent['next_max_id']
		for contents in webcontent['list']:
			article = json.loads(contents['data'])
			#print(article)
			link = xueqiu_url + article['target']
			content = article['text']
			print(link, content)
			print('==='*30)

	'热股榜'
	r = requests.get(url='https://stock.xueqiu.com/v5/stock/hot_stock/list.json', params={'size':10, '_type':10, 'type':10},  headers=headers)
	webcontent = r.json()['data']['items']
	for tikets in webcontent:
		print(tikets)
		print('*'*50)

	'热门新闻'
	data_hostnews = {'a':1, 'count':10, 'page':1, 'meigu':0, 'scope':'day', 'type':'news'}
	r = requests.get(url=xueqiu_url+'/statuses/hots.json', params=data_hostnews,  headers=headers)
	webcontent = r.json()
	for news in webcontent:
		title = news['title']
		content = news['text']
		print(title, content)
		print('*'*50)

	'热门公告'
	data_notice = data_hostnews
	data_notice['type'] = 'notice'
	r = requests.get(url=xueqiu_url+'/statuses/hots.json', params=data_notice,  headers=headers)
	webcontent = r.json()
	for news in webcontent:
		content = news['text']
		print(content)
		print('*'*50)

def toutiao():
	'今日头条 	https://www.toutiao.com/'
	toutiao_url = 'https://www.toutiao.com/'		#7X24
	headers = {
		"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
		"Cookie":""
		}
	datas = {'min_behot_time':0,'category':'__all__','utm_source':'toutiao','widen':1,'tadrequire':'true','as':'A105DD9E208921E','cp':'5DE089C211BE3E1','_signature':'.IIYsgAgEBUNIF6vxpLc2PyCGKAAKFs'}
	r = requests.get(url=toutiao_url+'api/pc/feed/', params=datas,  headers=headers)
	webcontent = r.json()['data']
	for news in webcontent:
		title = news['title']
		source = news['source']
		content = news['abstract']
		link = toutiao_url+'a'+news['item_id']
		print(title, source, content, link)
		print('*'*50)

def guancha():
	'观察者	https://www.guancha.cn/?s=dhshouye'
	guancha_url = 'https://www.guancha.cn'
	headers = {
				"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
				"Cookie":""
			  }
	r = requests.get(url=guancha_url+'/?s=dhshouye', headers=headers)
	codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	r.encoding = codestyle	# 指定正确的编码格式
	webcontent = r.text
	# print(webcontent)
	soup = BeautifulSoup(webcontent, "html.parser")
	index_list = soup.find("ul", class_="Review-item")
	# print(index_list)
	content = index_list.find_all("h4", class_='module-title')
	for news in content:
		# print(news)
		title = news.text
		link = news.select('h4>a')[0].get('href')
		link = guancha_url + link
		print(title, link)
		print('*'*50)

def gaoqingla():
	'中国高清网	http://gaoqing.la/'
	gaoqing_url = 'http://gaoqing.la/'
	headers = {
				"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
				"Cookie":""
			  }
	r = requests.get(url=gaoqing_url, headers=headers)
	codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	r.encoding = codestyle	# 指定正确的编码格式
	webcontent = r.text
	# print(webcontent)
	soup = BeautifulSoup(webcontent, "html.parser")
	index_list = soup.find("ul", id="post_container")
	# print(index_list)
	content = index_list.find_all("div", class_='article')
	for news in content:
		#news = news.find('h2', href = True)
		#print(news)
		title = news.select('div>h2')[0].text
		link = news.select('div>h2>a')[0].get('href')
		print(title, link)

def sina_sports():
	'新浪体育-NBA技术统计 https://slamdunk.sports.sina.com.cn/player/rank#season_type=reg&item_type=average&item=points'
	sina_nba_url = 'https://slamdunk.sports.sina.com.cn/api'	
	headers = {
		"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
		"Cookie":""
		}

	'球员得分'
	datas_player = {
			'p':'radar',
			'callback':'jQuery11130004012145345625218_1575247137004',
			'p':'radar',
			's':'leaders',
			'a':'players_top',
			'season':2019,
			'season_type':'reg',
			'item_type':'average',
			'item':'points',
			'order':1,
			'_':1575247137005
			}
	r = requests.get(url=sina_nba_url, params=datas_player,  headers=headers)	# 球员得分
	webcontent = r.text
	
	pattern = re.compile('{"result":{"status".*}]}}}')
	webcontent = pattern.search(webcontent)
	webcontent = webcontent.group()
	webcontent = json.loads(webcontent)
	print(type(webcontent))
	players = webcontent['result']['data']['players']
	for player in players:
		name = player['last_name']
		score = player['score']
		team = player['team_name']
		print(player)
		print(name, score, team)
		print('*'*50)

	'球队排名'
	datas_team = {
			'p':'radar',
			'callback':'jQuery1113002749331082455897_1575418857475',
			'p':'radar',
			's':'team_standing',
			'a':'conference',
			'_':1575247137005
			}
	r = requests.get(url=sina_nba_url, params=datas_team,  headers=headers)
	webcontent = r.text
	
	pattern = re.compile('{"result":{"status".*}]}}}')
	webcontent = pattern.search(webcontent)
	webcontent = webcontent.group()
	webcontent = json.loads(webcontent)
	# print(webcontent)
	eastern = webcontent['result']['data']['eastern']	#东部球队
	western = webcontent['result']['data']['western']	#西部球队
	print('*'*20+'东部球队'+'*'*20)
	for team in eastern:
		name = team['team_name']
		wins = team['wins']
		losses = team['losses']
		points_for = team['points_for']
		points_against = team['points_against']
		print(name, wins, losses, points_for, points_against)
		print('-'*50)
	print('*'*20+'东部球队'+'*'*20)
	for team in western:
		name = team['team_name']
		wins = team['wins']
		losses = team['losses']
		points_for = team['points_for']
		points_against = team['points_against']
		print(name, wins, losses, points_for, points_against)
		print('-'*50)

	'最近5场比赛'
	datas_latest5 = {
			'p':'radar',
			'callback':'jQuery1113002749331082455897_1575418857475',
			'p':'radar',
			's':'schedule',
			'a':'latest',
			'limit':5 ,
			'_':1575247137005
			}
	r = requests.get(url=sina_nba_url, params=datas_latest5,  headers=headers)
	webcontent = r.text
	# print(webcontent)
	
	pattern = re.compile('{"result":{"status".*}]}}')
	webcontent = pattern.search(webcontent)
	webcontent = webcontent.group()
	webcontent = json.loads(webcontent)
	# print(webcontent)
	gamedata = webcontent['result']['data']
	for game in gamedata:
		home_name = game['home_name']
		home_score = game['home_score']
		away_name = game['away_name']
		away_score = game['away_score']
		print(str(home_name)+' VS '+str(away_name)+' : '+str(home_score)+' - '+str(away_score))
		print('-'*50)

	'本赛季常规赛数据之最_球队'
	datas_teamtop = {
			'p':'radar',
			'callback':'jQuery1113002749331082455897_1575418857475',
			'p':'radar',
			's':'leaders',
			'a':'team_top',
			'season_type': 'reg',
			'_':1575247137005
			}
	r = requests.get(url=sina_nba_url, params=datas_teamtop,  headers=headers)
	webcontent = r.text
	# print(webcontent)
	pattern = re.compile('{"result":{"status".*]}}}')
	webcontent = pattern.search(webcontent)
	webcontent = webcontent.group()
	webcontent = json.loads(webcontent)
	#print(webcontent)
	gamedata = webcontent['result']['data']['items']
	# print(gamedata)
	for game in gamedata:
		item_name = game['item']['name']
		print('数据统计：{}'.format(item_name))
		for teamdata in game['teams']:
			print(teamdata)
		print('-'*50)

	'本赛季常规赛数据之最_球员'
	datas_playertop = {
			'p':'radar',
			'callback':'jQuery1113002749331082455897_1575418857475',
			'p':'radar',
			's':'leaders',
			'a':'player_top',
			'season_type': 'reg',
			'_':1575247137005
			}
	r = requests.get(url=sina_nba_url, params=datas_playertop,  headers=headers)
	webcontent = r.text
	# print(webcontent)
	pattern = re.compile('{"result":{"status".*]}}}')
	webcontent = pattern.search(webcontent)
	webcontent = webcontent.group()
	webcontent = json.loads(webcontent)
	#print(webcontent)
	gamedata = webcontent['result']['data']['items']
	# print(gamedata)
	for game in gamedata:
		item_name = game['item']['name']
		print('数据统计：{}'.format(item_name))
		for teamdata in game['players']:
			print(teamdata)
		print('-'*50)

	football_url = 'http://api.sports.sina.com.cn/'
	'国际足球积分榜'
	area = {'英超':4,'西甲':2,'德甲':3,'意甲':1,'法甲':5,'欧冠':10,'欧联':11}	# 联赛ID
	datas_football = {
			'p': 'sports',
			's': 'sport_client',
			'a': 'index',
			'_sport_t_': 'football',
			'_sport_s_': 'opta',
			'_sport_a_': 'teamOrder',
			'dpc': 1,
			'callback': 'CB_870D9E88_4765_467F_A1D5_86E72C601287_3571367214_11_2019',
			'app_key': 3571367214,
			'type': 4,
			'season': 2019,
			'dpc': 1
			}
	for area_name, area_id in area.items():
		datas_football['type'] = area_id
		datas_football['_sport_a_'] = 'teamOrder'
		r = requests.get(url=football_url, params=datas_football,  headers=headers)
		webcontent = r.text
		# print(webcontent)
		pattern = re.compile('{"result":{"status".*}]}}')
		webcontent = pattern.search(webcontent)
		webcontent = webcontent.group()
		webcontent = json.loads(webcontent)
		# print(webcontent)
		gamedata = webcontent['result']['data']
		print('*'*20+'{}联赛积分'.format(area_name)+'*'*20)
		for game in gamedata:
			team_cn = game['team_cn']
			team_order = game['team_order']
			count = game['count']
			win = game['win']
			lose = game['lose']
			draw = game['draw']
			goal = game['goal']
			losegoal = game['losegoal']

			print('{0} 排名：{7} 场次：{1} 胜：{2} 负：{3} 平：{4} 进球：{5} 失球：{6}'.format(team_cn,count,win,lose,draw,goal,losegoal,team_order))
			print('-'*50)

		datas_player = datas_football
		datas_player['_sport_a_'] = 'playerorder'
		datas_player['item'] = 13
		datas_player['limit'] = 50
		r = requests.get(url=football_url, params=datas_player,  headers=headers)
		webcontent = r.text
		# print(webcontent)
		pattern = re.compile('{"result":{"status".*}]}}')
		webcontent = pattern.search(webcontent)
		webcontent = webcontent.group()
		webcontent = json.loads(webcontent)
		# print(webcontent)
		gamedata = webcontent['result']['data']
		print('*'*20+'{}联赛射手榜'.format(area_name)+'*'*20)
		for game in gamedata:
			goals_count = game['item1']	#总进球
			goals_nomal = game['item2']	#普通进球
			goals_dian = game['item3']	#点球
			player_name = game['player_name']
			team_name = game['team_name']
			print('{0} 球队：{1} 总数：{2} 普通：{3} 点球：{4}'.format(player_name,team_name,goals_count,goals_nomal,goals_dian))
			print('-'*50)

	'热门体育新闻'
	sina_sport_url = 'http://sports.sina.com.cn/'
	r = requests.get(url=sina_sport_url, headers=headers)
	codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	r.encoding = codestyle	# 指定正确的编码格式
	webcontent = r.text
	#print(webcontent)
	soup = BeautifulSoup(webcontent, "html.parser")
	index_list = soup.find("div", class_="ty-top-ent")
	# print(index_list)
	content = index_list.find_all("h3", class_='ty-card-tt')
	for news in content:
		#print(news)
		title = news.text
		link = news.select('h3>a')[0].get('href')
		link = 'https:'+link
		print(title, link)
		print('*'*50)

def boxoffice():
	'电影票房	http://58921.com/daily'
	box_url = 'http://58921.com'
	headers = {
				"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
				"Cookie":""
			  }
	'每日票房'
	r = requests.get(url=box_url+'/daily', headers=headers)
	codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	r.encoding = codestyle	# 指定正确的编码格式
	webcontent = r.text
	pattern = re.compile('<tr class=.* </tr>')	# 正则匹配所有的<tr class="">标签
	content = pattern.findall(webcontent)
	# print(content)
	for news in content:
		news = BeautifulSoup(news, "html.parser")	#转换成html格式
		# print(news)
		title = news.select('tr>td')[0].text
		link = news.select('tr>td>a')[0].get('href')
		link = box_url+link
		total = news.select('tr>td')[1].text 	#总票房
		people = news.select('tr>td')[2].text 	#观影人次
		rounds = news.select('tr>td')[3].text 	#播放场次
		print('{0} 票房：{1} 人次:{2} 场次:{3} 链接:{4} '.format(title, total, people, rounds, link))

	'总票房排行'
	r = requests.get(url=box_url+'/alltime', headers=headers)
	codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	r.encoding = codestyle	# 指定正确的编码格式
	webcontent = r.text
	pattern = re.compile('<tr class=.* </tr>')	# 正则匹配所有的<tr class="">标签
	content = pattern.findall(webcontent)
	# print(content)
	for news in content:
		news = BeautifulSoup(news, "html.parser")	#转换成html格式
		# print(news)
		title = news.select('tr>td')[2].text
		paiming = news.select('tr>td')[0].text 	#年度排名
		his_paiming = news.select('tr>td')[1].text 	#历史排名
		total = news.select('tr>td')[1].text 	#总票房
		date = news.select('tr>td')[6].text 	#上映年份
		link = news.select('tr>td>a')[0].get('href')
		link = box_url+link
		print('{0} 年度排名：{1} 历史排名:{2} 总票房:{3} 上映年份:{4} 链接:{5} '.format(title, paiming, his_paiming, total, date, link))

	'实时票房排行榜'
	r = requests.get(url=box_url+'/boxoffice/live', headers=headers)
	codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	r.encoding = codestyle	# 指定正确的编码格式
	webcontent = r.text
	pattern = re.compile('<tr class=.* </tr>')	# 正则匹配所有的<tr class="">标签
	content = pattern.findall(webcontent)
	# print(content)
	lens = len(content)
	for news in content[1:lens-1]:
		news = BeautifulSoup(news, "html.parser")	#转换成html格式
		# print(news)
		title = news.select('tr>td>a')[0].text
		today = news.select('tr>td')[1].text 	#当日排片
		today_people = news.select('tr>td')[2].text 	#当日观影人次
		today_total = news.select('tr>td')[3].text 	#当日预售票房
		total = news.select('tr>td')[4].text 	#实时累积票房
		link = news.select('tr>td>a')[0].get('href')
		link = box_url+link
		print('{0} 当日排片:{1} 当日观影人次:{2} 当日预售票房:{3} 实时累积票房:{4} 链接:{5} '.format(title, today, today_people, today_total, total, link))

def cbooo():
	'中国票房	http://www.cbooo.cn/'
	cbooo_url = 'http://www.cbooo.cn'
	headers = {
				"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
				"Cookie":""
			  }
	def gloabalbox():
		'全球票房'
		print('#'*20+'全球票房'+'#'*20)
		r = requests.get(url=cbooo_url+'/global', headers=headers)
		# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		# r.encoding = codestyle	# 指定正确的编码格式
		webcontent = r.text
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		# pattern = re.compile('<tr class=.* </tr>')	# 正则匹配所有的<tr class="">标签
		webcontent = soup.find('select', id='selTimeElm')
		# content = pattern.findall(webcontent)
		content = webcontent.find_all('option')
		#print(content)
		for news in content:
			# news = BeautifulSoup(news, "html.parser")	#转换成html格式
			pattern = re.compile('<option value=.*>')	# 正则匹配所有的<tr class="">标签
			text = pattern.search(str(news))
			text = text.group()
			pattern2 = re.compile("\d+")
			value = pattern2.search(text)
			date_value = value.group()	# 票房日期的值
			#print(value)
			title = news.text 	# 票房日期的文字描述
			title = title.strip()
			#print(title)
			resp = requests.get(url=cbooo_url+'/BoxOffice/getAllInfo', params={'weekId': date_value})
			movies = resp.json()
			print('票房日期：{}'.format(title))
			for movie in movies:
				movie_name = movie['MovieName']
				order = movie['Rank']	# 排名
				order_c = movie['RankChange']	# 排名变化
				BoxOffice = movie['BoxOffice']	# 周末票房(万)
				SumBoxOffice = movie['SumBoxOffice']	# 累计票房(万)
				CountryNum = movie['CountryNum']	# 国家及地区数		
				WeekNum = movie['WeekNum']	# 上映周数
				print('{0} 排名：{1} 排名变化:{2}  周末票房(万):{3} 累计票房(万):{4} 国家及地区数:{5} 上映周数:{6} '.format(movie_name, order, order_c, BoxOffice, SumBoxOffice, CountryNum, WeekNum))
				print('-'*50)

	def northA():
		'北美票房'
		print('#'*20+'北美票房'+'#'*20)
		r = requests.get(url=cbooo_url+'/northAmerica', headers=headers)
		# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		# r.encoding = codestyle	# 指定正确的编码格式
		webcontent = r.text
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		# pattern = re.compile('<tr class=.* </tr>')	# 正则匹配所有的<tr class="">标签
		webcontent = soup.find('select', id='selTimeElm')
		# content = pattern.findall(webcontent)
		content = webcontent.find_all('option')
		#print(content)
		for news in content:
			# news = BeautifulSoup(news, "html.parser")	#转换成html格式
			pattern = re.compile('<option value=.*>')	# 正则匹配所有的<tr class="">标签
			text = pattern.search(str(news))
			text = text.group()
			pattern2 = re.compile("\d+")
			value = pattern2.search(text)
			date_value = value.group()	# 票房日期的值
			#print(value)
			title = news.text 	# 票房日期的文字描述
			title = title.strip()
			#print(title)
			resp = requests.get(url=cbooo_url+'/BoxOffice/getALLInfo_b', params={'weekId': date_value})
			movies = resp.json()
			print('票房日期：{}'.format(title))
			for movie in movies:
				movie_name = movie['MovieName']
				order = movie['Rank']	# 排名
				order_c = movie['RankChange']	# 排名变化
				WeekendBoxOffice = movie['WeekendBoxOffice']	# 周末票房(万)
				BoxOffice = movie['BoxOffice']	# 累计票房(万)
				Cinema = movie['Cinema']	# 放映影院数	
				WeekNum = movie['WeekNum']	# 上映周数
				print('{0} 排名：{1} 排名变化:{2}  周末票房(万):{3} 累计票房(万):{4} 放映影院数:{5} 上映周数:{6} '.format(movie_name, order, order_c, WeekendBoxOffice, BoxOffice, Cinema, WeekNum))
				print('-'*50)

	def HK():
		'香港票房'
		print('#'*20+'香港票房'+'#'*20)
		r = requests.get(url=cbooo_url+'/hongkong', headers=headers)
		# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		# r.encoding = codestyle	# 指定正确的编码格式
		webcontent = r.text
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		# pattern = re.compile('<tr class=.* </tr>')	# 正则匹配所有的<tr class="">标签
		webcontent = soup.find('select', id='selTimeElm')
		# content = pattern.findall(webcontent)
		content = webcontent.find_all('option')
		#print(content)
		for news in content:
			# news = BeautifulSoup(news, "html.parser")	#转换成html格式
			pattern = re.compile('<option value=.*>')	# 正则匹配所有的<tr class="">标签
			text = pattern.search(str(news))
			text = text.group()
			pattern2 = re.compile("\d+")
			value = pattern2.search(text)
			date_value = value.group()	# 票房日期的值
			#print(value)
			title = news.text 	# 票房日期的文字描述
			title = title.strip()
			#print(title)
			resp = requests.get(url=cbooo_url+'/BoxOffice/getALLInfo_x', params={'weekId': date_value})
			movies = resp.json()
			print('票房日期：{}'.format(title))
			for movie in movies:
				movie_name = movie['MovieName']
				order = movie['Rank']	# 排名
				order_c = movie['RankChange']	# 排名变化
				WeekendBoxOffice = movie['WeekBoxOffice']	# 周末票房(万)
				BoxOffice = movie['SumBoxOffice']	# 累计票房(万)
				# Cinema = movie['Cinema']	# 放映影院数	
				WeekNum = movie['WeekNum']	# 上映天数
				print('{0} 排名：{1} 排名变化:{2}  周末票房(万):{3} 累计票房(万):{4} 上映天数:{5} '.format(movie_name, order, order_c, WeekendBoxOffice, BoxOffice, WeekNum))
				print('-'*50)

	def getMdata_movie():
		'影库'
		print('#'*30+'影库'+'#'*30)
		datas = {'area':50, 'type':0, 'year':0, 'initial':'全部', 'pIndex':1}
		r = requests.get(url=cbooo_url+'/Mdata/getMdata_movie', params=datas, headers=headers)
		webcontent = r.json()
		page_num = webcontent['tPage']	# 获取总页数
		# for i in range(1, page_num+1):
		for i in range(1, page_num+1):
			print(i)
			datas['pIndex'] = i
			r = requests.get(url=cbooo_url+'/Mdata/getMdata_movie', params=datas, headers=headers)
			webcontent = r.json()['pData']
			for movie in webcontent:
				movie_name = movie['MovieName']
				MovieEnName = movie['MovieEnName']	#英文名
				BoxOffice = movie['BoxOffice']	# 总票房
				releaseYear = movie['releaseYear']	# 上映年份
				print('{0} {1} 总票房:{2}  上映年份:{3} '.format(movie_name, MovieEnName, BoxOffice, releaseYear))
				print('-'*50)

	def GetPlayIndexRank():
		'电视'
		print('#'*30+'电视'+'#'*30)
		datas = {'tvType': 2}
		r = requests.get(url=cbooo_url+'/Mess/GetPlayIndexRank', params=datas, headers=headers)
		webcontent = r.json()
		webcontent = webcontent['data1']	# 获取总页数
		# print(webcontent)
		for movie in webcontent:
			movie_name = movie['TvName']
			Genres = movie['Genres']	#类型
			rank = movie['Irank']	# 排名
			print('{0} 类型:{1} 排名:{2} '.format(movie_name, Genres, rank))
			print('-'*50)

	def GetNewsList():
		'资讯'
		print('#'*30+'资讯'+'#'*30)
		datas = {'pIndex': 1}
		r = requests.get(url=cbooo_url+'/Information/GetNewsList', params=datas, headers=headers)
		webcontent = r.json()
		page_num = webcontent['tolPage']	# 获取总页数
		# for i in range(1, page_num+1):
		for i in range(1, page_num+1):
			print(i)
			datas['pIndex'] = i
			r = requests.get(url=cbooo_url+'/Information/GetNewsList', params=datas, headers=headers)
			webcontent = r.json()['d']
			for movie in webcontent:
				title = movie['title']
				addtime = movie['addtime']	#发布时间
				print('{0} {1}'.format(addtime, title))
				print('-'*50)
				
	return HK(), gloabalbox(), northA(), getMdata_movie(), GetPlayIndexRank(), GetNewsList()
	# return GetNewsList()

def testerhome():
	'TesterHome https://testerhome.com/topics/excellent'
	headers = {
			"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
			"Cookie":""
		  }
	tester_url = 'https://testerhome.com'
	def excellent():
		'精华帖'
		r = requests.get(url=tester_url+'/topics/excellent', headers=headers)
		# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		# r.encoding = codestyle	# 指定正确的编码格式
		webcontent = r.text
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		webcontent = soup.find('div', class_='panel-body item-list')
		content = webcontent.find_all('div', class_='title media-heading')
		# print(content)
		for news in content:
			title = news.select('div>a')[0].get('title')
			link = news.select('div>a')[0].get('href')
			link = tester_url + link
			print(title, link)
			# print(news)
			print('*'*50)
	def jobs():
		'招聘'
		datas = {'location':'上海'}
		r = requests.get(url=tester_url+'/jobs', params=datas, headers=headers)
		# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		# r.encoding = codestyle	# 指定正确的编码格式
		webcontent = r.text
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		webcontent = soup.find('div', class_='panel-body item-list')
		content = webcontent.find_all('div', class_='title media-heading')
		# print(content)
		for news in content:
			title = news.select('div>a')[0].get('title')
			link = news.select('div>a')[0].get('href')
			link = tester_url + link
			print(title, link)
			# print(news)
			print('*'*50)

	return excellent(), jobs()

def testing51():
	'51testing最新热门 http://bbs.51testing.com/forum.php?mod=guide&view=hot'
	headers = {
			"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
			"Cookie":""
		  }
	tester_url = 'http://bbs.51testing.com/'
	datas = {'mod': 'guide', 'view': 'hot'}
	r = requests.get(url=tester_url+'forum.php', params=datas, headers=headers)
	# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	# r.encoding = codestyle	# 指定正确的编码格式
	webcontent = r.text
	soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
	content = soup.find_all('th', class_="common")
	for news in content:
		new = news.find('a', href=True)
		title = new.text
		link = new.get('href')
		link = tester_url + link
		print(title, link)
		#print(new)
		print('*'*50)

def github():
	'github explore https://github.com/explore'
	headers = {
			"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
			"Cookie":""
		  }
	github_url = 'https://github.com'
	r = requests.get(url=github_url+'/explore', headers=headers)
	# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	# r.encoding = codestyle	# 指定正确的编码格式
	webcontent = r.text
	soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
	webcontent = soup.find('div', class_="col-md-8 col-lg-6 py-4")
	# print(webcontent)
	content = webcontent.find_all('article', class_="border rounded-1 box-shadow bg-gray-light my-4")
	# print(content)
	for news in content:
		new = news.find('a', class_="text-bold")
		new2 = news.find('a', class_="social-count float-none")
		if new:
			title = (new.text).strip()
			link = new.get('href')
			link = github_url + linkk
			star = (new2.text).strip() 	#标星数量
			print(title, star, link)
			# print(new)
			print('*'*50)

def zhibo8():
	'zhibo8 https://www.zhibo8.cc/'
	headers = {
			"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
			"Cookie":""
		  }
	zhibo8_url = 'https://www.zhibo8.cc'
	def sportsnews():
		'集锦&新闻'
		r = requests.get(url=zhibo8_url, headers=headers)
		codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		r.encoding = codestyle	# 指定正确的编码格式
		webcontent = r.text
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		webcontent = soup.find('div', id="recommend")
		# print(webcontent)
		content1 = webcontent.find_all('div', class_="r_video left")
		content2 = webcontent.find_all('div', class_="r_news right")
		for content in content1:
			# print(content)
			news = content.find_all('li', href=False)
			for new in news:
				aticles = new.find_all('a', href=True)
				for aticle in aticles:
					title = aticle.text
					link = aticle.get('href')
					print(title, link)
					print('*'*50)

		for content in content2:
			# print(content)
			news = content.find_all('li', href=False)
			for new in news:
				aticles = new.find_all('a', href=True)
				for aticle in aticles:
					title = aticle.text
					link = aticle.get('href')
					print(title, link)
					print('*'*50)

	def games():
		'比赛-全部'
		r = requests.get(url=zhibo8_url, headers=headers)
		codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		r.encoding = codestyle	# 指定正确的编码格式
		webcontent = r.text
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		webcontent = soup.find('div', class_="schedule_container left")
		
		# print(webcontent)
		gamebox = webcontent.find_all('div', class_='box')
		for box in gamebox:
			gamedate = box.find('h2').text 	#比赛日期
			print('#############'+gamedate+'#############')
			content = box.find('div', class_='content')
			content = content.find_all('li', href=False)
			for games in content:
				title = games.get('label')
				print(title)
				channels = games.find_all('a', href=True)	# 直播渠道
				for channel in channels:
					name = channel.text 	# 直播源名称
					link = channel.get('href') #直播地址
					if link.startswith('http'):
						pass
					else:
						link = zhibo8_url + link
					print(name, link)
				print('*'*50)
			print('='*50)
	return games(), sportsnews()

def cnblogs():
	'博客园cnblogs https://www.cnblogs.com/'
	headers = {
			"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
			"Cookie":""
		  }
	cnblogs_url = 'https://www.cnblogs.com'

	def pick():
		'首页精华 https://www.cnblogs.com/pick/'
		i = 1
		maxpage = 0
		while 1:
			page = i
			r = requests.get(url=cnblogs_url+'/pick#p%s'%(page), headers=headers)
			i += 1
			# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
			# r.encoding = codestyle	# 指定正确的编码格式
			webcontent = r.text
			soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
			webcontent = soup.find('div', id="post_list")
			#print(webcontent)
			content = webcontent.find_all('div', class_="post_item_body")
			# print(content)
			for news in content:
				title = news.select('div>h3')[0].text
				newsbody = news.select('div>p')[0].text
				# linkdesc = news.find('p', class_='post_item_summary')
				# link = linkdesc.find('a', href=True)
				link = news.select('div>h3>a')[0].get('href')
				print(title)
				print(newsbody)
				print(link)
				print('*'*50)
			if page == 2:
				pages = []	# 获取总页数
				pagelist = soup.find('div', class_='pager')
				pagelist = pagelist.find_all('a', href=True)
				for page in pagelist:
					page = page.text
					print(type(page))
					if page.startswith('N'):	# 去掉'Next'
						pass
					# page = page.strip('https://www.cnblogs.com/fnng/default.html?page=')
					else:
						pages.append(int(page))
				pages.sort(reverse=True)
				maxpage = pages[0]	#获取最大页数
				# print(maxpage)
			print('maxpage==%s'%maxpage)
			print('page=%s'%(page))
			if page == maxpage:
				print('到达最大页数，获取数据完成')
				break	# 当前执行页达到最大页数，跳出循环

	def yichun():
		'乙醇的cnblog'
		r = requests.get(url=cnblogs_url+'/nbkhic', headers=headers)
		# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		# r.encoding = codestyle	# 指定正确的编码格式
		webcontent = r.text
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		webcontent = soup.find('div', class_="forFlow")
		# print(webcontent)
		content = webcontent.find_all('div', class_="day")
		# print(content)
		for news in content:
			dayTitle = news.find('div', class_='dayTitle')	#发布日期
			dayTitle = dayTitle.find('a', href=True)
			daytitle = dayTitle.text
			postTitle = news.find('a', class_='postTitle2')	# 主题
			posttitle = (postTitle.text).strip()
			postcon = postcon.strip('阅读全文')
			try:
				postCon = news.find('div', class_='c_b_p_desc')	# 简介
				postcon = (postCon.text).strip()
			except:
				postcon= 'None'

			postDesc = news.find('div', class_='postDesc')	# 全文链接
			postDesc = postDesc.find('a', href=True)
			link = postDesc.get('href')
			print(daytitle,posttitle,postcon, link)
			print('*'*50)

	def chongshi():
		'虫师cnblog'
		maxpage = 0
		i = 1
		while 1:
			page = i
			r = requests.get(url=cnblogs_url+'/fnng/default.html?page=%s'%(page), headers=headers)
			# print('page=%s'%(page))
			i += 1
			print(r.url)
			#print(r.text)
			webcontent = r.text
			soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
			webcontent = soup.find('div', id="content")
			# print(webcontent)
			content = webcontent.find_all('div', class_="post post-list-item")
			# print(content)
			for news in content:
				postTitle = news.find('h2')	# 主题
				posttitle = (postTitle.text).strip()
				try:
					postCon = news.find('div', class_='c_b_p_desc')	# 简介
					postcon = (postCon.text).strip()
					postcon = postcon.strip('阅读全文')
					# postcon.replace('阅读全文')
					linkdesc = postCon.find('a', href=True)
					link = linkdesc.get('href')
				except:
					postcon= 'None'
				
				print(posttitle)
				print(postcon)
				print(link)
				print('*'*50)

			if page == 2:
				pages = []	# 获取总页数
				pagelist = soup.find('div', id='homepage_bottom_pager')
				pagelist = pagelist.find_all('a', href=True)
				for page in pagelist:
					page = page.get('href')
					page = page.strip('https://www.cnblogs.com/fnng/default.html?page=')
					pages.append(int(page))
				pages.sort(reverse=True)
				maxpage = pages[0]	#获取最大页数
				# print(maxpage)
			print('maxpage==%s'%maxpage)
			print('page=%s'%(page))
			if page == maxpage:
				print('到达最大页数，获取数据完成')
				break	# 当前执行页达到最大页数，跳出循环
	
	# return yichun(), chongshi(), pick()
	return pick()

def testclass():
	'软件测试-接口测试 testclass https://www.testclass.cn'
	headers = {
			"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
			"Cookie":""
		  }
	testclass_url = 'https://www.testclass.cn'
	def testclass_home():
		'首页'
		r = requests.get(url=testclass_url, headers=headers)
		# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		# r.encoding = codestyle	# 指定正确的编码格式
		webcontent = r.text
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		webcontent = soup.find_all('article', class_="aside-item card scrool-item")
		print('#########################首页########################')
		for news in webcontent:
			new = news.find('h2', class_='card-title')
			title = new.select('h2>a')[0].text
			link = new.select('h2>a')[0].get('href')
			print(title, link)
			print('*'*50)

	def testclass_function():
		'功能测试'
		r = requests.get(url=testclass_url+'/category/functional_test', headers=headers)
		# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		# r.encoding = codestyle	# 指定正确的编码格式
		webcontent = r.text
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		webcontent = soup.find_all('article', class_="col-md-6 col-xl-4 category-item")
		print('#########################功能测试########################')
		for news in webcontent:
			new = news.find('h3', class_='text-center')
			title = new.select('h3>a')[0].text
			link = new.select('h3>a')[0].get('href')
			print(title, link)
			print('*'*50)

	def testclass_performance_test():
		'性能测试'
		r = requests.get(url=testclass_url+'/category/performance_test', headers=headers)
		# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		# r.encoding = codestyle	# 指定正确的编码格式
		webcontent = r.text
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		webcontent = soup.find_all('article', class_="col-md-6 col-xl-4 category-item")
		print('#########################性能测试########################')
		for news in webcontent:
			new = news.find('h3', class_='text-center')
			title = new.select('h3>a')[0].text
			link = new.select('h3>a')[0].get('href')
			print(title, link)
			print('*'*50)

	def testclass_security_test():
		'安全测试'
		r = requests.get(url=testclass_url+'/category/security_test', headers=headers)
		# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		# r.encoding = codestyle	# 指定正确的编码格式
		webcontent = r.text
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		webcontent = soup.find_all('article', class_="col-md-6 col-xl-4 category-item")
		print('#########################安全测试########################')
		for news in webcontent:
			new = news.find('h3', class_='text-center')
			title = new.select('h3>a')[0].text
			link = new.select('h3>a')[0].get('href')
			print(title, link)
			print('*'*50)

	def testclass_interface():
		'接口测试'
		r = requests.get(url=testclass_url+'/category/interface_test', headers=headers)
		# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		# r.encoding = codestyle	# 指定正确的编码格式
		webcontent = r.text
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		webcontent = soup.find_all('article', class_="col-md-6 col-xl-4 category-item")
		print('#########################接口测试########################')
		for news in webcontent:
			new = news.find('h3', class_='text-center')
			title = new.select('h3>a')[0].text
			link = new.select('h3>a')[0].get('href')
			print(title, link)
			print('*'*50)

	def testclass_automation_test():
		'自动化测试'
		for i in range(1, 50):
			r = requests.get(url=testclass_url+'/category/automation_test/page/%s'%i, headers=headers)
			# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
			# r.encoding = codestyle	# 指定正确的编码格式
			webcontent = r.text
			if r.status_code == 404:	#超出请求页数，则停止请求
				break
			soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
			webcontent = soup.find_all('article', class_="col-md-6 col-xl-4 category-item")
			print('#########################自动化测试########################')
			for news in webcontent:
				new = news.find('h3', class_='text-center')
				title = new.select('h3>a')[0].text
				link = new.select('h3>a')[0].get('href')
				print(title, link)
				print('*'*50)
	return testclass_interface(), testclass_home(), testclass_function(), testclass_performance_test(), testclass_security_test(), testclass_automation_test()
	# return testclass_automation_test()

def runoob():
	'菜鸟教程 https://www.runoob.com/'
	headers = {
			"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
			"Cookie":""
		  }
	runoob_url = 'https://www.runoob.com/'
	r = requests.get(url=runoob_url, headers=headers)
	# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	# r.encoding = codestyle	# 指定正确的编码格式
	webcontent = r.text
	soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
	soup = soup.find('div', attrs={"class":"col middle-column-home"})
	webcontent = soup.find_all('div', class_=True)
	for module in webcontent:
		modulename = module.select('div>h2')[0].text
		print('模块名称：',modulename)
		modules = module.find_all('a', class_='item-top item-1')
		for news in modules:
			link = news.get('href')
			try:
				title = news.select('a>strong')[0].text
			except:
				break
			print(title, link)
			print('*'*50)

def gitee():
	'码云 https://gitee.com/explore'
	headers = {
			"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
			"Cookie":""
		  }
	gitee_url = 'https://gitee.com/explore'
	def tuijian():
		'推荐项目'
		r = requests.get(url=gitee_url, headers=headers)
		# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		# r.encoding = codestyle	# 指定正确的编码格式
		webcontent = r.text
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		# ------------其他推荐项目------------
		webcontent = soup.find_all('div', class_="explore-custom-categories__container")
		for modules in webcontent:
			modulename = modules.select('div>h3')[0].text
			print('模块名称：',modulename)
			news = modules.find_all('div', class_='item')
			for new in news:

				titlecontent = new.find('div', class_='title-left')
				title = titlecontent.select('div>h3>a')[0].text
				link = titlecontent.select('div>h3>a')[0].get('href')
				contentdesc = new.find('div', class_='project-desc')
				desc = contentdesc.text
				print(title, desc, link)
				print('*'*50)
		# ------------推荐项目------------
		webcontent2 = soup.find('div', class_="nine wide column")
		modulename = webcontent2.select('div>h3')[0].text
		print('模块名称：',modulename)
		news = modules.find_all('div', class_='item')
		for new in news:

			titlecontent = new.find('div', class_='title-left')
			title = titlecontent.select('div>h3>a')[0].text
			link = titlecontent.select('div>h3>a')[0].get('href')
			contentdesc = new.find('div', class_='project-desc')
			desc = contentdesc.text
			print(title, desc, link)
			print('*'*50)
		# ------------今日热门------------
		print('------------今日热门------------')
		daily_trending = soup.find('div', class_='ui tab active')
		daily_trending = daily_trending.find_all('div', class_='explore-trending-projects__list-item')
		for daily in daily_trending:
			titledesc = daily.find('div', class_='title')
			title = titledesc.select('div>a')[0].text
			link = titledesc.select('div>a')[0].get('href')
			description = daily.find('div', class_='description')
			description = description.text
			print(title)			
			print(description)
			print('*'*50)
		# ------------本周热门------------
		print('------------本周热门------------')
		daily_trending = soup.find('div', class_='ui tab')
		daily_trending = daily_trending.find_all('div', class_='explore-trending-projects__list-item')
		for daily in daily_trending:
			titledesc = daily.find('div', class_='title')
			title = titledesc.select('div>a')[0].text
			link = titledesc.select('div>a')[0].get('href')
			description = daily.find('div', class_='description')
			description = description.text
			print(title)			
			print(description)
			print('*'*50)
	return tuijian()

def STCN():
	'证券时报网 http://www.stcn.com/'
	headers = {
			"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
			"Cookie":""
		  }
	stcn_url = 'http://www.stcn.com/'
	def kuaixun():
		'快讯'
		kuaixun_url = 'http://kuaixun.stcn.com'
		for i in range(1, 100):
			r = requests.get(url=kuaixun_url+'/index_%s.shtml'%(i), headers=headers)
			# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
			# r.encoding = codestyle	# 指定正确的编码格式
			webcontent = r.text
			soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
			if i == 1:
				pages = soup.find('div', attrs={'class':"pagelist1"})
				pages = pages.find_all('a', href=True)	# 获取最大页数
				pagelist = []
				for page in pages:
					pagenum = page.text
					pagenum = pagenum.strip('http://kuaixun.stcn.com/index') 
					pagenum = pagenum.strip('.shtml') 
					try:
						pagenum = int(pagenum)
						pagelist.append(pagenum)
					except:
						print('pagenum is not int')
				print(pagelist)
				pagelist.sort(reverse=True)
				maxpage = pagelist[0]
				print(maxpage)
			# ------------获取快讯消息------------
			kuaixun = soup.find('ul', attrs={"id":"news_list2"})
			kuaixun = kuaixun.find_all('li')
			for module in kuaixun:
				timedesc = module.select('li>i')[0].text 	#发布时间
				datedesc = module.select('li>span')[0].text 	#发布日期
				title = module.select('li>a')[0].get('title')
				link = module.select('li>a')[0].get('href')
				print(datedesc, timedesc, title, link)
				print('*'*50)
			if i == maxpage:	#达到最大页数则停止循环
					break

	def hotnews():
		'热点新闻'
		r = requests.get(url=stcn_url, headers=headers)
		# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		# r.encoding = codestyle	# 指定正确的编码格式
		webcontent = r.text
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		webcontent = soup.find('div', class_='maj_left')
		# --------------加粗新闻--------------
		hotnews = webcontent.find_all('h2', href=False)
		for hotnew in hotnews:
			title = hotnew.select('h2>a')[0].text
			link = hotnew.select('h2>a')[0].get('href')
			print(title, link)
		# --------------热点新闻--------------
		news = webcontent.find_all('li')
		for new in news:
			article = new.select('li>a')
			title1 = article[0].text
			link1 = article[0].get('href')
			if len(article) >1:
				title2 = article[1].text
				link2 = article[1].get('href')
				print(title2, link2)
			print(title1, link1)
			print('*'*50)

		# --------------财经要闻--------------
		caijing = soup.find('div', class_='caijing')
		news = caijing.find_all('p')
		for new in news:
			article = new.select('p>a')
			title = article[0].text
			link = article[0].get('href')
			print(title, link)
			print('*'*50)

	def stock():
		'股市'
		stock_url = 'http://stock.stcn.com/'
		r = requests.get(url=stock_url, headers=headers)
		# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		# r.encoding = codestyle	# 指定正确的编码格式
		webcontent = r.text
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		webcontent = soup.find('ul', id='idData')
		hotnews = webcontent.find_all('li')
		for hotnew in hotnews:
			titledesc = hotnew.find('p', class_='tit')
			title = titledesc.select('p>a')[0].get('title')
			link = titledesc.select('p>a')[0].get('href')
			description = hotnew.find('p', class_='exp')
			description = description.text
			print(title, description, link)

	def finance():
		'机构'
		finance_url = 'http://finance.stcn.com/'
		r = requests.get(url=finance_url, headers=headers)
		# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		# r.encoding = codestyle	# 指定正确的编码格式
		webcontent = r.text
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		webcontent = soup.find('div', class_='box_left')
		# --------------头条要闻--------------
		hotnew = webcontent.find('dl', class_='hotNews')
		hotnewt = hotnew.find('dd', class_='tit')
		hotnewtitle = hotnewt.select('dd>a')[0].get('title')
		hotnewlink = hotnewt.select('dd>a')[0].get('href')
		hotnewd = hotnew.find('dd', class_='exp')
		hotnewdesc = hotnewd.text
		hotnews = webcontent.find_all('li')
		print(hotnewtitle, hotnewdesc, hotnewlink)
		# --------------要闻--------------
		topnews = webcontent.find_all('li')
		for hotnew in topnews:
			titledesc = hotnew.find('p', class_='tit')
			title = titledesc.select('p>a')[0].get('title')
			link = titledesc.select('p>a')[0].get('href')
			# description = hotnew.find('p', class_='exp')
			# description = description.text
			print(title, link)	

	def datastcn():
		'数据新闻'
		data_url = 'http://data.stcn.com/'
		r = requests.get(url=data_url, headers=headers)
		# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		# r.encoding = codestyle	# 指定正确的编码格式
		webcontent = r.text
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		# --------------机器人新闻--------------
		webcontent = soup.find('ul', class_='jqr_con')
		topnews = webcontent.find_all('li')
		for hotnew in topnews:
			timedesc = hotnew.select('li>span')[0].text
			title = hotnew.select('li>a')[0].get('title')
			link = hotnew.select('li>a')[0].get('href')
			print(timedesc, title, link)

	def stocktop():
		'龙虎榜单'
		localtion = ['sh', 'sz']	# 交易所
		timedesc = time.time()
		for local in localtion:
			stocktop_url = 'http://data.stcn.com/common27/filepublish/lhb%sListQuery/list/querylist_1.json'%local
			r = requests.get(url=stocktop_url, params={'timestamp': timedesc}, headers=headers)
			
			webcontent = r.text
			webcontent = webcontent.replace("'", '"')
			webcontent = json.loads(webcontent)
			print('证券代码	证券简称	 成交量(万股)  成交金额(万股)  期间涨跌幅(%)  期间换手率(%)  交易开始日  交易截止日  异动原因')
			for stocks in webcontent['data']:
				secucode = stocks['secucode']
				secuabbr = stocks['secuabbr']
				TurnoverVolume = stocks['TurnoverVolume']
				TurnoverValue = stocks['TurnoverValue']
				zdf = stocks['zdf']
				hsl = stocks['hsl']
				TradingStartDate = stocks['TradingStartDate']
				tradingday = stocks['tradingday']
				ms = stocks['ms']
				print(secucode.ljust(6), secuabbr.ljust(6), TurnoverVolume.ljust(12), TurnoverValue.ljust(15), zdf.ljust(12), hsl.ljust(12), TradingStartDate.ljust(10), tradingday.ljust(10), ms)

	def newstock():
		'新股发行'
		timedesc = time.time()
		i = 1
		while 1:
			print('i====',i)
			newstock_url = 'http://data.stcn.com/common27/filepublish/newstockremind/list/querybypage_%s.json'%i
			r = requests.get(url=newstock_url, params={'timestamp': timedesc}, headers=headers)
			
			webcontent = r.text
			webcontent = webcontent.replace("'", '"')
			webcontent = json.loads(webcontent)
			print('证券代码	证券简称	 申购代码  发行总量(万股)  网上发行(万股)  网上申购(万股)  上申所需市值(万股) 申购价格(元)  申购日期 市盈率(倍)  中签率(%)  中签公布日  上市日期  首日涨跌(%)  连续一字板  上市涨跌幅(%)')
			for stocks in webcontent['data']:
				secucode = stocks['SecuCode']
				secuabbr = stocks['SecuAbbr']
				sgdm = stocks['sgdm']
				fxsx = stocks['fxsx']
				wsfx = stocks['wsfx']
				sgsx = stocks['sgsx']
				sgsz = stocks['sgsz']
				sgjg = stocks['sgjg']
				sgrq = (stocks['sgrq']).strip('00:00:00.000')
				fxsyl = stocks['fxsyl']
				wszql = stocks['wszql']
				zqhgbr = (stocks['zqhgbr']).strip('00:00:00.000')
				ssrq = stocks['ssrq']
				if ssrq != '':
					GMT_FORMAT = '%b %d, %Y %I:%M:%S %p'
					mytime = time.strptime(ssrq, GMT_FORMAT)
					ssrq = time.strftime('%Y-%m-%d', mytime)	# 时间格式转换
				srfsd = stocks['srfsd']
				ts = stocks['ts']
				ssfsd = stocks['ssfsd']
				print(secucode.ljust(8), secuabbr.ljust(6), sgdm.ljust(12), fxsx.ljust(15), wsfx.ljust(12), 
					sgsx.ljust(12), sgsz.ljust(15), sgjg.ljust(10), sgrq.ljust(4), fxsyl.ljust(6), wszql.ljust(10), 
					zqhgbr.ljust(10), ssrq.ljust(10), srfsd.ljust(10), ts.ljust(6), ssfsd.ljust(6))
			if i == int(webcontent['pageCount']):
				break
			i += 1

	def datacwbb():
		'高管薪酬'
		'''
		暂时只查了第一页的数据
		'''
		data_url = 'http://info.stcn.com/data/cwbb'
		yearname = 2018	#要查询的年份
		datas = {"cl": 13,"pageNostr": 1,"pages": 183,"pageNostr": 1,"ordernameclause": 32,"secuabbr":"" ,"t_year": yearname,"hydm": 0,"secucode": "代码/简称","gotopages":"" }
		r = requests.post(url=data_url, data=datas, headers=headers)
		# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		# r.encoding = codestyle	# 指定正确的编码格式
		webcontent = r.text
		# print(webcontent)
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		# --------------高管薪酬--------------
		webcontent = soup.find('table', class_='tabstyle5')
		topnews1 = webcontent.find_all('tr', class_=False)
		topnews2 = webcontent.find_all('tr', class_='cover')
		topnews = topnews1 + topnews2
		#print(topnews)
		for hotnew in topnews:
			# print(hotnew)
			secucode = hotnew.select('tr>td')[0].text
			secname = hotnew.select('tr>td')[1].text
			print(secucode, secname)
			# --------------高管薪酬明细--------------
			datas2 = {"cl": 14,"pageNostr": 1,"pages": 1,"pageNostr": 1,"ordernameclause": 32,"secuabbr":secname ,"t_year": yearname,"hydm": 0,"secucode": secucode,"gotopages":"" }
			r = requests.post(url=data_url, data=datas2, headers=headers)
			webcontent = r.text
			soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
			# --------------高管薪酬--------------
			try:
				webcontent = soup.find('table', class_='tabstyle5')
				selery1 = webcontent.find_all('tr', class_=False)
				selery2 = webcontent.find_all('tr', class_='cover')
				selery = selery1 + selery2

				for usercount in selery:
					# print(usercount)
					userno = usercount.select('tr>td')[0].text 	# 高管序号
					username = usercount.select('tr>td')[1].text 	# 高管名字
					userposition = usercount.select('tr>td')[2].text 	# 高管职位
					userselery = usercount.select('tr>td')[3].text 	# 高管薪酬
					userselery = userselery.strip()
					print(userno, username, userposition, userselery)
					print('*'*50)
			except:
				print('暂无数据')
			print('-'*50)

	def hgt():
		'沪股通'
		hgt_url = 'http://hgt.stcn.com/'
		i = 1
		while 1:
			r = requests.get(url=hgt_url+'index_%s.shtml'%i, headers=headers)
			# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
			# r.encoding = codestyle	# 指定正确的编码格式
			webcontent = r.text
			soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
			webcontent = soup.find('div', class_='qh3_con ww')
			# --------------获取最大页数--------------
			pagelist = webcontent.find('div', class_='pagelist')
			pagelist = pagelist.find_all('li')
			pagenum = []
			for page in pagelist:
				num = page.select('li>a')[0].get('href')
				num = num.strip('http://hgt.stcn.com/index_')
				num = num.strip('.shtml')
				try:
					pagenum.append(int(num))
				except:
					pass
			pagenum.sort(reverse=True)
			maxpage = pagenum[0]
			print(maxpage)
			# --------------获取新闻内容--------------
			content = webcontent.find('ul')
			content = content.find_all('li')
			for hotnew in content:
				timedesc = hotnew.select('li>span')[0].text
				title = hotnew.select('li>a')[0].get('title')
				link = hotnew.select('li>a')[0].get('href')
				link = link.strip(' ')
				print(timedesc, title, link)
			if maxpage == i:
				break
			i += 1

	def sgt():
		'深股通'
		sgt_url = 'http://sgt.stcn.com/'
		i = 1
		while 1:
			r = requests.get(url=sgt_url+'index_%s.shtml'%i, headers=headers)
			# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
			# r.encoding = codestyle	# 指定正确的编码格式
			webcontent = r.text
			soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
			webcontent = soup.find('div', class_='qh3_con ww')
			# --------------获取最大页数--------------
			pagelist = webcontent.find('div', class_='pagelist')
			pagelist = pagelist.find_all('li')
			pagenum = []
			for page in pagelist:
				num = page.select('li>a')[0].get('href')
				num = num.strip('http://hgt.stcn.com/index_')
				num = num.strip('.shtml')
				try:
					pagenum.append(int(num))
				except:
					pass
			pagenum.sort(reverse=True)
			maxpage = pagenum[0]
			print(maxpage)
			# --------------获取新闻内容--------------
			content = webcontent.find('ul')
			content = content.find_all('li')
			for hotnew in content:
				timedesc = hotnew.select('li>span')[0].text
				title = hotnew.select('li>a')[0].get('title')
				link = hotnew.select('li>a')[0].get('href')
				link = link.strip(' ')
				print(timedesc, title, link)
			if maxpage == i:
				break
			i += 1

	def chinext():
		'创业板'
		chinext_url = 'http://chinext.stcn.com/'
		i = 1
		while 1:
			r = requests.get(url=chinext_url+'index_%s.shtml'%i, headers=headers)
			# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
			# r.encoding = codestyle	# 指定正确的编码格式
			webcontent = r.text
			soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
			webcontent = soup.find('div', class_='x_tabBox ww')
			# --------------获取最大页数--------------
			pagelist = webcontent.find('div', class_='pagelist')
			pagelist = pagelist.find_all('li')
			pagenum = []
			for page in pagelist:
				num = page.select('li>a')[0].get('href')
				num = num.strip('http://hgt.stcn.com/index_')
				num = num.strip('.shtml')
				try:
					pagenum.append(int(num))
				except:
					pass
			pagenum.sort(reverse=True)
			maxpage = pagenum[0]
			print(maxpage)
			# --------------年报内容--------------
			content = webcontent.find('ul')
			content = content.find_all('li')
			for hotnew in content:
				timedesc = hotnew.select('li>span')[0].text
				title = hotnew.select('li>a')[0].get('title')
				link = hotnew.select('li>a')[0].get('href')
				link = link.strip(' ')
				print(timedesc, title, link)
			if maxpage == i:
				break
			i += 1

	def kcb():
		'科创板'
		kcb_url = 'http://kcb.stcn.com/'
		r = requests.get(url=kcb_url, headers=headers)
		# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		# r.encoding = codestyle	# 指定正确的编码格式
		webcontent = r.text
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		# --------------信息披露--------------
		print('--------------信息披露--------------')
		xinpi = soup.find('div', class_='ind_xinpi clearfix')
		# pagelist = webcontent.find('div', class_='pagelist')
		xinpi_content = xinpi.find_all('li')
		for content in xinpi_content:
			timedesc = content.select('li>span')[0].text
			link = content.select('li>a')[0].get('href')
			title = content.select('li>a')[0].get('title')
			print(timedesc, title, link)
		# --------------发审动态--------------
		print('--------------发审动态--------------')
		fashen = soup.find('div', class_='fashen_dt clearfix')
		# --------------发审动态-表头名称--------------
		fashen_table = fashen.find('table', class_='tabstyle0')
		table_head = fashen_table.find('tr', class_='tabhead0')	#表名
		table_head = table_head.find_all('td')
		names = ''
		for table in table_head:
			headname = table.text 
			names = names+headname+' '*15
		print(names)
		# --------------发审动态-内容解析--------------
		table_content1 = fashen_table.find_all('tr', class_='odd')
		table_content2 = fashen_table.find_all('tr', class_=False)
		# print(table_content1)
		# print(table_content2)
		table_content = table_content1 + table_content2
		
		for content in table_content:
			content = content.find_all('td')
			# print(content)
			newslsit = ''
			for news in content:
				new = news.text 
				newslsit = newslsit+new+' '*7
			print(newslsit)

		# --------------交易所通知--------------
		print('--------------交易所通知--------------')
		jiaoyisuo = soup.find('div', class_='jiaoyisuo clearfix')
		jiaoyisuo = jiaoyisuo.find('div', class_='x_tabBoxW qh2_con clearfix')
		# pagelist = webcontent.find('div', class_='pagelist')
		jiaoyisuo_content = jiaoyisuo.find_all('li')
		for content in jiaoyisuo_content:
			timedesc = content.select('li>span')[0].text
			link = content.select('li>a')[0].get('href')
			title = content.select('li>a')[0].get('title')
			print(timedesc, title, link)

	return kuaixun(), hotnews() ,stock(), finance(), datastcn(), stocktop(), newstock(), datacwbb(), hgt(), sgt(), chinext(), kcb()
	# return kcb()

def sse():
	'上交所 http://www.sse.com.cn/'
	headers = {
			"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
			"Cookie":""
		  }
	sse_url = 'http://www.sse.com.cn/'
	def yunhq():
		'行情'
		now = time.time()
		yunhq_url = 'http://yunhq.sse.com.cn:32041//v1/sh1/list/self/000001_000016_000010_000009_000300'
		datas = {'callback':'jQuery1124017165705535549503_1577172543561', 'select':'code,name,last,chg_rate,amount,open,prev_close', '_':now}
		r = requests.get(url=yunhq_url, params=datas, headers=headers)
		# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		# r.encoding = codestyle	# 指定正确的编码格式
		webcontent = r.text
		# print(webcontent)
		pattern = re.compile('{"date":.*}')
		webcontent = pattern.search(webcontent)
		webcontent = webcontent.group()
		webcontent = json.loads(webcontent)
		print(' 代码  名称  今收  涨跌幅  成交额  今开  昨收')
		for hq in webcontent['list']:
			print(hq)

	def tradedata():
		'股票成交概况'
		now = time.time()
		today = datetime.datetime.now().date()
		tradedata_url = 'http://query.sse.com.cn/marketdata/tradedata/queryNewTradingByProdTypeData.do'
		datas = {'callback':'jsonpCallback34613', 'searchDate':today, 'prodType':'gp', '_':now}
		r = requests.get(url=tradedata_url, params=datas, headers=headers)
		# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		# r.encoding = codestyle	# 指定正确的编码格式
		webcontent = r.text
		print(webcontent)
		pattern = re.compile('{"actionErrors":.*}')
		webcontent = pattern.search(webcontent)
		webcontent = webcontent.group()
		webcontent = json.loads(webcontent)
		# print(' 代码  名称  今收  涨跌幅  成交额  今开  昨收')
		for hq in webcontent['result']:
			print(hq)

	def webupdate():
		'各栏更新'
		webupdate_url = 'http://www.sse.com.cn/home/webupdate/'
		i = 1
		while 1:
			if i==1:
				tishurl = 's_index.htm'
			else:
				tishurl = 's_index_%s.htm'%i
			r = requests.get(url=webupdate_url+tishurl, headers=headers)
			webcontent = r.text
			soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
			# 获取总页数
			webcontent = soup.find('div', id='sse_list_1')
			pagecount = soup.find('div', id='createPage')
			pagecount = pagecount.get("page_count")
			print(pagecount)
			# 解析内容
			contents = webcontent.find_all('dd')
			for new in contents:
				timedesc = new.select('dd>span')[0].text 
				title = new.select('dd>a')[0].get('title') 
				link = new.select('dd>a')[0].get('href') 
				print(timedesc, title.encode('ISO-8859-1').decode('utf-8'), link)
				# print('*'*50)
			if i == int(pagecount):
				print('最后一页获取完成')
				break
			else:
				i += 1

	def hotandd():
		'热点动态'
		hotandd_url = 'http://www.sse.com.cn/aboutus/mediacenter/hotandd/'
		i = 1
		while 1:
			if i==1:
				tishurl = 's_index.htm'
			else:
				tishurl = 's_index_%s.htm'%i
			r = requests.get(url=hotandd_url+tishurl, headers=headers)
			webcontent = r.text
			soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
			# 获取总页数
			webcontent = soup.find('div', id='sse_list_1')
			pagecount = soup.find('div', id='createPage')
			pagecount = pagecount.get("page_count")
			print(pagecount)
			# 解析内容
			contents = webcontent.find_all('dd')
			for new in contents:
				timedesc = new.select('dd>span')[0].text 
				title = new.select('dd>a')[0].get('title') 
				link = new.select('dd>a')[0].get('href') 
				print(timedesc, title.encode('ISO-8859-1').decode('utf-8'), link)
				# print('*'*50)
			if i == int(pagecount):
				print('最后一页获取完成')
				break
			else:
				i += 1

	def SpecialTips():
		'停复牌提示'
		now = time.time()
		today = datetime.datetime.now().date()
		tips_url = 'http://query.sse.com.cn/infodisplay/querySpecialTipsInfoByPage.do'
		datas = {
			'jsonCallBack':'jsonpCallback18562', 
			'isPagination':'true',
			'searchDate':today,
			'bgFlag':1,
			'searchDo':1,
			'pageHelp.pageSize':25,
			'pageHelp.pageNo':1,
			'pageHelp.beginPage':1,
			'pageHelp.cacheSize':1,
			'pageHelp.endPage':5,
			 '_':now
			 }
		headers['Referer'] = 'http://www.sse.com.cn/disclosure/dealinstruc/suspension/'
		r = requests.get(url=tips_url, params=datas, headers=headers)
		webcontent = r.text
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		webcontent = r.text
		# print(webcontent)
		pattern = re.compile('{"bgFlag":.*}')
		webcontent = pattern.search(webcontent)
		webcontent = webcontent.group()
		contents = json.loads(webcontent)
		# 解析内容
		print('证券代码    证券简称    停(复)牌时间    停牌期限							停(复)牌原因')
		for new in contents['result']:
			productCode = new['productCode']
			productName = new['productName']
			stopTime = new['stopTime']	# 停牌期限
			stopReason = new['stopReason']	#停(复)牌原因
			stopDate = new['stopDate']	#停复牌时间
			print(productCode.ljust(10), productName.ljust(8), stopDate.ljust(12), stopTime.ljust(35), stopReason)
			# print('*'*50)

	def calendar():
		'市场日历-查询市场信息'
		now = time.time()
		today = time.strftime('%Y%m%d')
		calendar_url = 'http://query.sse.com.cn/commonSoaQuery.do'
		datas = {
			'jsonCallBack':'jQuery112408916959178676822_1577235664059', 
			'isPagination':'true',
			'order':'tradeBeginDate|desc,stockCode|desc',
			'tradeBeginDate':today,
			'tradeEndDate':today,
			'sqlId':'PL_SCRL_SCRLB',
			'bizType':4,	# 1-IPO信息，7-停复牌信息，5-分红送转/除权除息，4-股东大会，3-e访谈信息，2-路演信息，
			'pageHelp.pageSize':25,
			'pageHelp.pageNo':1,
			'pageHelp.beginPage':1,
			'pageHelp.cacheSize':1,
			'pageHelp.endPage':5,
			 '_':now
			 }
		headers['Referer'] = 'http://www.sse.com.cn/disclosure/dealinstruc/calendar/'
		r = requests.get(url=calendar_url, params=datas, headers=headers)
		webcontent = r.text
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		webcontent = r.text
		# print(webcontent)
		pattern = re.compile('{"actionErrors":.*}')
		webcontent = pattern.search(webcontent)
		webcontent = webcontent.group()
		contents = json.loads(webcontent)
		# 解析内容
		for new in contents['result']:
			print(new)
			print('*'*50)

	def announcement():
		'基金公告'
		announcement_url = 'http://www.sse.com.cn/disclosure/fund/announcement/'
		r = requests.get(url=announcement_url, headers=headers)
		codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		r.encoding = codestyle	# 指定正确的编码格式
		webcontent = r.text
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		xinpi = soup.find('div', class_='sse_list_1')
		# pagelist = webcontent.find('div', class_='pagelist')
		xinpi_content = xinpi.find_all('dd')
		for content in xinpi_content:
			timedesc = content.select('dd>span')[0].text
			link = content.select('dd>a')[0].get('href')
			title = content.select('dd>a')[0].get('title')
			print(timedesc, title, link)
			print('*'*50)

	return yunhq(), tradedata(), webupdate(), hotandd(), SpecialTips(), calendar(), announcement()
	# return announcement()

def szse():
	'深交所 http://www.szse.cn/'
	headers = {
			"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
			"Cookie":""
		  }
	szse_url = 'http://www.szse.cn/'
	def tech_guide():
		'技术指南 http://www.szse.cn/marketServices/technicalservice/guide'
		guide_url = 'http://www.szse.cn/api/search/content'
		# while 1:
		datas = {'keyword':'', 'time':0, 'range':'title', 'channelCode[]':'technicalGuide_hidden', 'currentPage':1, 'pageSize':20}
		i = 1
		while 1:
			datas['currentPage'] = i
			r = requests.post(url=guide_url, data=datas,params={'random':'0.6115615140687631'}, headers=headers)
			# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
			# r.encoding = codestyle	# 指定正确的编码格式
			# print(r.text)
			webcontent = r.json()
			for content in webcontent['data']:
				doctitle = content['doctitle']
				docpuburl = content['docpuburl']
				docpubtime = content['docpubtime']
				# 将时间格式化成YY-MM-DD格式
				docpubtime = str(docpubtime).strip('000')
				docpubtime = time.localtime(int(docpubtime))
				docpubtime = time.strftime("%Y-%m-%d", docpubtime)
				print(docpubtime ,doctitle, docpuburl)
				print('*'*50)
			pageSize = webcontent['pageSize']
			totalSize = webcontent['totalSize']
			if pageSize*i > totalSize:
				print('请求完成')
				break
			else:
				i += 1

	def tech_notice():
		'技术公告 http://www.szse.cn/marketServices/technicalservice/notice/'
		notice_url = 'http://www.szse.cn/api/search/content'
		# while 1:
		datas = {'keyword':'', 'time':0, 'range':'title', 'channelCode[]':'technicalLatestNotice', 'currentPage':1, 'pageSize':20}
		i = 1
		while 1:
			datas['currentPage'] = i
			r = requests.post(url=notice_url, data=datas,params={'random':'0.6115615140687631'}, headers=headers)
			# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
			# r.encoding = codestyle	# 指定正确的编码格式
			# print(r.text)
			webcontent = r.json()
			for content in webcontent['data']:
				doctitle = content['doctitle']
				docpuburl = content['docpuburl']
				docpubtime = content['docpubtime']
				# 将时间格式化成YY-MM-DD格式
				docpubtime = docpubtime//1000	#去掉最后三个0
				docpubtime = time.localtime(int(docpubtime))
				docpubtime = time.strftime("%Y-%m-%d", docpubtime)
				print(docpubtime ,doctitle, docpuburl)
				print('*'*50)
			
			pageSize = webcontent['pageSize']
			totalSize = webcontent['totalSize']
			print(pageSize, totalSize)
			if pageSize*i > totalSize:
				print('请求完成')
				break
			else:
				i += 1

	def dataInterface():
		'数据接口 http://www.szse.cn/marketServices/technicalservice/interface/'
		notice_url = 'http://www.szse.cn/api/search/content'
		# while 1:
		datas = {'keyword':'', 'time':0, 'range':'title', 'channelCode[]':'dataInterface_hidden', 'currentPage':1, 'pageSize':20}
		i = 1
		while 1:
			datas['currentPage'] = i
			r = requests.post(url=notice_url, data=datas,params={'random':'0.6115615140687631'}, headers=headers)
			# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
			# r.encoding = codestyle	# 指定正确的编码格式
			# print(r.text)
			webcontent = r.json()
			for content in webcontent['data']:
				doctitle = content['doctitle']
				docpuburl = content['docpuburl']
				docpubtime = content['docpubtime']
				# 将时间格式化成YY-MM-DD格式
				docpubtime = docpubtime//1000	#去掉最后三个0
				docpubtime = time.localtime(int(docpubtime))
				docpubtime = time.strftime("%Y-%m-%d", docpubtime)
				print(docpubtime ,doctitle, docpuburl)
				print('*'*50)
			pageSize = webcontent['pageSize']
			totalSize = webcontent['totalSize']
			if pageSize*i > totalSize:
				print('请求完成')
				break
			else:
				i += 1

	# return tech_guide(), tech_notice(), dataInterface()
	return dataInterface()

def chouti():
	'抽屉新热榜 https://dig.chouti.com/'
	headers = {
			"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
			"Cookie":""
		  }
	chouti_url = 'https://dig.chouti.com'
	now = time.time()
	def tophot():
		'热榜'
		hottime = ['24hr', '72hr', '168hr']
		for tt in hottime:
			r = requests.get(url=chouti_url+'/top/%s'%tt, params={'_':now}, headers=headers)
			webcontent = r.json()
			print('+++++++++++++++%s热榜+++++++++++++++'%tt)
			for modules in webcontent['data']:
				title = modules['title']
				link = modules['originalUrl']
				print(title, link)
				print('*'*50)

	return tophot()

def kanshangjie():
	'商界 http://www.kanshangjie.com/'
	headers = {
			"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
			"Cookie":""
		  }
	chouti_url = 'http://www.kanshangjie.com/api.php'
	def jingxuan():
		'精选'
		r = requests.get(url=chouti_url, params={'op':'util_api', 'ac':'autoload', 'p':1, 'catid':3670, 'q':''}, headers=headers)
		webcontent = r.json()
		# print('+++++++++++++++热榜+++++++++++++++')
		for modules in webcontent:
			title = modules['title']
			link = modules['url']
			print(title, link)
			print('*'*50)

	def kuaisun():
		'24h快讯'
		url = 'http://www.kanshangjie.com/'
		r = requests.get(url=url, headers=headers)
		codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		r.encoding = codestyle	# 指定正确的编码格式
		webcontent = r.text
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		xinpi = soup.find('div', class_='hours')
		# pagelist = webcontent.find('div', class_='pagelist')
		xinpi_content = xinpi.find_all('li')
		for content in xinpi_content:
			try:
				link = content.select('li>a')[0].get('href')
				title = content.select('li>a')[0].text
				print(title, link)
				print('*'*50)
			except:
				break

	return jingxuan(), kuaisun()

def feiyan():
	'新型肺炎疫情数据'
	headers = {
			"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
			"Cookie":""
		  }

	def feiyan_163():
		'来自163的数据'
		url = 'https://c.m.163.com/ug/api/wuhan/app/data/list-total'
		r = requests.get(url=url, headers=headers)
		webcontent = r.json()
		chinatotal = r.json()['data']['chinaTotal']['total']
		chinatotay = r.json()['data']['chinaTotal']['today']
		total = chinatotal['confirm']
		dead = chinatotal['dead']
		heal = chinatotal['heal']
		suspect = chinatotal['suspect']

		total_new = chinatotay['confirm']
		dead_new = chinatotay['dead']
		heal_new = chinatotay['heal']
		suspect_new = chinatotay['suspect']
		print(total_new,dead_new,heal_new,suspect_new)
		print('确诊：{}-{}，疑似：{}-{}，死亡：{}-{}，治愈：{}-{}'.format(total,total_new,suspect,suspect_new,dead,dead_new,heal,heal_new))

	def feiyan_ndb():
		'来自每日经济网的数据'
		today = datetime.date.today()
		url = 'http://www.nbd.com.cn/zhuanti/feiyan_day_records.json'
		r = requests.get(url=url, headers=headers)
		webcontent = r.json()['records']
		for data in webcontent:
			record_date = data['record_date']
			total = data['certain']
			total_new = data['certain_incr']
			dead = data['death']
			heal = data['cure']
			suspect = data['uncertain']
			suspect_new = data['uncertain_incr']
			severe = data['severe']
			severe_new = data['severe_incr']
			print('时间：{}，确诊：{}-{}，疑似：{}-{}，死亡：{}，治愈：{}，重症{}-{}'.format(record_date,total,total_new,suspect,suspect_new,dead,heal,severe,severe_new))
	def feiyan_ndb_article():
		'来自每日经济网的数据_权威发布'
		url = 'http://www.nbd.com.cn/columns/1190/articles_list_for_zhuanti.json'
		datas = {'with_content':1, 'per':50, 'page_index':1}
		r = requests.get(url=url, params=datas ,headers=headers)
		webcontent = r.json()
		for new in webcontent:
			title = new['title']
			link = new['article_url']
			publish_time = new['additional_text']
			print(publish_time, title, link)

	def feiyan_ndb_anosugartech():
		'来自每日经济网的数据_确诊信息'
		url = 'http://2019ncov.nosugartech.com/data.json'
		r = requests.get(url=url, headers=headers)
		webcontent = r.json()['data']
		for new in webcontent:
			title1 = new['t_no']
			title2 = new['t_no_sub']
			title3 = new['t_pos_end']
			title4 = new['t_pos_start']
			who = new['who']
			publish_time = new['t_end']
			print(title1, title2, title3, title4, who, publish_time)

	def feiyan_ndb_world():
		'来自每日经济网的数据_全球信息'
		url = 'http://www.nbd.com.cn/zhuanti/cfg_stores/get_by_activity_name'
		datas = {'activity_name':'2020feiyan_peaple_world', 'cfg_type':'array'}
		r = requests.get(url=url, params=datas, headers=headers)
		webcontent = r.json()['cfg']
		print('地区  确诊  死亡  治愈')
		for new in webcontent:
			provinceName = new['provinceName']
			confirmedCount = new['confirmedCount']
			deadCount = new['deadCount']
			curedCount = new['curedCount']
			print(provinceName, confirmedCount, deadCount, curedCount)

	def feiyan_ndb_china():
		'来自每日经济网的数据_国内信息'
		url = 'http://www.nbd.com.cn/zhuanti/cfg_stores/get_by_activity_name'
		datas = {'activity_name':'2020feiyan_peaple_province', 'cfg_type':'array'}
		r = requests.get(url=url, params=datas, headers=headers)
		webcontent = r.json()['cfg']
		print('地区  确诊  死亡  治愈')
		for new in webcontent:
			provinceName = new['provinceName']
			confirmedCount = new['confirmedCount']
			deadCount = new['deadCount']
			curedCount = new['curedCount']
			print(provinceName, confirmedCount, deadCount, curedCount)

	# return feiyan_163(), feiyan_ndb(), feiyan_ndb_article(), feiyan_ndb_anosugartech(), feiyan_ndb_world(), feiyan_ndb_china()
	return feiyan_ndb_world(),feiyan_ndb_china()

def fortunechina():
		'财富'
		headers = {
			"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
			"Cookie":""
		  }
		def world500():
			'2019世界500强'
			url = 'http://www.fortunechina.com/fortune500/c/2019-07/22/content_339535.htm'
			r = requests.get(url=url, headers=headers)
			codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
			r.encoding = codestyle	# 指定正确的编码格式
			webcontent = r.text
			soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
			xinpi = soup.find('table', id='yytable')
			xinpi_content = xinpi.find('tbody')
			# print(xinpi_content)
			contents = xinpi_content.find_all('tr')
			# print(contents)
			print('排名 上年排名  公司名称    营收(百万美元)    利润(百万美元)    国家')
			for content in contents:
				# print(content)
				items = content.find_all('td')
				ranking = items[0].text 	# 排名
				ranking_last = items[1].text 	# 去年排名
				name = items[2].text 	# 公司
				revenue = items[3].text 	# 营收
				profit = items[4].text 	#利润
				country = items[5].text 	#国家
				print(ranking+''*5, ranking_last, name, revenue, profit, country)
				print('*'*50)

		def china500():
			'2019中国500强'
			url = 'http://www.fortunechina.com/fortune500/c/2019-07/10/content_337536.htm'
			r = requests.get(url=url, headers=headers)
			codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
			r.encoding = codestyle	# 指定正确的编码格式
			webcontent = r.text
			soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
			xinpi = soup.find('table', id='table1')
			xinpi_content = xinpi.find('tbody')
			contents = xinpi_content.find_all('tr')
			print('排名 上年排名  公司名称    营收(百万元)    利润(百万元)')
			for content in contents:
				# print(content)
				items = content.find_all('td')
				ranking = items[0].text 	# 排名
				ranking_last = items[1].text 	# 去年排名
				name = items[2].text 	# 公司
				revenue = items[3].text 	# 营收
				profit = items[4].text 	#利润
				print(ranking+''*5, ranking_last, name, revenue, profit)
				print('*'*50)

		def china500_deficit():
			'2019中国500强中的亏损企业'
			url = 'http://www.fortunechina.com/fortune500/c/2019-07/10/content_337559.htm'
			r = requests.get(url=url, headers=headers)
			codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
			r.encoding = codestyle	# 指定正确的编码格式
			webcontent = r.text
			soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
			xinpi = soup.find('table', class_='rankingtable')
			xinpi_content = xinpi.find('tbody')
			contents = xinpi_content.find_all('tr')
			# print('排名 公司名称   亏损金额(百万元)')
			for content in contents[1:]:
				# print(content)
				items = content.find_all('td')
				ranking = items[0].text 	# 排名
				name = items[1].text 	# 公司
				profit = items[2].text 	#利润
				print(ranking+''*5, name, profit)
				print('*'*50)

		def china500_profit():
			'2019中国500强中利润最高的企业'
			url = 'http://www.fortunechina.com/fortune500/c/2019-07/10/content_337557.htm'
			r = requests.get(url=url, headers=headers)
			codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
			r.encoding = codestyle	# 指定正确的编码格式
			webcontent = r.text
			soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
			xinpi = soup.find('table', class_='rankingtable')
			xinpi_content = xinpi.find('tbody')
			contents = xinpi_content.find_all('tr')
			print('排名 公司名称  利润率')
			for content in contents[1:]:
				# print(content)
				items = content.find_all('td')
				ranking = items[0].text 	# 排名
				name = items[1].text 	# 公司
				profit = items[2].text 	#利润
				print(ranking+''*5, name, profit)
				print('*'*50)
		return world500(), china500(), china500_deficit(), china500_profit()

def huanqiu():
	'环球网 https://www.huanqiu.com/'
	headers = {
			"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
			"Cookie":""
		  }

	def chiannews():
		'国内新闻'
		url = 'https://china.huanqiu.com/api/list'
		datas = {'offset':0, 'limit':40}
		r = requests.get(url=url, headers=headers, params=datas)
		webcontent = r.json()
		# print(webcontent)
		for new in webcontent['list']:
			if len(new)  == 0:
				break
			else:
				title = new['title']
				summary = new['summary']
				link = 'https://china.huanqiu.com/article/'+new['aid']
				print(title, summary, link)
				print('*'*50)

	def worldnews():
		'国际新闻'
		url = 'https://world.huanqiu.com/api/list'
		datas = {'offset':0, 'limit':40}
		r = requests.get(url=url, headers=headers, params=datas)
		webcontent = r.json()
		# print(webcontent)
		for new in webcontent['list']:
			if len(new)  == 0:
				break
			else:
				title = new['title']
				summary = new['summary']
				link = 'https://world.huanqiu.com/article/'+new['aid']
				print(title, summary, link)
				print('*'*50)
	
	return chiannews(), worldnews()

def  traffic():
	'交通安全综合服务管理平台-上海'
	url = 'https://sh.122.gov.cn/'
	r = requests.post(url=url+'m/page/publicity/list', headers=headers)
	webcontent = r.json()['data']
	# print(webcontent)
	# -----------业务热点-----------
	manuals = webcontent['manuals']
	for new in manuals:
		print(new['wjm'], url+new['wjlj'])
	# -----------信息公告-----------
	bulletions = webcontent['bulletions']
	for new in bulletions:
		print(new['wjm'], new['scsj'], url+new['wjlj'])
	# -----------信息公布-----------
	publishs = webcontent['publishs']
	for new in publishs:
		print(new['wjm'], new['scsj'], url+new['wjlj'])

	# 交管动态
	datas = {'path':'jgdt', 'page':1, 'size':50}
	r = requests.post(url=url+'m/page/news/getDetails', data=datas, headers=headers)

	webcontent = r.json()['data']['pageList']['list']
	print('-'*20,'交管动态','-'*20)
	for new in webcontent:
		title = new['title']
		link = url+new['link']
		releasedate = new['releasDate']
		print(title, releasedate, link)

	# 警示教育
	datas['path']='jsjy'
	r = requests.post(url=url+'m/page/news/getDetails', data=datas, headers=headers)

	webcontent = r.json()['data']['pageList']['list']
	print('-'*20,'警示教育','-'*20)
	for new in webcontent:
		title = new['title']
		link = url+new['link']
		releasedate = new['releasDate']
		print(title, releasedate, link)

def police_gov():
	'中华人民共和国公安部'
	headers['Cookie'] = "maxPageNum5097045=265; __jsluid_h=dfabaa396a9ed9f7b7ef8fb3cec53cf8; __jsluid_s=7bac328a51598b8152d0510fe02003d7; zh_choose=n; __FTabceffgh=2020-2-18-15-28-6; __NRUabceffgh=1582010886328; __RTabceffgh=2020-2-18-15-28-6; __jsl_clearance=1582078286.144|0|IteI1qyai4zO%2B4sF4%2F%2F7vsRA%2Bag%3D"
	url = 'https://www.mps.gov.cn/'
	# --------------公安要闻--------------
	r = requests.get(url=url+'n2253534/n2253535/index.html', headers=headers)
	codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	r.encoding = codestyle	# 指定正确的编码格式
	# print(codestyle)
	webcontent = r.text
	soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
	print('-'*20,'公安要闻','-'*20)
	xinpi = soup.find('span', id='comp_5097045')
	# xinpi_content = xinpi.find('tbody')
	contents = xinpi.find_all('dd')
	#print(contents)
	for content in contents:
		releasedate = content.select('span')[0].text
		releasedate = releasedate.strip('()')
		title = content.find('a').text
		link = content.find('a').get('href')
		link = link.replace('../../', url)
		print(releasedate, title, link)

	# --------------各地警务--------------
	r = requests.get(url=url+'n2253534/n4904351/index.html', headers=headers)
	codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	r.encoding = codestyle	# 指定正确的编码格式
	# print(codestyle)
	webcontent = r.text
	soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
	print('-'*20,'各地警务','-'*20)
	xinpi = soup.find('span', id='comp_3497341')
	# xinpi_content = xinpi.find('tbody')
	contents = xinpi.find_all('dd')
	#print(contents)
	for content in contents:
		releasedate = content.select('span')[0].text
		releasedate = releasedate.strip('()')
		title = content.find('a').text
		link = content.find('a').get('href')
		link = link.replace('../../', url)
		print(releasedate, title, link)

	# --------------工作动态--------------
	r = requests.get(url=url+'n2254098/n4904352/index.html', headers=headers)
	codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	r.encoding = codestyle	# 指定正确的编码格式
	# print(codestyle)
	webcontent = r.text
	soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
	print('-'*20,'工作动态','-'*20)
	xinpi = soup.find('span', id='comp_3497341')
	# xinpi_content = xinpi.find('tbody')
	contents = xinpi.find_all('dd')
	#print(contents)
	for content in contents:
		releasedate = content.select('span')[0].text
		releasedate = releasedate.strip('()')
		title = content.find('a').text
		link = content.find('a').get('href')
		link = link.replace('../../', url)
		print(releasedate, title, link)

	# --------------警方提示--------------
	r = requests.get(url=url+'n2253534/n2253543/index.html', headers=headers)
	codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	r.encoding = codestyle	# 指定正确的编码格式
	# print(codestyle)
	webcontent = r.text
	soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
	print('-'*20,'警方提示','-'*20)
	xinpi = soup.find('span', id='comp_3497341')
	# xinpi_content = xinpi.find('tbody')
	contents = xinpi.find_all('dd')
	#print(contents)
	for content in contents:
		releasedate = content.select('span')[0].text
		releasedate = releasedate.strip('()')
		title = content.find('a').text
		link = content.find('a').get('href')
		link = link.replace('../../', url)
		print(releasedate, title, link)

	# --------------人事信息--------------
	r = requests.get(url=url+'n2254314/n4904354/index.html', headers=headers)
	codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	r.encoding = codestyle	# 指定正确的编码格式
	# print(codestyle)
	webcontent = r.text
	soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
	print('-'*20,'人事信息','-'*20)
	xinpi = soup.find('span', id='comp_3497341')
	# xinpi_content = xinpi.find('tbody')
	contents = xinpi.find_all('dd')
	#print(contents)
	for content in contents:
		releasedate = content.select('span')[0].text
		releasedate = releasedate.strip('()')
		title = content.find('a').text
		link = content.find('a').get('href')
		link = link.replace('../../', url)
		print(releasedate, title, link)

def yangmaoduo():
	'薅羊毛'
	url = 'http://www.yangmaoduo.com/'
	# --------------获取每页的url--------------
	r = requests.get(url=url, headers=headers)
	codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	r.encoding = codestyle	# 指定正确的编码格式
	# print(codestyle)
	webcontent = r.text
	soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
	xinpi = soup.find('div', class_='pagebar')
	# xinpi_content = xinpi.find('tbody')
	contents = xinpi.find_all('a', href=True)
	# print(contents)
	pagenum = 1
	for content in contents:
		page = content.get('href')	# 获取翻页的url

		print('正在获取第{}页,url={}'.format(pagenum,page))
		# --------------页面内容--------------
		r = requests.get(url=page, headers=headers)
		codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		r.encoding = codestyle	# 指定正确的编码格式
		# print(codestyle)
		webcontent = r.text
		pagenum += 1
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		xinpi = soup.find('div', id='lieb')
		# xinpi_content = xinpi.find('tbody')
		contents = xinpi.find_all('dl')
		# print(contents)
		for content in contents:
			#print(content)
			title = content.select('dl>dt>h2>a')[0].text
			link = content.select('dl>dt>h2>a')[0].get('href')
			desc = content.select('dl>dd>p')[0].text
			print(title, desc, link)

def xianbao():
	'线报网'
	url = 'https://www.52xianbao.com/'
	for i in range(1,4):
		'请求前三页数据'
		r = requests.get(url=url+'/page/%s'%i, headers=headers)
		print('正在获取第{}页,url={}'.format(i,r.url))
		codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		r.encoding = codestyle	# 指定正确的编码格式
		# print(codestyle)
		webcontent = r.text
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		contents = soup.find_all('article', class_=True)
		for content in contents:
			news = content.find('h2')
			new = news.find_all('a')
			if len(new) > 1:
				title = new[1].text
				link = new[1].get('href')
			else:
				title = new[0].text
				link = new[0].get('href')
			print(title, link)

def card111():
	'信用卡论坛'
	url = 'https://www.card111.com/'
	# --------------热门帖子--------------
	print('-'*20,'热门帖子','-'*20)
	r = requests.get(url=url+'forum.php', headers=headers)
	codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	r.encoding = codestyle	# 指定正确的编码格式
	# print(codestyle)
	webcontent = r.text
	soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
	xinpi = soup.find('div', id='portal_block_107')
	contents = xinpi.find_all('li')
	for content in contents:
		new = content.find_all('a')
		title = new[1].text
		link = new[1].get('href')
		desc = new[0].text
		print(desc, title, link)

	# --------------资讯--------------
	print('-'*20,'资讯','-'*20)
	datas = {'mod':'list', 'catid':2}
	r = requests.get(url=url+'portal.php', params=datas, headers=headers)
	codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	r.encoding = codestyle	# 指定正确的编码格式
	# print(codestyle)
	webcontent = r.text
	soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
	xinpi = soup.find('div', class_='deanpiclist top15')
	contents = xinpi.find_all('li')
	for content in contents:
		new = content.select('li>div>div')[1]
		title = new.select('div>h2')[0].text
		link = new.select('div>h2')[0].get('href')
		print(title, link)

def earnews():
	'赚钱资讯网'
	url = 'https://www.earnews.cn/'
	# --------------最新资讯--------------
	print('-'*20,'最新资讯','-'*20)
	r = requests.get(url=url+'article/index.html', headers=headers)
	codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	r.encoding = codestyle	# 指定正确的编码格式
	# print(codestyle)
	webcontent = r.text
	soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
	xinpi = soup.find('div', class_='art_sheet list')
	contents = xinpi.find_all('div', style='padding-bottom:5px;padding-left:0px;float:left;')
	for content in contents:
		new = content.select('div>a')[0]
		title = new.get('title')
		link = new.get('href')
		print(title, link)

	# --------------最新文章--------------
	print('-'*20,'最新文章','-'*20)
	tuijian = soup.find_all('div', class_='box list')[2]
	tuijian = tuijian.find('div', class_='main')
	contents = tuijian.find_all('div')
	for content in contents:
		title = content.select('a')[0].get('title')
		link = content.select('a')[0].get('href')
		link = url+link
		print(title, link)

	# --------------推荐文章--------------
	print('-'*20,'推荐文章','-'*20)
	tuijian = soup.find_all('div', class_='box list')[4]
	tuijian = tuijian.find('div', class_='main')
	contents = tuijian.find_all('div')
	for content in contents:
		title = content.select('a')[0].get('title')
		link = content.select('a')[0].get('href')
		link = url+link
		print(title, link)

	# --------------金融理财--------------
	print('-'*20,'金融理财','-'*20)
	r = requests.get(url=url+'article/cat-1/index.html', headers=headers)
	codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	r.encoding = codestyle	# 指定正确的编码格式
	# print(codestyle)
	webcontent = r.text
	soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
	xinpi = soup.find('div', class_='art_sheet list')
	contents = xinpi.find_all('div', style='padding-bottom:5px;padding-left:0px;float:left;')
	for content in contents:
		new = content.select('div>a')[0]
		title = new.get('title')
		link = new.get('href')
		print(title, link)

	# --------------应用频道--------------
	print('-'*20,'应用频道','-'*20)
	r = requests.get(url=url+'article/cat-2/index.html', headers=headers)
	codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	r.encoding = codestyle	# 指定正确的编码格式
	# print(codestyle)
	webcontent = r.text
	soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
	xinpi = soup.find('div', class_='art_sheet list')
	contents = xinpi.find_all('div', style='padding-bottom:5px;padding-left:0px;float:left;')
	for content in contents:
		new = content.select('div>a')[0]
		title = new.get('title')
		link = new.get('href')
		print(title, link)

	# --------------红包频道--------------
	print('-'*20,'红包频道','-'*20)
	r = requests.get(url=url+'article/cat-3/index.html', headers=headers)
	codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	r.encoding = codestyle	# 指定正确的编码格式
	# print(codestyle)
	webcontent = r.text
	soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
	xinpi = soup.find('div', class_='art_sheet list')
	contents = xinpi.find_all('div', style='padding-bottom:5px;padding-left:0px;float:left;')
	for content in contents:
		new = content.select('div>a')[0]
		title = new.get('title')
		link = new.get('href')
		print(title, link)

	# --------------话费频道--------------
	print('-'*20,'话费频道','-'*20)
	r = requests.get(url=url+'article/cat-4/index.html', headers=headers)
	codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	r.encoding = codestyle	# 指定正确的编码格式
	# print(codestyle)
	webcontent = r.text
	soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
	xinpi = soup.find('div', class_='art_sheet list')
	contents = xinpi.find_all('div', style='padding-bottom:5px;padding-left:0px;float:left;')
	for content in contents:
		new = content.select('div>a')[0]
		title = new.get('title')
		link = new.get('href')
		print(title, link)

	# --------------流量频道--------------
	print('-'*20,'流量频道','-'*20)
	r = requests.get(url=url+'article/cat-5/index.html', headers=headers)
	codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	r.encoding = codestyle	# 指定正确的编码格式
	# print(codestyle)
	webcontent = r.text
	soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
	xinpi = soup.find('div', class_='art_sheet list')
	contents = xinpi.find_all('div', style='padding-bottom:5px;padding-left:0px;float:left;')
	for content in contents:
		new = content.select('div>a')[0]
		title = new.get('title')
		link = new.get('href')
		print(title, link)

def maoqiu():
	'毛球'
	url = 'http://www.maoqiuapp.com/'
	datas = {'pageNum':1, 'pageSize':20, 'status':2, 'time':''}
	r = requests.post(url=url+'v1/dashboard/edit', headers=headers, data=datas)
	webcontent = r.json()['data']
	# print(webcontent)
	for new in webcontent['list']:
		title = new['title']
		likeCount = new['likeCount']
		link = new['shareUrl']
		print(title, likeCount, link)
		# print('*'*50)

def cnbeta():
	'cnbeta'
	url = 'https://m.cnbeta.com'
	# --------------业界--------------
	print('-'*20,'业界','-'*20)
	r = requests.get(url=url, headers=headers)
	codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	r.encoding = codestyle	# 指定正确的编码格式
	# print(codestyle)
	webcontent = r.text
	soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
	xinpi = soup.find_all('ul', class_='info_list')
	for block in xinpi:
		contents = block.find_all('li')
		#print(contents)
		for content in contents:
			new = content.select('li>p>a')
			if len(new) >0:
				new = new[0]
				title = new.select('a>img')[0].get('alt')
				link = new.get('href')
				link = url+link
				print(title, link)

def webservices():
	from suds.client import Client
	from suds.xsd.doctor import ImportDoctor, Import
	'Web Services接口调用 http://www.webxml.com.cn/zh_cn/web_services.aspx'
	def mobilecode():
		'手机号归属地查询'
		url = 'http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'	#号码归属地
		client = Client(url)
		print(client)
		result = client.service.getMobileCodeInfo('18516292278')
		print(result)

	def funddata():
		'基金信息'
		url = 'http://ws.webxml.com.cn/WebServices/ChinaOpenFundWS.asmx?WSDL'	#开放基金信息
		imp = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
		imp.filter.add('http://WebXml.com.cn/')
		doctor = ImportDoctor(imp)	# 显示的制定调用标准
		# client = Client(url, plugins=[ImportDoctor(imp)])
		client = Client(url, doctor=doctor)
		print(client)
		result = client.service.getFundCodeNameDataSet()
		print(result)

	def weather():
		'天气查询'
		url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx?wsdl'	#天气查询
		imp = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
		imp.filter.add('http://WebXml.com.cn/')
		doctor = ImportDoctor(imp)	# 显示的制定调用标准
		# client = Client(url, plugins=[ImportDoctor(imp)])
		client = Client(url, doctor=doctor)
		print(client)
		result = client.service.getWeather('北京')
		print(result)
		# ======================可以直接用requests库请求======================
		url2 = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx'	#开放基金信息
		r = requests.get(url2+'/getWeather', params={'theCityCode':'上海', 'theUserID':''})
		print(r.text)

	def airline():
		'航班查询'
		url = 'http://ws.webxml.com.cn/webservices/DomesticAirline.asmx?wsdl'	#航班查询
		imp = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
		imp.filter.add('http://WebXml.com.cn/')
		doctor = ImportDoctor(imp)	# 显示的制定调用标准
		# client = Client(url, plugins=[ImportDoctor(imp)])
		client = Client(url, doctor=doctor)
		print(client)
		startCity = "上海"
		lastCity = "北京"
		theDate = datetime.date.today()
		result = client.service.getDomesticAirlinesTime(startCity, lastCity, theDate)
		print(result)	
	# return mobilecode(), funddata(), weather(), airline()
	return airline()

def yicai():
	'第一财经'
	url_yicai = 'https://www.yicai.com/news'
	url = 'https://www.yicai.com/api/ajax/getranklistbykeys'
	def topnews():
		'新闻排行榜'
		r = requests.get(url=url, params={'keys':'newsRank,videoRank,imageRank,liveRank'}, headers=headers)
		webcontent = r.json()
		# ======================新闻排行======================
		newsRank = webcontent['newsRank']
		print('-'*20,'新闻排行-周','-'*20)
		for new in newsRank['week']:
			title = new['NewsTitle']
			link = url_yicai+new['url']
			print(title, link)
		print('-'*20,'新闻排行-月','-'*20)
		for new in newsRank['month']:
			title = new['NewsTitle']
			link = url_yicai+new['url']
			print(title, link)

		# ======================视频排行======================
		videoRank = webcontent['videoRank']
		print('-'*20,'视频排行-周','-'*20)
		for new in videoRank['week']:
			title = new['NewsTitle']
			link = url_yicai+new['url']
			print(title, link)
		print('-'*20,'视频排行-月','-'*20)
		for new in videoRank['month']:
			title = new['NewsTitle']
			link = url_yicai+new['url']
			print(title, link)

		# ======================大直播排行======================
		liveRank = webcontent['videoRank']
		print('-'*20,'大直播排行-周','-'*20)
		for new in liveRank['week']:
			title = new['NewsTitle']
			link = url_yicai+new['url']
			print(title, link)
		print('-'*20,'大直播排行-月','-'*20)
		for new in liveRank['month']:
			title = new['NewsTitle']
			link = url_yicai+new['url']
			print(title, link)

		# ======================图集播排行======================
		imageRank = webcontent['videoRank']
		print('-'*20,'图集排行-周','-'*20)
		for new in imageRank['week']:
			title = new['NewsTitle']
			link = url_yicai+new['url']
			print(title, link)
		print('-'*20,'图集排行-月','-'*20)
		for new in imageRank['month']:
			title = new['NewsTitle']
			link = url_yicai+new['url']
			print(title, link)

	return topnews()

def caixin():
	'财新网'
	url = 'http://www.caixin.com/'
	r = requests.get(url=url, headers=headers)
	codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	r.encoding = codestyle	# 指定正确的编码格式
	# print(codestyle)
	webcontent = r.text
	soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
	# --------------排行榜--------------
	print('-'*20,'排行榜','-'*20)
	xinpi = soup.find('div', class_='top10Con')
	news = xinpi.find_all('dd')
	for new in news:
		title = new.text
		link = new.select('dd>a')[0].get('href')
		print(title, link)

	# --------------首页列表--------------
	print('-'*20,'首页列表','-'*20)
	xinpi = soup.find('div', class_='news_list')
	news = xinpi.find_all('dd')
	# print(news)
	for new in news:
		title = new.select('dd>p>a')[0].text
		link = new.select('dd>p>a')[0].get('href')
		print(title, link)

def odaily():
	'星球日报'

	def odaily_page():
		'从页面获取'
		url = 'https://www.odaily.com'
		r = requests.get(url=url, headers=headers)
		codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
		r.encoding = codestyle	# 指定正确的编码格式
		# print(codestyle)
		webcontent = r.text
		soup = BeautifulSoup(webcontent, "html.parser")	#转换成html格式
		# --------------文章热榜-日--------------
		print('-'*20,'文章热榜-日','-'*20)
		xinpi = soup.find('div', class_='_2xoas7mT')
		news = xinpi.find_all('div',class_='_2huHp6uR _2O131UXz _3bQIemFv')
		# print(news)
		for new in news:
			title = new.select('div>a>img')[0].get('alt')
			link = new.select('div>a')[0].get('href')
			link = url+link
			print(title, link)

	def odaily_interface():
		'从接口获取'
		url = 'https://www.odaily.com/service/founds/postList'
		# ======================文章热榜-日======================
		r = requests.get(url=url, params={'type':'day'}, headers=headers)
		# print(r.json())
		webcontent = r.json()['data']
		newsRank = webcontent['items']
		print('-'*20,'文章热榜-日','-'*20)
		for new in newsRank:
			title = new['title']
			new_id = new['id']
			link = 'https://www.odaily.com/post/'+str(new_id)
			print(title, link)

		# ======================文章热榜-周======================
		r = requests.get(url=url, params={'type':'week'}, headers=headers)
		# print(r.json())
		webcontent = r.json()['data']
		newsRank = webcontent['items']
		print('-'*20,'文章热榜-周','-'*20)
		for new in newsRank:
			title = new['title']
			new_id = new['id']
			link = 'https://www.odaily.com/post/'+str(new_id)
			print(title, link)

	return odaily_page(), odaily_interface()

if __name__ == '__main__':
	odaily()
