# -*- coding:utf-8 -*-
'''
获取二手房信息
'''
import sys
import os
import re
import csv
import urllib.request
from bs4 import BeautifulSoup

house_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'house.csv'))


# 成功打开页面是返回页面的对象，否则打印错误信息，退出程序
def get_baobj(url):
    page = urllib.request.urlopen(url)
    if page.getcode() == 200:
        html = page.read()
        bsobj = BeautifulSoup(html, "html.parser")
        return bsobj
    else:
        print('页面访问出错')
        sys.exit()

def get_house_info_list(url):
    print('获取二手房区域信息:',url)
    house_info_list = []
    bsobj = get_baobj(url)
    if not bsobj:
        return None

    #获取页数
    global house_info_page
    house_page = bsobj.find("div", {"class":"page-box house-lst-page-box"})
    house_page = house_page['page-data']
    print(house_page)
    house_info_page = int(eval(house_page)['totalPage'])
    house_list = bsobj.find_all("div", {"class":"info clear"})
    for house in house_list:    #从第二个元素开始截取house_list
        print(house)
        # 小区名称
        title = house.find("div", {"class":"title"}).get_text().split('/')
        # 获取信息数据 （例：加怡名城 | 2室1厅 | 62.48平米 | 西 | 精装），通过“|”符号分割字符串
        info = house.find("div", {"class":"houseInfo"}).get_text().split('|')
        print(info)
        info2 = house.find("div", {"class":"flood"}).get_text()
        # 价格
        minor = house.find("div", {"class":"priceInfo"})
        # 总价
        price = minor.find("div", {"class":"totalPrice"}).get_text()
        # 单价
        unitprice = minor.find("div", {"class":"unitPrice"}).get_text()
        # 楼层位置
        block= info2
        if len(info2)>1:
            niandai = info2
        else:
            niandai = '未知'
        # 房型
        house_type = info[1].strip()
        # 面积
        size = info[2].strip()

        house_info_list.append({'主题':title, '房型':house_type, '面积':size, '总格':price, '年代':niandai, '单价':unitprice})

    return house_info_list

# 读取前100个页面的房屋信息，将信息保存到house.csv 文件中
def house_mess(url):
    house_info_list = []
    get_house_info_list(url)
    if house_info_page>20:
        for i in range(0, 21):
            new_url = url + '/d' + str(i)
            house_info_list.extend(get_house_info_list(new_url))
            print(house_info_list)


    if house_info_list:
        with open(house_path, 'w' ,newline='') as f:
            writer = csv.writer(f)
            filenames = house_info_list[0].keys()
            writer.writerow(filenames)
            for house_info in house_info_list:
                writer.writerow(house_info.values())
