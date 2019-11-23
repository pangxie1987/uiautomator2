# coding=utf-8
'''
天天基金网-基金数据
http://fund.eastmoney.com
'''

import os
import sys
import requests
import json
from lxml import etree
# casepath = os.path.abspath(os.path.dirname(__file__))
# sys.path.append(casepath)
from comm.config import email_conf
from comm.email import send_email

myheaders = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
                }
path = os.path.dirname(__file__)
datafile = os.path.join(path, "xueqiu.txt")

def get_favor():
    '通过页面数据分析'
    url_home = 'http://fund.eastmoney.com/'
    url = 'http://fund.eastmoney.com/fund.html#os_0;isall_0;ft_;pt_1'   #分页连接
    url_all = 'http://fund.eastmoney.com/fund.html#os_0;isall_1;ft_|;pt_1'  #全部数据
    t = requests.get(url=url, headers=myheaders)
    print(t.encoding)
    t.encoding='gbk'
    print(t.text)
    content = etree.HTML(t.text)
    fundid = content.xpath('//*[@id="tr184801"]/td[4]')
    fundid = fundid[0].text
    fundlink = url_home+fundid+'.html'
    print(fundid)
    print(fundlink)
    fundname = content.xpath('//*[@id="tr184801"]/td[5]/nobr/a[1]')
    print(fundname[0].text)
    fund_dwjz = content.xpath('//*[@id="tr184801"]/td[6]')
    fund_dwjz = fund_dwjz[0].text   # 单位净值（当日）
    print(fund_dwjz)
    fund_ljjz = content.xpath('//*[@id="tr184801"]/td[6]')
    fund_ljjz = fund_ljjz[0].text   # 累计净值（当日）
    print(fund_ljjz)
    num = content.xpath('//*[@id="pager"]/span[9]')
    num = num[0].text   #获取页码数
    print(num)

def get_allfund():
    '通过接口返回所以数据'
    url = 'https://fundapi.eastmoney.com/fundtradenew.aspx?ft=pg&sc=1n&st=desc&pi=1&pn=100&cp=&ct=&cd=&ms=&fr=&plevel=&fst=&ftype=&fr1=&fl=0&isab='
    # pn=100 代表获取的数据数，100表示100条
    r = requests.get(url=url, headers=myheaders, verify=False)
    # content = (r.text).split('=')[1]
    # content = content.split(':')[1]
    # print(content)
    # content = content.split(",")    #将str转换成list
    # print(len(content))
    # fundsItems = []
    # fundsItem = {
    #     "code":'',
    #     "name":''
    # }
    # for fundinfo in content:
    #     print('='*10)
    #     print(fundinfo)
    #     fundinfo = str(fundinfo).split('|')
    #     print(fundinfo[0])
    #     fundsItems['code'] = fundinfo[0]
    #     fundsItems['name'] = fundinfo[1]
    #     print(fundsItem)
    #     fundsItems.append(fundsItem)

    # print(fundsItems)

    r.encoding = 'utf-8'
    datas = r.text

    # 取出json部分
    datas = datas[datas.find('{'):datas.find('}')+1] # 从出现第一个{开始，取到}

    # 给json各字段名添加双引号
    datas = datas.replace('datas', '\"datas\"')
    datas = datas.replace('allRecords', '\"allRecords\"')
    datas = datas.replace('pageIndex', '\"pageIndex\"')
    datas = datas.replace('pageNum', '\"pageNum\"')
    datas = datas.replace('allPages', '\"allPages\"')

    jsonBody = json.loads(datas)
    jsonDatas = jsonBody['datas']
    print(jsonDatas)

    fundsItem = {
        "code":'',
        "name":'',
        'day':'',
        'unitNetWorth':'',    #单位净值
        'dayOfGrowth':'',     #日增长率
        'recent1Week' :'',    # 最近一周
        'recent1Month' :'',   # 最近一月
        'recent3Month' :'',   # 最近三月
        'recent6Month' :'',   # 最近六月
        'recent1Year' :'',    # 最近一年
        'recent2Year' :'',    # 最近二年
        'recent3Year' :'',    # 最近三年
        'fromThisYear' :'',   # 今年以来
        'fromBuild' :'',      # 成立以来
        'serviceCharge' :'',  # 手续费
        'upEnoughAmount' :'', # 起够金额
        }
    
    with open(datafile, 'a+') as f:
        for fundinfo in jsonDatas:
            fundsItems = []
            fundinfo = fundinfo.split('|')
            fundsItem['code'] = fundinfo[0]
            fundsItem['name'] = fundinfo[1]
            fundsItem['day'] = fundinfo[3]
            fundsItem['unitNetWorth'] = fundinfo[4]
            fundsItem['dayOfGrowth'] = fundinfo[5]
            fundsItem['recent1Week'] = fundinfo[6]
            fundsItem['recent1Month'] = fundinfo[7]
            print(fundsItem)
            fundsItems.append(fundsItem)
            f.write(str(fundsItem))
            f.write('\n')
            f.writelines('*'*20+'\n')
            print('*'*10)
        #print(fundsItems)

if __name__ == '__main__':
    get_allfund()