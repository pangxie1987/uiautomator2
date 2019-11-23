# -*- coding:utf-8 -*-

'''
获取淘宝店铺商品信息
'''

#import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time


# 第一页URL的处理
url = 'https://shop1457628855363.1688.com/page/offerlist_97921283.htm?spm=a2615.7691456.newlist.6.6a8d64e6m4S4WL&showType=windows'

html = urlopen(url)
bsobj = BeautifulSoup(html, 'html.parser')  
t1 = bsobj.find_all('a')

for t2 in t1:
    t = str(t2.get('href'))
    #print('t====',t)

    if 'https://detail' in t:
        with open('url_info.txt','a+') as f:
            f.write(t)
            f.write('\n')
            #print(t)
            #time.sleep(0.1)

# 第二页及之后的URL处理(采用URL+页码拼接的方式)
url_new = 'https://shop1457628855363.1688.com/page/offerlist_97921283.htm?spm=a2615.7691456.newlist.234.4995e9d8Zkxh36&showType=windows&tradenumFilter=false&sampleFilter=false&sellerRecommendFilter=false&videoFilter=false&mixFilter=false&privateFilter=false&mobileOfferFilter=%24mobileOfferFilter&groupFilter=false&sortType=tradenumdown&pageNum='
url_back = '#search-bar'


for i in range(2,69):
    html = urlopen(url_new + str(i) + url_back)
    bsobj = BeautifulSoup(html, 'html.parser')  
    t1 = bsobj.find_all('a')
    i += 1
    print('i==',i)
    

    for t2 in t1:
        t = str(t2.get('href'))

        if 'https://detail' in t:
            with open('url_info.txt','a+') as f:
                f.write(t)  # 将获取的数据写入到当前目录下的url_info.txt文件中
                f.write('\n')
                #print(t)
    # time.sleep(0.1)
