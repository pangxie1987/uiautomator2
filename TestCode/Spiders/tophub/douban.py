'''
豆瓣电影查询（按照名称）
https://www.jianshu.com/p/3df95dcbd92f
'''
from bs4 import BeautifulSoup
from selenium import webdriver
import requests

movie_name = '战狼2'

headers = {
		"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
		"Cookie":""}

driver = webdriver.Chrome()
driver.get('https://movie.douban.com/')
input_text = driver.find_element_by_name('search_text')
input_text.send_keys(movie_name)
search_button = driver.find_element_by_css_selector('#db-nav-movie > div.nav-wrap > div > div.nav-search > form > fieldset > div.inp-btn > input[type=submit]')
search_button.click()

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
	summary = soupmovie.find("span", property="v:summary").text.strip() 	# 剧情简介
	print(summary)
	print('='*50)


