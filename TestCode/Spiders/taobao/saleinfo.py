'''
淘宝店铺商品销量信息
https://blog.csdn.net/dxcve/article/details/81669521
https://www.jianshu.com/p/b5be61e757d7
'''
import requests
from bs4 import BeautifulSoup

def goods():
	'获取店铺所有商品'
	shop_url = 'https://detail.tmall.com/item.htm'
	headers = {
				"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
				}
	querystring = {"spm":"a1z10.3-b-s.w4011-15160618060.42.4cdc2172FKB3Cz","id":"596669888519","rn":"ea5da27fac34a04b6d5dddd447c2ed39","abbucket":"19","sku_properties":"5919063:6536025"}
	r = requests.get(url=shop_url, params=querystring, headers=headers)
	# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	# r.encoding = codestyle	# 指定正确的编码格式
	webcontent = r.text
	print((webcontent))
	soup = BeautifulSoup(webcontent, 'html.parser')
	#print(soup)
	index_list = soup.find("meta", name_="description")
	#print(index_list)
	# content = index_list.find_all("dd", class_='detail ')
	# print(content)
	#for news in content:
		#news = news.find('h2', href = True)
		#print(news)

def search_goods():
	'搜索商品'
	shop_url = 'https://list.tmall.com/search_product.htm'
	headers = {
				"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
				}
	querystring = {"q":"羽毛球鞋","type":"p","spm":"a220m.1000858.a2227oh.d100","from":".list.pc_1_searchbutton"}
	r = requests.get(url=shop_url, params=querystring, headers=headers)
	# codestyle = requests.utils.get_encodings_from_content(r.text)[0]	#获取网页的实际编码格式
	# r.encoding = codestyle	# 指定正确的编码格式
	webcontent = r.text
	# print((webcontent))
	soup = BeautifulSoup(webcontent, 'html.parser')
	#print(soup)
	index_list = soup.find("div", id="J_ItemList")
	# print(index_list)
	content = index_list.find_all("div", class_='product-iWrap')
	# print(content)
	for goods in content:
		price = goods.select('div>p')[1].text
		title = goods.select('div>p')[2].text
		link = goods.select('div>p')[2]
		link = link.select('p>a')[0].get('href')
		link = 'https'+link
		print(goods)
		print(title, price, link)
		print('*'*50)

if __name__ == '__main__':
	search_goods()