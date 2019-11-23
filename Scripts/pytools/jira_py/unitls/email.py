# -*- coding:utf-8 -*-
'''
邮件发送
'''

import sys
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # 混合MIME格式，支持上传附件
from email.header import Header  # 用于使用中文邮件主题
casepath = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) 
sys.path.append(casepath)

class email_conf():
    '邮件发送配置'
    fromname = '18516292278@163.com'
    toname = '773779347@qq.com'
    subject = '项目BUG数量统计'
    server = 'smtp.163.com'
    user = '18516292278'
    passwd = 'lpb201212'

def send_email(projectname, result):
    msg = MIMEMultipart()  # 混合MIME格式
    msg.attach(MIMEText(result, 'plain', 'utf-8'))
    # try:
    #     msg.attach(MIMEText(open(report_file, encoding='utf-8').read(), 'html', 'utf-8'))  # 添加html格式邮件正文（会丢失css格式）
    #     att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')  # 二进制格式打开
    #     att1["Content-Type"] = 'application/octet-stream'
    #     att1["Content-Disposition"] = 'attachment; filename="zgcollection_report.html"'  # filename为邮件中附件显示的名字
    #     msg.attach(att1)
    # except:
    #     print('找不到附件--%s'%report_file) 
    msg['From'] = email_conf.fromname  # 发件人
    msg['To'] = email_conf.toname  # 收件人
    msg['Subject'] = Header('【'+projectname+'】'+email_conf.subject, 'utf-8')  # 中文邮件主题，指定utf-8编
    # logfile = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'report','zgcollection.log')
    # att2 = MIMEText(open(logfile, 'rb').read(), 'base64', 'utf-8')
    # att2["Content-Type"] = 'application/octet-stream'
    # att2["Content-Disposition"] = 'attachment; filename="zgcollection.log"'
    # msg.attach(att2)
    try:
        smtp = smtplib.SMTP_SSL(email_conf.server)  # smtp服务器地址 使用SSL模式
        smtp.login(email_conf.user, email_conf.passwd)  # 用户名和授权码（注意不是登录密码）
        smtp.sendmail(msg['From'], msg["To"].split(","), msg.as_string())
        #smtp.sendmail("test_results@sina.com", "superhin@126.com", msg.as_string())  # 发送给另一个邮箱
        print("邮件发送完成！")
    except Exception as e:
        print(str(e))
    finally:
        smtp.quit()

if __name__ == '__main__':
    report_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'report','report.html')
    send_email('爬虫系统','FAIL')