'''
豆瓣电影查询（按照名称）
https://www.jianshu.com/p/3df95dcbd92f
'''
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

# movie_name = input('要查询的电影名：')
movie_name = '剪刀手爱德华'
print(movie_name)

headers = {
		"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
		"Cookie":""}

driver = webdriver.Chrome()
driver.get('https://movie.douban.com/')

def search():
	'搜索电影'
	input_text = driver.find_element_by_name('search_text')
	input_text.send_keys(movie_name)
	search_button = driver.find_element_by_css_selector('#db-nav-movie > div.nav-wrap > div > div.nav-search > form > fieldset > div.inp-btn > input[type=submit]')
	search_button.click()
	time.sleep(3)
	getmovie()

def nextpage():
	'点击下一页'
	try:
		next_page = driver.find_element_by_css_selector('a.next')
		next_page.click()
		now_page = driver.find_element_by_css_selector('a.num.activate.thispage').text
		time.sleep(3)
		print('--------------------当前页{}已加载完成--------------------'.format(now_page))
		getmovie()
		nextpage()
	except:
		print('没有下一页')

def getmovie():
	'解析电影'
	page = driver.page_source
	soup = BeautifulSoup(page, "html.parser")
	# print(soup)
	contents = soup.find_all("div", class_="item-root")

	for movies in contents:
		title = movies.select('div>div>div')[0].text
		link = movies.select('div>div>div')[0].select('div>a')[0].get('href')
		print(title, link)
		r = requests.get(url=link, headers=headers)
		soupmovie = BeautifulSoup(r.text, "html.parser")
		try:
			summary = soupmovie.find("span", property="v:summary").text.strip() 	# 剧情简介
		except:
			# print('影片简介为空')
			summary = '影片简介为空'
		print(summary)
		print('='*50)


def main():
	'入口函数'
	
	try:
		search()
		nextpage()
		getmovie()
	except Exception as e:
		raise e
	finally:
		driver.close()

if __name__ == '__main__':
	main()