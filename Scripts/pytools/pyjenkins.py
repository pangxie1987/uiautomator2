'''
pip install python-jenkins
python调用Jenkins接口
https://www.cnblogs.com/znicy/p/5498609.html
https://www.jianshu.com/p/8fda9e96addd
'''

import jenkins

username='admin'
passwd = 'lpb1987'
token = '11c38f1f6c47e700c38c32663e8d4c250b'
server_url = 'http://127.0.0.1:8085'

server = jenkins.Jenkins(server_url, username=username, password=token)

# jobnames = server.get_all_jobs()

# for job in jobnames:
#     #print(server.get_build_test_report(job['name'], 10))
#     print(job['name'])

server.build_job('每日资讯')