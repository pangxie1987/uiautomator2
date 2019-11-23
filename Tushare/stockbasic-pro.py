# -*- coding:utf-8 -*-
'''
获取Tushare数据-新版
'''
import pymssql
import pandas
import tushare as ts
from sqlalchemy import create_engine

con = create_engine('mysql+pymysql://root:lpb1987@127.0.0.1:3306/tebonxspider?charset=utf8')
ts.set_token('4f37af208c3a4a38d3e89aeb7498d8f9e9f4b6ce46cb8acd0f7d402f')


def get_stock_basics():
    '股票列表'
    #list_status：：上市状态： L上市 D退市 P暂停上市
    pro = ts.pro_api()
    stockbasic = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    print(len(stockbasic))
    #stockbasic.to_sql('stock_basic', con, index=False )

if __name__ == '__main__':
    #get_stock_basics()
    df = ts.realtime_boxoffice()
    print(df)