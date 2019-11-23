# -*- coding:utf-8 -*-
'''
TestLink接口使用
pip install TestLink-API-Python-client
'''
import testlink
import os
import csv

class getTestcase(object):
    '获取csv测试用例，并写入本地csv文件'

    def __init__(self, proname, csv_file):
        '''
        proname:项目名称；
        csv_file:要写入的csv文件
        '''
        self.proname = proname
        self.csv_file = csv_file
        self.url = 'http://192.168.130.29:8088/testlink/lib/api/xmlrpc/v1/xmlrpc.php'
        self.key = 'a404fe7a2cf5b31b67ae9ce5597300fb'

    def testlink_connect(self):
        'testlink登录'
        self.myTestLink = testlink.TestlinkAPIClient(self.url, self.key)

    def gettescase(self):
        '获取testcase数据，并写入csvfile'
        self.case_list = ['','','','']
        self.testlink_connect()
        # count = self.myTestLink.countProjects() #所有项目数量
        # projects = self.myTestLink.getTestProjectByName(self.proname) #根据项目名称获取项目信息
        id = self.myTestLink.getProjectIDByName(self.proname)   #根据项目名称获取项目id
        topsuit = self.myTestLink.getFirstLevelTestSuitesForTestProject(id) #根据id获取项目最顶层的suit
        for suit in topsuit:
            # print('suit==========',suit)
            self.case_list[0] = suit['name']
            suitid = suit['id']
            testcases = self.myTestLink.getTestCasesForTestSuite(testsuiteid=suit['id'], details='full') #details='full'获取case所有信息
            for testcase in testcases:
                # print('testcase====',testcase)
                self.case_list[1] = testcase['name']
                for step in testcase['steps']:
                    actions = step['actions'].strip("\n").strip("<p>").strip("</p>")
                    expected_results = step['expected_results'].strip("\n").strip("<p>").strip("</p>")
                    self.case_list[2] = actions
                    self.case_list[3] = expected_results
                    print(self.case_list)
                    self.csv_write(self.case_list)

    def csv_open(self):
        '创建CSV写入模块'
        self.csvfile = open(self.csv_file, 'w', newline='')
        self.spamwriter = csv.writer(self.csvfile, dialect='excel')

    def csv_write(self, content):
        '写入list'
        self.spamwriter.writerow(content)

    def csv_close(self):
        '关闭csvfile'
        print('write done, close csv_file')
        self.csvfile.close()

    def gettestplan(self):
        '将测试结果回写到Testlink中'
        self.testlink_connect()
        # 根据项目名称和测试计划名称，获取测试计划信息
        testplan = self.myTestLink.getTestPlanByName('资讯推送平台', 'pushmsg')
        print(testplan)
        # 测试计划id
        testplanid = testplan[0]['id']
        # 根据测试计划信息获取测试案例id
        plancase = self.myTestLink.getTestCasesForTestPlan(testplanid)
        print(plancase)
        plancaseid = list(plancase)[0]
        print('plancaseid=====', plancaseid)
        # 将测试结果返回到Testlink中，结果为f 或者 p
        result = self.myTestLink.reportTCResult(testcaseid=plancaseid, testplanid=testplanid, buildname=None, status='p', noet="", guess=True)
        print('result====', result)

if __name__ == '__main__':
    
    csv_file = os.path.join(os.path.dirname(__file__), 'pushmsg.csv')
    mytest = getTestcase('资讯推送平台', csv_file)
    # content = ['suit', 'case', 'step', 'expect']
    # mytest.csv_open()
    # mytest.csv_write(content)
    # mytest.gettescase()
    # mytest.csv_close()
    mytest.gettestplan()
