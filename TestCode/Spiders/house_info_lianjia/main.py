# -*- coding:utf-8 -*-
'''
从链家获取二手房信息，并保存到本地csv
https://www.cnblogs.com/HZQHZA/p/7648452.html
'''
import csv
import sys
import urllib.request
from bs4 import BeautifulSoup
from house import house_mess
from house import house_path
from citys import citys_path

def get_city_dict():
    city_dict = {}
    with open(citys_path) as f:
        reader = csv.reader(f)
        for city in reader:
            if len(city) > 0:
                city_dict[city[0]] = city[1]
    return city_dict

city_dict = get_city_dict()


def get_district_dict(url):
    district_dict = {}
    html = urllib.request.urlopen(url).read()
    bsobj = BeautifulSoup(html, 'html.parser')
    roles = bsobj.find("div", {"data-role":"ershoufang"}).findChildren("a")
    for role in roles:
        # 对应区域的url
        district_url = role.get("href")
        # 对应区域的名称
        district_name = role.get_text()
        # 保存早字典中
        district_dict[district_name] = district_url

    return district_dict

def run():
    city_dict = get_city_dict()
    for city in city_dict.keys():
        print(city, end=' ')
    print()
    key_city = input("请输入城市：")
    # 根据用户输入的城市名， 得到城市的url
    city_url = city_dict.get(key_city)
    # 根据用户输入的城市名，得到城市的url
    if city_url:
        print(key_city, city_url)
    else:
        print("输入错误")
        sys.exit()

    ershoufang_city_url = city_url + "ershoufang"
    print(ershoufang_city_url)
    district_dict = get_district_dict(ershoufang_city_url)
    # 打印区域名
    for district in district_dict.keys():
        print(district, end=' ')
    print()

    input_distirct = input("请输入地区：")
    district_url = district_dict.get(input_distirct)

    # 输入错误，程序退出
    if not district_url:
        print("输入错误")
        sys.exit()

    # 如果输入正确
    house_info_url = city_url + district_url
    house_mess(house_info_url)

if __name__ == '__main__':
    run()


