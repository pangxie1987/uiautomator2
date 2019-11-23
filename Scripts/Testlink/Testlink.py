# -*- coding=utf-8 -*-
'''
将从TestLink导出的xml文件读取到csv文件
'''
import sys
import os
from imp import reload  
reload(sys)   
import csv
from time import sleep
from xml.etree.ElementTree import iterparse
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
class XML_CSV():
    #去掉xml文件中的HTML标签
    def strip_tags(self,htmlStr):
        htmlStr = htmlStr.strip()
        htmlStr = htmlStr.strip("\n")
        result = []
        parser = HTMLParser()
        parser.handle_data = result.append
        parser.feed(htmlStr)
        parser.close()
        return  ''.join(result)
      
    def read_xml_to_csv(self, csv_file, xmlfile):
        csv_file = os.path.join(os.path.dirname(__file__), csv_file)
        xmlfile = os.path.join(os.path.dirname(__file__), xmlfile)
        csvfile = open(csv_file, 'w', newline='')
        spamwriter = csv.writer(csvfile, dialect='excel')
        spamwriter.writerow(['suit', 'name', 'node_order', 'details', 'internalid','externalid','summary','preconditions','steps','expectedresults','caseno'])
        #逐行解析XML文件，将每行的内容存入列表，之后逐行写入CSV文件中
        i = 0
        for (event,node) in iterparse(xmlfile,events=['start']):
            # print('Node====', node.tag)
            if node.tag == "testsuite":
                suite_list = ['','','','','','','','','','']
                print( node.attrib['name'])
                suite_list[0] = node.attrib['name']
                for child in node:
                    if child.tag == "node_order":
                        print( child.text)
                        suite_list[2] = child.text
                    if child.tag == "details":
                        print( child.text)
                        suit3 = self.strip_tags(str(child.text))
                        suit3 = ''.join(suit3.split())  #去掉所有换行符、制表符、空格。
                        suite_list[3] = suit3
                spamwriter.writerow(suite_list)
            if node.tag == "testcase":
                case_list = ['testcase','','','','','','','','','','']
                print( node.attrib['internalid'])
                print( node.attrib['name'])
                case_list[1] = node.attrib['name']
                case_list[4] = node.attrib['internalid']
                for child in node:
                    if child.tag == "node_order":
                        print( child.text)
                        case_list[2] = child.text
                    if child.tag == "externalid":
                        print( child.text)
                        case_list[5] = child.text
                    if child.tag == "summary":
                        print( self.strip_tags(str(child.text)))
                        case_list[6] = self.strip_tags(str(child.text))
                    if child.tag == "preconditions":
                        print(self.strip_tags(str(child.text)))
                        list7 = self.strip_tags(str(child.text))
                        list7 = ''.join(list7.split()) #去掉所有换行符、制表符、空格。
                        case_list[7] = list7
                    if child.tag == "steps":
                        for step in child:
                            if step.tag == 'step':
                                for action in step:
                                                                       
                                    if action.tag == 'actions':
                                        i += 1
                                        case_list[10] = i
                                        print('*****i*****',i)
                                        print('case_list[7]', self.strip_tags(str(action.text)))
                                        case_list[8] = self.strip_tags(str(action.text))

                                    if action.tag == 'expectedresults':
                                        print('case_list[8]', self.strip_tags(str(action.text)))
                                        case_list[9] = self.strip_tags(str(action.text))
                                        print(case_list)
                                        spamwriter.writerow(case_list)
        csvfile.close()
     
    # def read_csv_to_xml(self,csv_file,xmlfile):
    #     #逐行读取CSV文件的内容，将内容写进以internalid为键，name，sumary，steps，expectresult为值得字典
    #     csv_file = os.path.join(os.path.dirname(__file__), csv_file)
    #     xmlfile = os.path.join(os.path.dirname(__file__), xmlfile)
    #     csv_file = open(csv_file,'rt')
    #     reader = csv.reader(csv_file)  
    #     case_dic = {}  
    #     for line in reader:  
    #         if reader.line_num == 1:  
    #             continue  
    #         if line[0] == "testcase":
    #             name = str(line[1])
    #             internalid = str(line[4])
    #             summary = line[6]
    #             steps = line[7]
    #             expectedresults = line[8]
    #             case_dic[internalid] = (name,summary,steps,expectedresults)
    #     csv_file.close()
    #     print( case_dic)
    #     #用ElementTree方法打开xml文件，逐行解析XML文件，发现case为tag的行，就将name，sumary，steps，expectresult，这几项用字典的值替换。
    #     tree = ET.ElementTree()
    #     tree.parse(xmlfile)
    #     root = tree.getroot()
    #     root_suite_name = root.attrib['name']
         
    #     for node in tree.iter():
    #         if node.tag == "testsuite":
    #             print( node.attrib['name'])
    #             sub_suite_name = node.attrib['name']
    #             if sub_suite_name == root_suite_name:
    #                 sub_suite_name = ""
    #             for child in node:
    #                 if child.tag == "node_order":
    #                     #print( child.text)
    #                     pass
    #                 if child.tag == "details":
    #                     pass
    #         if node.tag == "testcase":
    #             new_internalid = node.attrib['internalid']
    #             #将根目录和子目录的名字都写进了case名字中。如果不需要可以用下面那行注释掉的替换这一行
    #             node.attrib['name'] = root_suite_name+'_'+sub_suite_name+'_'+case_dic[new_internalid][0]
    #             #node.attrib['name'] = case_dic[new_internalid][0]
    #             print( node.attrib['name'])
    #             #解析tag为testcase的节点的子节点，并修改节点的值
    #             for child in node:
    #                 if child.tag == "node_order":
    #                     pass
    #                 if child.tag == "externalid":
    #                     pass
    #                 if child.tag == "summary":
    #                     child.text = case_dic[new_internalid][1]
    #                     child.text = str(child.text.replace('\n',"<p>"))
    #                 if child.tag == "steps":
    #                     child.text = str(case_dic[new_internalid][2])
    #                     child.text = str(child.text.replace('\n',"<p>"))
    #                 if child.tag == "expectedresults":
    #                     child.text = case_dic[new_internalid][3]
    #                     child.text = str(child.text.replace('\n',"<p>"))
    #     #将修改后的ElementTree对象写入xml文件中。
    #     tree.write(xmlfile,encoding='utf8')   
if __name__ == "__main__":
    test = XML_CSV()
    # 获取当前目录下的.xml文件
    allfile = os.path.dirname(os.path.abspath(__file__))
    allfile = os.listdir(allfile)
    print(allfile)
    for files in allfile:
        print(files)
        if os.path.splitext(files)[1]=='.xml':
            print('get you', files)
            test.read_xml_to_csv(files.split('.')[0]+'.csv', files)
            sleep(5)
    # test.read_csv_to_xml('pushmsg.csv','testsuites.xml')