'''
豆瓣电影查询（按照名称）
https://www.jianshu.com/p/3df95dcbd92f
'''
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from lxml import etree

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
		

def get_douban_now():
    '豆瓣-正在上映'
    url = "https://movie.douban.com/"
    url2 = "https://movie.douban.com/cinema/nowplaying/shanghai/"
    t = requests.get(url=url, headers=myheaders)
    cookie = t.cookies.get_dict()
    # print(cookie)
    # print(t.text)
    tid = 0
    # 请求数据
    t = requests.get(url=url2, headers=myheaders, cookies=cookie)
    #print(t.text)
    content = etree.HTML(t.text)
    print(content)
    movies = content.xpath('//div[@id="nowplaying"]/div/ul[@class="lists"]/li')
    with open(file,'a+') as f:
        f.write('*'*20+'正在上映'+'*'*20+'\n\n')
        for ss in movies:
            tid = int(tid)+1
            data = ss.attrib
            name = data['data-title']   #电影名
            score = data['data-score']  #IMDB评分
            actors = data['data-actors']    #主演
            print(name)
            f.write(str(tid))
            f.write(' '+name+'\t'+score+'\t'+actors+'\n\n')

def get_douban_later():
    '豆瓣-即将上映'
    url = "https://movie.douban.com/"
    url2 = "https://movie.douban.com/cinema/nowplaying/shanghai/"
    t = requests.get(url=url, headers=myheaders)
    cookie = t.cookies.get_dict()
    tid = 0
    # 请求数据
    t = requests.get(url=url2, headers=myheaders, cookies=cookie)
    content = etree.HTML(t.text)
    movies = content.xpath('//div[@id="upcoming"]/div/ul[@class="lists"]/li')
    with open(file,'a+') as f:
        f.write('*'*20+'即将上映'+'*'*20+'\n\n')
        for ss in movies:
            tid = int(tid)+1
            data = ss.attrib
            name = data['data-title']   #电影名
            region = data['data-region']  #产地
            director = data['data-director'] #导演
            actors = data['data-actors']    #主演
            print(name)
            f.write(str(tid))
            f.write(' '+name+'\t'+region+'\t'+director+'\t'+actors+'\n\n')



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