# -*- coding:utf-8 -*-
'''
获取Tushare数据-旧版
'''

#import pymssql
#import pandas
import tushare as ts
import threading
from datetime import datetime
from sqlalchemy import create_engine
from logger import logger

username = 'root'
password = 'admin'
# password = 'lpb1987'
host = '172.16.101.223:3306'
# host = '127.0.0.1:3306'
dbname = 'tebonxspider'
con = create_engine('mysql+pymysql://%s:%s@%s/%s'%(username,password,host,dbname))

def getstocks():
    '股票列表'
    # 出现数据插入失败，修改数据库stock_basic中'code'为varchar类型，并指定长度
    try:
        stockbasic = ts.get_stock_basics()
        logger.info(stockbasic)
        stockbasic.to_sql('stock_basic', con, index=True, if_exists='append')
    except Exception as e:
        logger.error(e)
        logger.error('stock_basic插入失败')

def reportdata(year, quarter):
    '业绩报告（主表）'
    # 出现数据插入失败，修改数据库resport_basic中'distrib'为text类型
    try:
        resports = ts.get_report_data(year=year,quarter=quarter)
        logger.info(resports)
        resports.to_sql('resport_basic', con, index=True, if_exists='append')
        logger.info('='*10+'获取第：%s年，第%s季度的数据完成'%(year, quarter)+'='*10)
    except Exception as e:
        logger.error(e)
        logger.error('resport_basic插入失败')
    

def profitdata(year, quarter):
    '盈利能力'
    try:
        profitsd = ts.get_profit_data(year=year,quarter=quarter)
        logger.info(profitsd)
        profitsd.to_sql('profit_basic', con, index=True, if_exists='append')
        logger.info('='*10+'获取第：%s年，第%s季度的数据完成'%(year, quarter)+'='*10)
    except Exception as e:
        logger.error(e)
        logger.error('profit_basic插入失败')

def operationdata(year, quarter):
    '营运能力'
    try:
        operationd = ts.get_operation_data(year=year,quarter=quarter)
        logger.info(operationd)
        operationd.to_sql('operation_basic', con, index=True, if_exists='append')
        logger.info('='*10+'获取第：%s年，第%s季度的数据完成'%(year, quarter)+'='*10)
    except Exception as e:
        logger.error(e)
        logger.error('operation_basic插入失败')

def growthdata(year, quarter):
    '成长能力'
    try:
        growth = ts.get_growth_data(year=year, quarter=quarter)
        logger.info(growth)
        growth.to_sql('growth_basic', con, index=True, if_exists='append')
        logger.info('='*10+'获取第：%s年，第%s季度的数据完成'%(year, quarter)+'='*10)
    except Exception as e:
        logger.error(e)
        logger.error('growth_basic插入失败')

def deptpaydata(year, quarter):
    '偿债能力'
    try:
        deptpay = ts.get_debtpaying_data(year=year,quarter=quarter)
        logger.info(deptpay)
        deptpay.to_sql('deptpay_basic', con, index=True, if_exists='append')
        logger.info('='*10+'获取第：%s年，第%s季度的数据完成'%(year, quarter)+'='*10)
    except Exception as e:
        logger.error(e)
        logger.error('deptpay_basic插入失败')

def cashflowdata(year, quarter):
    '现金流量'
    try:
        cashflow = ts.get_cashflow_data(year=year, quarter=quarter)
        logger.info(cashflow)
        cashflow.to_sql('cashflow_basic', con, index=True, if_exists='append')
        logger.info('='*10+'获取第：%s年，第%s季度的数据完成'%(year, quarter)+'='*10)
    except Exception as e:
        logger.error(e)
        logger.error('cashflow_basic插入失败')

if __name__ == '__main__':
    getstocks()
    reportdata()
    profitdata()
    operationdata()
    growthdata()
    deptpaydata()
    cashflowdata()