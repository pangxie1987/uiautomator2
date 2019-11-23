# -*-coding:utf-8 -*-
'''
从Excel中读取数据，并插入数据库
'''
import os
import re
import sys
import base64
import datetime
import time
import datetime
fapath = os.path.dirname(os.path.dirname(__file__))
sys.path.append(fapath)
import pymysql
import os
from comm.readjson import read
import xlrd

# 读取json格式的配置文件并解析各个参数
# user = read('mysql_db.json')['mysqlconf']['user']
# passwd = read('mysql_db.json')['mysqlconf']['password']

report_path = os.path.join(os.path.dirname(__file__), '推送名单.xlsx')
 
class mysqlconnect(object):
    '数据库连接'
    def __init__(self):
        # self.conn = pymysql.connect(host='172.16.100.22', db='tebonxbiz_spider', user=user, passwd=passwd, use_unicode=True, charset="utf8")
        self.conn = pymysql.connect(host='172.16.100.22', db='tebonxbiz_spider', user='root', passwd='tebon2017', use_unicode=True, charset="utf8")
        self.cursor = self.conn.cursor()

    def execute(self, sql):
        '执行并返回单条数据'
        self.cursor.execute(sql)
        sqldata = self.cursor.fetchone()
        # print(sqldata)
        # 返回的是一个元组
        return sqldata

    def insert_data(self, sql):
        '修改数据'
        self.cursor.execute(sql)
        self.cursor.execute('commit')
        return

class ReadData(object):
    '读取Excel数据'
    def __init__(self):
        self.data = xlrd.open_workbook(report_path)
        self.table = self.data.sheet_by_name('Sheet1') #通过名称获取
    
    def rownum(self):
        '返回所有行数'
        self.nrows = self.table.nrows
        return self.nrows
    
    def onerow(self, rownum):
        '获取单行数据，列表形式'
        onedata = self.table.row_values(rownum)
        return onedata
        
if __name__ == '__main__':
    alldatas = ReadData()
    mydb = mysqlconnect()
    for i in range(2,alldatas.rownum()):
        userinfo = alldatas.onerow(i)
        print(userinfo)
        username = userinfo[1]
        usernober = userinfo[2]
        userding = userinfo[3]
        useremail = userinfo[4]
        sql = 'INSERT INTO spider_user_info (true_name,employee_id,dingding,phone_number,email,status)VALUES("%s","%s","%s","11112222333","%s",1)'%(username,usernober,userding,useremail)
        print(sql)
        mydb.insert_data(sql)        
