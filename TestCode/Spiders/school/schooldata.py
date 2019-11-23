'''
https://gkcx.eol.cn/special
根据专业查询所有学校（单页查询）
'''
import math
import pymysql
import requests

host = "172.16.101.223"
port = "3306"
user = "root"
password = "admin"
dbname = "testresult"

conn = pymysql.connect(host=host, db=dbname, user=user, passwd=password, use_unicode=True, charset="utf8")
cursor = conn.cursor()


url = 'https://api.eol.cn/gkcx/api/'
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
          }

datas = {
    "access_token": "",
    "keyword": "",
    "page": 1,
    "province_id": "",
    "request_type": 1,
    "school_type": "",
    "size": 1000000,
    "special_id": "1",
    "type": "",
    "uri": "apidata/api/gk/schoolSpecial/lists"
}

r = requests.post(url=url, params=datas, headers=headers)
items = r.json()['data']['item']
for item in items:
    print(item)
    print('校名：%s'%(item['name']))
    print('专业名称：%s'%(item['spname']))
    print('教育部直属%s'%(item['level1']))
    print('重点专业：%s'%(item['is_important']))
    print('f211%s'%(item['f211']))
    print('f985%s'%(item['f985']))
    print('='*20)