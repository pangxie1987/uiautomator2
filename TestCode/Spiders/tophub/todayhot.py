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

	return kuaixun(), hotnews() ,stock(), finance(), datastcn(), stocktop()
	# return stocktop()

if __name__ == '__main__':
	STCN()
