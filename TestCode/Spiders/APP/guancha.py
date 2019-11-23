# coding=utf-8
'''
手机app 观察者
'''
import requests

header = {'User-Agent': 'Observer/5.2 (com.guanchazhe.GuanCha; build:2.0; iOS 12.0.1) Alamofire/4.7.3'}

def appdata():
    aurl = 'https://api.guancha.cn/Appdata/getDetailExtend?id=400967'
    r = requests.get(url=aurl, headers=header)
    arts = r.json()['datas']['most_news']
    print(arts)
    for art in arts:
        print('id=%s'%art['id'])
        print('title=%s'%art['title'])


def news():
    aurl2 = 'https://app.guancha.cn/news/list1.json?id=ChanJing&page=1&type=1'
    t = requests.get(url=aurl2, headers=header)
    print(t.json()['data']['toutiao'])

if __name__ == '__main__':
    appdata()
    news()

