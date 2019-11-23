# -*- coding-utf-8 -*-
'''
国家企业信用信息公开系统
http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html
https://blog.csdn.net/fenglei0415/article/details/81865379
'''
import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from lxml import etree
import requests
import re
import time
import json
import pymysql
# import redis

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,und;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
} 

url = "http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html"
data_url = "http://www.gsxt.gov.cn/affiche-query-area-info-paperall.html?noticeType=11&areaid=100000&noticeTitle=&regOrg="
# set phantomJS's agent to Firefox
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = \
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
 
# 根据实际的path改写，我的是mac，路径为"/usr/local/bin/PhantomJS"
path = os.path.dirname(__file__)
phantomjsPath = os.path.join(path, "phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
driver = webdriver.PhantomJS(executable_path=phantomjsPath, desired_capabilities=dcap)
 
class mysqlconf():
        host="172.16.100.23"
        port="3306"
        user="root"
        password="admin"
        dbname="credit_information"

connect = pymysql.connect(host=mysqlconf.host, db=mysqlconf.dbname, user=mysqlconf.user, passwd=mysqlconf.password, use_unicode=True, charset="utf8")
cursor = connect.cursor()
print('数据库连接成功！')
 
def get_cookies(url):
    '构造cookie'
    cookie_list = {}
    driver.get(url)
    time.sleep(2)
    cookies = driver.get_cookies()
    for co in cookies:
        if co in cookies:
            if co['name'] == '__jsl_clearance' or co['name'] == '__jsluid':
                cookie_list[co['name']] = co['value']
    driver.quit()
    cookies = requests.utils.add_dict_to_cookiejar(cj=None, cookie_dict=cookie_list)
    return cookies
 
def make_session(url):
    '构造请求对象'
    global headers
    cookies = get_cookies(url)
    s = requests.Session()
    s.cookies = cookies
    s.headers = headers
    return s

def insert_sql(mylist):
    '数据入库'
    sql = "insert into credit_data (dataform,entname,judauth,judauth_cn,juddate,lastmodifiedtime,noticecontent,noticedate,noticeid,noticeno,noticetitle,noticetype,simplecancelurl) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, mylist)
    connect.commit()

def get_content(ids):
    '根据各省的id获取各省的数据'
    for province_id in ids:
        print(province_id)
        pr_url = data_url+str(province_id)

        for i in range(1,6):
            playload = {"draw":i, "strat":(i-1)*10, "length":10}    #获取1-5页的数据,每页10条
            r = s.post(url=pr_url, data=playload)
            if '有疑似非正常访问行为' in r.text:
                print('访问过频，稍后重试')
                break
            else:
                # print(r.json()['data'])
                pr_datas = r.json()['data']
                # print(pr_datas)
                for provice in pr_datas:
                    print('*'*20)
                    print(provice['noticeTitle'])
                    datas_list = (provice['datafrom'],provice['entName'],provice['judAuth'],provice['judAuth_CN'],provice['judDate'],provice['lastModifiedTime'],provice['noticeContent'],provice['noticeDate'],provice['noticeId'],provice['noticeNO'],provice['noticeTitle'],provice['noticeType'],provice['simpleCancelUrl'])
                    print(datas_list)
                    insert_sql(datas_list)

if __name__ == '__main__':
    
    s = make_session(url)
    r = s.get(url, verify=False)    
    con = r.text.replace('\n', '').replace('\t', '').replace('\r', '')
    content = etree.HTML(con)
    id_list = content.xpath('//div[@class="label-list"]/div/@id')   #获取各省的id
    print(id_list)
    get_content(id_list)
    connect.close()
