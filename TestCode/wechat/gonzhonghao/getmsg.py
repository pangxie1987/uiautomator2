'''
微信公众号信息
https://zhuanlan.zhihu.com/p/72558672?utm_source=wechat_session&utm_medium=social&utm_oi=563854400989364224
'''
import requests
import json
import time
from pymongo import MongoClient
import pymysql
import pdfkit
import os

url = 'https://mp.weixin.qq.com/mp/profile_ext'

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.1021.400 QQBrowser/9.0.2524.400"
}
tname = 'wxtest'

def mongoconn():
    # 保存到Mongo中
    conn = MongoClient('mongodb://localhost:27017/')
    db = conn.wx
    mongowx = db.article
    # mongowx.insert({
    #         'title':title,
    #         'content_url':content_url,
    #         'cover':cover,
    #         'datetime':datetime
    #     })

def createpdf(url, fileid):
    '将文章转成pdf,需要安装wkhtmltopdf.exe'
    
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    path = os.path.dirname(__file__)
    pdfname = os.path.join(path,str(fileid)+'.pdf')
    print(pdfname)
    print(url)
    pdfkit.from_url(url, pdfname, configuration=config)

class MysqlConn(object):
    'mysql数据库'
    def __init__(self):
        self.mysqlconn = pymysql.connect(host='172.16.101.223', db='tebonxbot',user='root', passwd='admin', charset='utf8')
        self.cursor = self.mysqlconn.cursor()

    def createdb(self, tablename):
        '创建新表'
        # dropsql = "DROP TABLE IF EXISTS %s"%tablename
        # self.cursor.execute(dropsql)
        # 创建数据表SQL语句
        sql = """
                DROP TABLE IF EXISTS %s
                CREATE TABLE `%s` (
                `fileid` int(11) DEFAULT NULL COMMENT '文章id',
                `digest` char(255) DEFAULT NULL COMMENT '发布者',
                `title` char(255) DEFAULT NULL COMMENT '文章标题',
                `content_url` char(255) DEFAULT NULL COMMENT '文章地址',
                `cover` char(255) DEFAULT NULL COMMENT '封面',
                `datetime` datetime DEFAULT NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
            """%(tablename,tablename)
        self.cursor.execute(sql)

    def execute(self,sql):
        '执行sql'
        try:
            self.cursor.execute(sql)
            self.mysqlconn.commit()
        except:
            self.mysqlconn.rollback()
        # self.mysqlconn.close()

def getdatas(index=0, count=10):
    '获取公众号数据-券商中国'
    '''
    __biz : 用户和公众号之间的唯一id，

    uin ：用户的私密id

    key ：请求的秘钥，一段时候只会就会失效。

    offset ：偏移量

    count ：每次请求的条数
    '''
    offset = (index+1)*count
    querystring = {
        "__biz":"MzA3NjM5MjIwOQ==",
        "uin":"MjU1MjExMjgxNw==",
        "key":"f6d26f92f2a2f56d94a0c40bd12d2a9bef24495b2fc03737c1b572bce1050a289068e3b2c11567744056d8bc4c1cb4201ddd03ba0f6c7f864c6ec60dc8f4e073160a52648721d199ca4bc22a5f1d1cfb",   #变动的，一段时间失效
        "offset":offset,
        "count":count,    #获取的条数
        "action":"getmsg",
        "f":"json"
    }
    r = requests.get(url=url, params=querystring, headers=header)
    resp = r.json()

    # mysqlconn = MysqlConn()
    # mysqlconn.createdb(tname)
    if resp['errmsg'] == 'ok':
        
        can_msg_continue = resp['can_msg_continue'] #是否有分页数据
        msg_count = resp['msg_count']   #当前分页文章数量
        resp = r.json()['general_msg_list']
        datas = json.loads(resp)
        listdata = datas['list']
        for contents in listdata:
            messages = contents['app_msg_ext_info']
            print(messages)
            # 文章id
            fileid = messages['fileid']
            # 发布者
            digest = messages['digest']
            # 文章标题
            title = messages['title']
            # 文章地址
            content_url = messages['content_url']
            # 文章封面
            cover = messages['cover']
            # 发布时间
            datetime = contents['comm_msg_info']['datetime']
            datetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(datetime))
            print(fileid,digest,title,content_url,cover,datetime)
            sql = "INSERT INTO %s VALUES (%s, '%s', '%s', '%s', '%s', '%s');"%(tname,fileid,digest,title,content_url,cover,datetime)
            print(sql)
            mysqlconn.execute(sql)
            createpdf(content_url, fileid)

        if can_msg_continue == 1:
            return True
        else:
            print('文章获取异常')
            return False
        print('Mongo写入完成')

if __name__ == '__main__':
    index = 0
    mysqlconn = MysqlConn()
    mysqlconn.createdb(tname)
    while 1:
        print('开始获取公众号第{}页文章'.format(index+1))
        flag = getdatas(index=index)
        time.sleep(5)
        index += 1
        if not flag:
            print('公众号文章已全部抓取完毕')
            break
    # getdatas()
