# -*- coding:utf-8 -*-

'''
雪球
api   https://xueqiu.com/v4/statuses/user_timeline.json?page=#{page}&user_id=#{user_id}
user_id 为文章用户的id
'''
import os
import sys
import requests
from lxml import etree
# casepath = os.path.abspath(os.path.dirname(__file__))
# sys.path.append(casepath)
from comm.config import email_conf
from comm.email import send_email
from eastmoney import get_allfund

myheaders = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
                }
path = os.path.dirname(__file__)
file = os.path.join(path, "xueqiu.txt")

def get_xueqiu():
    '雪球'
    user_id = '1184824257'  #券商中国
    url = 'https://xueqiu.com'
    url2 = 'https://xueqiu.com/v4/statuses/user_timeline.json'
    
    # 获取首页的cookie
    t = requests.get(url=url, headers=myheaders)
    cookie = t.cookies.get_dict()
    print(cookie)
    # print(t.text)
    tid = 0
    # 请求数据
    t = requests.get(url=url2, params={'page':1,'user_id':user_id}, headers=myheaders, cookies=cookie)

    with open(file,'w+') as f:
        f.write('*'*20+'雪球-券商中国'+'*'*20+'\n\n')
        for content in t.json()['statuses']:
            tid = int(tid)+1
            title = content['title']
            imgurl = url+content['target']
            print(tid,title,imgurl)
            # content_list = (tid,title,imgurl)
            f.write(str(tid))
            f.write(' '+title+imgurl+'\n\n')

def get_stcn_news():
    '证券时报-要闻'
    url = "http://news.stcn.com/"
    tid = 0
    # 请求数据
    t = requests.get(url=url, headers=myheaders)
    content = etree.HTML(t.text)
    movies = content.xpath('//*[@id="idData"]/li')
    with open(file,'a+') as f:
        f.write('*'*20+'证券时报-要闻'+'*'*20+'\n\n')
        for ss in movies:
            tid = int(tid)+1
            title = ss.xpath('p[1]/a/text()')[0]
            href = ss.xpath('p[1]/a/@href')[0]
            print(title)
            print(href)
            f.write(str(tid))
            f.write(' '+title+'\t'+href+'\t'+'\n\n')

def get_stcn_guonei():
    '证券时报-国内'
    url = "http://news.stcn.com/guonei/"
    tid = 0
    # 请求数据
    t = requests.get(url=url, headers=myheaders)
    content = etree.HTML(t.text)
    movies = content.xpath('/html/body/div[3]/div[1]/ul')
    for gg in movies:
        ll = gg.xpath('li[1]/p[1]/a')[0]
        print(ll.text)
        print(ll.attrib['href'])
    
if __name__ == '__main__':
    # get_xueqiu()
    # get_douban_now()
    # get_douban_later()
    # get_stcn_news()
    # send_email(file)
    get_stcn_guonei()
    get_allfund()
    