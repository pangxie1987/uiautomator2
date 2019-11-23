# -*- coding:utf-8 -*-
'''
房产价格信息
https://blog.csdn.net/wenyusuran/article/details/80965578
'''
import os
import re
import requests
import pandas
from bs4 import BeautifulSoup

# 信息存储文件 house_price.xlsx 路径
filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), 'house_price.xlsx'))
print(filepath)

url = 'http://newhouse.cd.fang.com/house/s/b91/'
HTML = requests.get(url)
SOUP = BeautifulSoup(HTML.content, 'html.parser', from_encoding='gb18030')

last_page = SOUP.select('.last')
print(last_page)
page_number = int(last_page[0]['href'].split('/')[3].split('9')[1])
print(page_number)

names_list = []
addresses_list = []
all_type_list = []
all_money_list = []
url_demo = 'http://newhouse.cd.fang.com/house/s/b9{}/'
for i in range(1, page_number+1):
    url = url_demo.format(i)
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser', from_encoding='gb18030')
    names = soup.select('.nlcd_name a')
    addresses = soup.select('.address a')
    for name in names:
        names_list.append(name.text.strip())
    for address in addresses:
        address_detail = re.findall(r'".+"', str(re.findall(r'title=".+"', str(address))))[0]
        addresses_list.append(address_detail.split('"')[1])
        all_type = soup.findAll(name="span", attrs={"class":re.compile(r"forSale|inSale|outSale|zusale|zushou")})
    for type in all_type:
        all_type_list.append(type.text)

    if soup.select('.kanzx'):
        all_money_list.append('无')
        all_money = soup.findAll(name="div", attrs={"class":re.compile(r"nhouse_price|kanesf")})
        for money in all_money:
            all_money_list.append(money.text.strip())
    else:
        all_money = soup.findAll(name="div", attrs={"class":re.compile(r"nhouse_price|kanesf")})
        for money in all_money:
            all_money_list.append(money.text.strip())

all_message = []
for m in range(0, len(names_list)):
    message = [names_list[m], addresses_list[m], all_type_list[m], all_money_list[m]]
    print(message)
    all_message.append(message)
    df = pandas.DataFrame(all_message)
    df.to_excel(filepath)
    print(df)