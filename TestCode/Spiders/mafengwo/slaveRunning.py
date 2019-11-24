#-*- coding:utf-8 -*-
import json
import requests
import re
from datetime import datetime, timedelta
import time
import smtplib
import logging
from email.mime.text import MIMEText
from email.utils import formataddr
#from dataConfig import option
import yaml
import logging.config
import os

myName='18516292278'

def setup_logging(default_path = "logging.yml",default_level = logging.INFO,env_key = "LOG_CFG"):
    yaml.warnings({'YAMLLoadWarning': False})
    path = default_path
    value = os.getenv(env_key,None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path,"r") as f:
            config = yaml.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level = default_level)


setup_logging(default_path = "logging.yml")


def getOutIp():
    try:
        text = requests.get('http://txt.go.sohu.com/ip/soip').text
        outIP = re.findall(r'\d+.\d+.\d+.\d+',text)
    except Exception as E:
        return (E)
    return (outIP)



def mail(msg_txt):
    my_sender = 'm18516292278@163.com'  # 发件人邮箱账号
    my_pass = 'lpb201212'  # 发件人邮箱密码
    my_user = ['m18516292278@163.com,', 'lpb.wal@outllok.com']  # 收件人邮箱账号，我这边发送给自己
    try:
        msg = MIMEText('\n'.join(msg_txt))
        msg['From'] = formataddr(["监控小助手", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = ','.join(my_user)  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "马蜂窝失效报警"  # 邮件的主题，也可以说是标题
        server = smtplib.SMTP_SSL("smtp.163.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, msg['To'].split(','), msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        logging.info('报警邮件发送成功')
        server.quit()  # 关闭连接
    except Exception as E:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        logging.info('报警邮件发送失败！！！！！！！！！！！！！！')
        return E
    return





fakeHeaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
}
baseHeader = {
    'Host': 'm.mafengwo.cn',
    'content-length': '73',
    'origin': 'https://m.mafengwo.cn',
    'content-type': 'application/x-www-form-urlencoded',
    'referer': 'https://m.mafengwo.cn/hotel/grab_coupon',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
}

def Update (a):
    try:
        r = requests.post('http://116.62.113.163:8080/zp/openMfwApi/saveOrUpdateGrabCouponInfo', data=a, headers = {'Content-Type': 'application/json'})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        rJson = r.json()
        print(rJson)
    except Exception as e:
        print(e)
        return e

def getdata (account):
    try:
        r = requests.get('http://116.62.113.163:8080/zp/openMfwApi/getMfwAccountInfo?accountId=%s' %(account))
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        rJson = r.json()
        return rJson
    except Exception as e:
        mail('数据拉取失败')
        logging.info(e)
        return e

def mydata_list(actID,cloudData):
    try :
        mydataList = []
        map_data = {
            '80':'d612f8301fbf5643e6fcfbabddda93d7',
            '100':'d45c8dc781ddf7bfceaa391dfb927f9e',
            '50':'8f91915938b59f18f48830bec8b8d824'
        }
        for i in cloudData['data']['priorityLevel'].split(','):
            ditc_a = {}
            ditc_a['coupon_sn'] = map_data[i]
            ditc_a['activity_id'] = actID
            mydataList.append(ditc_a)
        return mydataList
    except Exception as e:
        logging.info(e)
        return



def getTodayAct():
    act_id_dic = {}
    try:
        r = requests.get('https://m.mafengwo.cn/hajax/activity/coupon/activities_list',headers=fakeHeaders,timeout=5)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        rJson = r.json()
        act1 = rJson['data']['activity_list'][0]['activity_id']
        act1time = rJson['data']['activity_list'][0]['start_time']
        act1Status = rJson['data']['activity_list'][0]['activity_status']
        act2=rJson['data']['activity_list'][1]['activity_id']
        act2time=rJson['data']['activity_list'][1]['start_time']
        act2Status = rJson['data']['activity_list'][1]['activity_status']
        act3=rJson['data']['activity_list'][2]['activity_id']
        act3time=rJson['data']['activity_list'][2]['start_time']
        act3Status = rJson['data']['activity_list'][2]['activity_status']
        #act_id_list=[act1,act1time,act2,act2time,act3,act3time]
        act_id_dic[str(act1time.split(' ')[1].split(':')[0])+'|'+str(act1Status)] = act1
        act_id_dic[str(act2time.split(' ')[1].split(':')[0])+'|'+str(act2Status)] = act2
        act_id_dic[str(act3time.split(' ')[1].split(':')[0])+'|'+str(act3Status)] = act3
        #logging.info(act_id_dic)
        return act_id_dic
    except Exception as e:
        logging.info (e)
        return e



def getHtmlText(url,mydataList):
    try:
        o = myName
        successMsg = {}
        msg_txt = ['以下账号已过期，请尽快处理：']
        IP = ''.join(getOutIp())
        msg_txt2 = [IP,'这个网段今天废了应该是抢到过了，上面搭载了以下账号：']
        successMsg['accountId'] = myName
        successMsg['updateby'] = myName
        successMsg['updatetime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #mydataList = mydata_list(actID)
        mydataList = mydata_list(actID, cloudData)
        i = baseHeader
        #for i,o in zip(myHeaderDic.values(),myHeaderDic.keys()):
        for a in mydataList:
            logging.info('开始发送请求:'+ str(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')))
            r = requests.post(url, headers = i, data=a, timeout=5)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            #print(type(r.json()))
            logging.info(str(r.json())+'响应耗时：'+ str(r.elapsed.total_seconds()) +str(a))
            error_num = r.json()['code']
            if error_num == 104:
                msg_txt.append(o)
            elif error_num == 113:
                msg_txt2.append(o)
            elif error_num == 101:
                if r.json()['data']['discount_value'] == 100:
                    successMsg['hundredNextTime'] = r.json()['data']['usable_end_time']
                elif r.json()['data']['discount_value'] == 80:
                    successMsg['eightyNextTime'] = r.json()['data']['usable_end_time']
                elif r.json()['data']['discount_value'] == 50:
                    successMsg['fiftyNextTime'] = r.json()['data']['usable_end_time']
                #a = json.dumps(successMsg)
                #Update(a)
                #logging.info('已成功反写会数据库'+a)
        if len(msg_txt) > 1 and (datetime.now().strftime('%H') in ('09','13','17','19')):
            print(msg_txt)
            mail(list(set(msg_txt)))
        if len(msg_txt2) > 2 and (datetime.now().strftime('%H') in ('09', '13', '17')):
            print(msg_txt2)
            mail(list(set(msg_txt2)))
        a = json.dumps(successMsg)
        Update(a)
        logging.info('已成功反写会数据库' + a)
        logging.info(o+'搞定')
    except Exception as e:
        logging.info(e)
        return e

#把datetime转成字符串
def datetime_toString(dt):
    return dt.strftime("%H:%M:%S")

#把字符串转成datetime
def string_toDatetime(string):
    return datetime.strptime(string, "%H:%M:%S")

# 加一分钟或5分钟
def datetime_add(dt_string,minutes):
    delta = timedelta(minutes=minutes)
    n_days = string_toDatetime(dt_string) + delta
    return n_days.strftime("%H:%M:%S")




time1 = datetime.now().strftime('%H:%M:%S')
#time1 = '19:59:59'
act_id_dic = getTodayAct()
cloudData = getdata(myName)
# baseHeader['Cookie'] = option.Cookie
# baseHeader['user-agent'] = option.user_agent
actID = '288951379046302071'
mydataList = mydata_list(actID,cloudData)
logging.info(time1+'卍卍卍卍卍<欧~妈咪妈咪哄>卍卍卍卍卍\n'+str(act_id_dic))
#logging.info(getHtmlText('https://m.mafengwo.cn/hajax/activity/coupon/grab_coupon'),datetime.datetime.now().strftime('%H:%M:%S.%f'))
while 1:
    baseHeader['Cookie'] = cloudData['data']['cookie']
    baseHeader['user-agent'] = cloudData['data']['userAgent']
    startSecond = str(cloudData['data']['startSecond'])
    delaySecond = cloudData['data']['delaySecond']
    #控制最后一秒的抢券动作sleep是关键
    if '10:00:03' >= time1 >= '09:59:55' or '14:00:03' >= time1 >= '13:59:55' or '20:00:03' >= time1 >= '19:59:55':
        #logging.info('666666666')
        #if (str(int(time1.split(':')[0])+1)+'|1' in act_id_dic.keys()) or (str(int(time1.split(':')[0]))+'|1' in act_id_dic.keys()):#用活动返回标志来抢
        if time1[-5:] == '59:'+str(startSecond):#靠时间差来抢
            time.sleep(delaySecond)
            logging.info(str(getHtmlText('https://m.mafengwo.cn/hajax/activity/coupon/grab_coupon',mydataList))+datetime.now().strftime('%H:%M:%S.%f\n\n'))
            logging.info('=====================<%s点场%s，已完成秒杀>======================'%(str(int(time1[:2])+1),actID))
            logging.info('当前参数设置为，账号%s\t开始时间为%s秒\t延时%s秒'%(myName,startSecond,delaySecond))
            #time1 = datetime.now().strftime('%H:%M:%S')
        act_id_dic = getTodayAct()
        #act_id_dic = {'14|1': '288959400648278174', '20|1': '288959872499515403', '10|0': '288961524009238715'}
        #logging.info(act_id_dic,time1)
    elif time1== '07:00:00':
        cloudData = getdata(myName)
        logging.info('每天早上七点，开始拉取服务器数据，组装请求')
    #logging.info(time1)
    #闲暇时间随便请求一下，防止cookie过期
    elif datetime_add(time1,13) <= '09:50:00' or '10:15:01' <= datetime_add(time1,13) <= '13:50:00' or  '14:15:01' <= datetime_add(time1,13) <= '19:50:00' or '20:15:00' <= datetime_add(time1,13) <= '23:59:59':
        #print(baseHeader, startSecond, delaySecond)
        time.sleep(60*10)
        if time1.split(':')[0] in ('9','13','19'):
            cloudData = getdata(myName)
        #time1 = datetime.now().strftime('%H:%M:%S')
    #最后10分钟的等待时间，把actID换成要执行的
    else:
        if time1.split(':')[0] not in ('10','14','20'):
            #logging.info('最后10分钟的等待时间，把actID换成要执行的')
            actID = act_id_dic[str(int(time1.split(':')[0])+1)+'|0']
            #time1 = datetime.now().strftime('%H:%M:%S')
            #logging.info('已将actID重置为：',actID)
    time1 = datetime.now().strftime('%H:%M:%S')

if __name__ == '__main__':
    mail(1)