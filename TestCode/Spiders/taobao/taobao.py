# -*- coding:utf-8 -*-
'''
获取1688店铺商品的url
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time


def firstpage():
    '第一页URL的处理'
    url = 'https://shop1457628855363.1688.com/page/offerlist_97921283.htm?spm=a2615.7691456.newlist.6.6a8d64e6m4S4WL&showType=windows'

    html = urlopen(url)
    bsobj = BeautifulSoup(html, 'html.parser')  
    t1 = bsobj.find_all('a')
    print('获取第一页数据')
    for t2 in t1:
        t = str(t2.get('href'))
        if 'https://detail' in t:
            print('url==', t)
            print('****'*30)
            write2file(t)

def otherpage():
    '第二页及之后的URL处理(采用URL+页码拼接的方式)'
    url_new = 'https://shop1457628855363.1688.com/page/offerlist_97921283.htm?spm=a2615.7691456.newlist.234.4995e9d8Zkxh36&showType=windows&tradenumFilter=false&sampleFilter=false&sellerRecommendFilter=false&videoFilter=false&mixFilter=false&privateFilter=false&mobileOfferFilter=%24mobileOfferFilter&groupFilter=false&sortType=tradenumdown&pageNum='
    url_back = '#search-bar'

    for i in range(2,69):
        html = urlopen(url_new + str(i) + url_back)
        bsobj = BeautifulSoup(html, 'html.parser')  
        t1 = bsobj.find_all('a')
        print('获取第{}页数据'.format(i))
        i += 1
        for t2 in t1:
            t = str(t2.get('href'))
            if 'https://detail' in t:
                print('url==', t)
                print('****'*30)
                write2file(t)

def write2file(info):
    '写入文件'
    with open('url_info.txt','a+') as f:
        f.write(info)  # 将获取的数据写入到当前目录下的url_info.txt文件中
        f.write('\n')


if __name__ == '__main__':
    firstpage()
    otherpage()