# -*- coding:utf-8 -*-

'''
pip install jira
jira库使用
https://developer.atlassian.com/cloud/jira/platform/rest/v2/#api-rest-api-2-jql-autocompletedata-get
'''
import os
import sys
from jira import JIRA
casepath = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) 
sys.path.append(casepath)
from unitls.email import send_email
# jac = JIRA(basic_auth=('liupb', 'liupb123456'), options={'server':'http://192.168.2.100:8000'})
# print(jac.user(jac.current_user()))
# print(jac.projects())

class ProjectInfo:
    '要查询的项目信息'
    name = '资管综合运营平台系统'
    types = '缺陷'
    status= ("暂缓","开始")

class ServerInfo:
    'Jira配置信息'
    username = 'liupb'
    passwd = 'liupb123456'
    server = 'http://192.168.2.100:8000'

def issue_serach():
    jira = JIRA(basic_auth=('liupb', 'liupb123456'), options={'server':'http://192.168.2.100:8000'})
    print(jira.user(jira.current_user()))
    done = jira.search_issues('project = "资管统一登录平台" AND issuetype = 缺陷 and status=暂缓 ',maxResults=100000)
    # testing = jira.search_issues('project = "证券行业资讯数据爬虫工具" AND issuetype = 故障 AND status = 测试中  ',maxResults=100000)
    # toDo = jira.search_issues('project = "证券行业资讯数据爬虫工具" AND issuetype = 故障 AND status = "To Do"  ',maxResults=100000)
    for issue in done:
        print('{0}: {1}'.format(issue.key, issue.fields.summary))

class Get_Bugs(object):
    '从jira中获取指定项目的bug'
    def __init__(self, username, password, serverinfo):
        #jira = JIRA(basic_auth=('liupb', 'liupb123456'), options={'server':'http://192.168.2.100:8000'})
        self.jira = JIRA(basic_auth=(username, password), options={'server':serverinfo})

    def get_datas(self, projectname, issuetype, issuestatus):
        '根据传入的projectname(项目名称),issuetype(问题类型),status(问题状态)，获取相关数据'
        '如果传入多个值，使用in ("AA","BB")的方式'
        zanhuan = self.jira.search_issues('project = %s AND issuetype = %s and status in %s '%(projectname,issuetype,issuestatus),maxResults=100000)
        descriptions = ''
        for issue in zanhuan:
            description = '{0}: {1}'.format(issue.key, issue.fields.summary)
            # print(description)
            # print("*"*20)
            descriptions = descriptions + description + '\n'+'-'*30+'\n'
            print(descriptions)
        return descriptions

if __name__ == '__main__':
    # issue_serach()
    getbug = Get_Bugs(ServerInfo.username, ServerInfo.passwd, ServerInfo.server)
    results = getbug.get_datas(ProjectInfo.name, ProjectInfo.types,ProjectInfo.status)
    print(results)
    send_email(ProjectInfo.name, results)