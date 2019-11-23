'''
简单的邮件发送库yagmail
https://www.cnblogs.com/fnng/p/7967213.html
https://blog.csdn.net/weixin_30359021/article/details/96116790
pip install yagmail

'''

import yagmail as ya

yag = ya.SMTP(user='m18516292278@163.com', password='lpb201212', host='smtp.163.com')

fileobject = open('./report.html', encoding='utf-8').read()


contents = ['This is the body, and here is just text http://somedomain/image.png',
            'You can find an audio file attached.',fileobject]

yag.send('m18516292278@163.com', 'subject', contents)