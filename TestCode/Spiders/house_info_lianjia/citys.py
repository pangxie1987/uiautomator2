# -*- coding:utf-8 -*-
'''
获取城市数据
'''
import sys
import os
import csv
import urllib.request
from bs4 import BeautifulSoup

citys_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'citys.csv'))

url_city = 'https://bj.lianjia.com/city/'
url = "https://www.lianjia.com"

# 获取html
# 获取html页面
html = urllib.request.urlopen(url_city).read()

bsobj = BeautifulSoup(html, "html.parser")
city_tags = bsobj.find("div",{"class":"city_list_section"}).findChildren("a")
print(city_tags)

# 将每一条数据抽离，保存在citys.csv中
with open(citys_path, "w") as f:
    writ = csv.writer(f)
    for city_tag in city_tags:
        city_info = []
        # 获取<a> 标签的href连接
        city_url = city_tag.get("href")
        # 获取<a>标签的文字， 如：天津
        city_name = city_tag.get_text()
        city_info.append(city_name)
        city_info.append(city_url)
        writ.writerow(city_info)
        print(city_name, city_url)



