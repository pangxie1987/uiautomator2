# -*- coding: utf-8 -*-  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time
import csv
import os
# import urllib2
import urllib.request as urllib2
import re
import requests
import random
from imp import reload
reload(sys)
# driver = webdriver.Firefox()
driver = webdriver.Chrome()
# 爬去url
url = 'https://s.1688.com/company/company_search.htm?keywords=%BA%EC%C5%A3&button_click=top&earseDirect=false&n=y'
# 登入url
login_url = 'https://login.taobao.com/member/login.jhtml'
# 跳转登入页面
driver.get(login_url)
# 睡眠5秒
time.sleep(5)
driver.find_element_by_id("J_Quick2Static").click()
time.sleep(2)
# 输入自己的账号密码
driver.find_element_by_name('TPL_username').send_keys('账号')
driver.find_element_by_name('TPL_password').send_keys('密码')
driver.find_element_by_name('TPL_password').send_keys(Keys.ENTER)
time.sleep(10)
print("请在15秒之类验证完毕，否则无效。。。。。。。。。。")
# 验证地址
driver.get(url)
time.sleep(15)
print("请在15秒之类再次验证，否则无效。。。。。。。。。。")
driver.get(url)
time.sleep(5)
driver.get(url)
csvfile = file('data.csv','wb')
writer = csv.writer(csvfile)
writer.writerow((
u'企业名称'.encode('gbk'),
u'主页'.encode('gbk'),
u'产品'.encode('gbk'),
u'联系人'.encode('gbk'),
u'职位'.encode('gbk'),
u'电话'.encode('gbk'),
u'地址'.encode('gbk'),
))
# 匹配每条商户
pattern = re.compile('<div class="contcat-desc".*?>(.*?)</div>', re.S)
# 定义电话正则
tel_patten = re.compile('<dd>(.*?)</dd>', re.S)
# 定义移动电话正则
member_name_pattern = re.compile('<a.*?class="membername".*?>(.*?)</a>', re.S)
# 职位正则
job_name_pattern = re.compile('<a.*?class="membername".*?</a>(.*?)<a', re.S)
# 定义地址正则
address_pattern = re.compile('"address">(.*?)</dd>', re.S)
# 公司名称
title_pattern = re.compile('<a.*?class="list-item-title-text".*?>(.*?)</a>', re.S)
cookies = '自己F12查看登入后的cookies，谢谢合作'
for j in range(74):
	for i in range(33):
		try:
			# if True:
			print("...........................")
			# 取标题
			xpath_title_str = '//*[@id="offer'+str(i+1)+'"]/div[1]/div[2]/div[1]/a[1]'
			title_xpath = driver.find_element_by_xpath(xpath_title_str)
			title_value = title_xpath.get_attribute('title')
			# 获取主页
			href_value = ((title_xpath.get_attribute('href')).split("?"))[0]+'page/contactinfo.htm'
			# 经营范围
			xpath_product_str = '//*[@id="offer'+str(i+1)+'"]/div[1]/div[2]/div[3]/div[1]/div[1]/a'
			product_xpath = driver.find_element_by_xpath(xpath_product_str)
			product_value = (product_xpath.text).replace('\n','').replace(' ','').replace('\r','')
			# 组建头部
			headers = {
			"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"Accept-Encoding":"gzip, deflate, sdch, br",
			"Accept-Language":"zh-CN,zh;q=0.8",
			"Referer":href_value,
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
			}
			cookies_info = {}
			for line in cookies.split(';'):   
				name,value=line.strip().split('=',1)  
				cookies_info[name]=value  
				response = requests.get(href_value, cookies=cookies_info, headers=headers)
				html = response.text
				info = re.findall(pattern, html)
				try:
					info = info[0]
				except Exception as e:
					continue
				tel = re.findall(tel_patten, info)
				try:
					tel = tel[0]
					tel = tel.strip()
					tel = tel.replace(' ','-')
				except Exception as e:
					tel = ''
					# //*[@id="site_content"]/div[1]/div/div/div/div[2]/div/div[1]/div[1]/dl/dd/text()
					# //*[@id="site_content"]/div[1]/div/div/div/div[2]/div/div[1]/div[1]/dl/dd/text()
					member_name = re.findall(member_name_pattern, html)
					# 取职位
					job_value = re.findall(job_name_pattern, html)
				try:
					job_value = job_value[0].strip()
					job_value = job_value.replace('&nbsp;',' ')
				except Exception as e:
					job_value = ''
				try:
					member_name = member_name[0].strip()
				except Exception as e:
					member_name = ''
					address = re.findall(address_pattern, html)
				try:
					address = address[0].strip()
				except Exception as e:
					address = ''
					print('tel:' + tel)
					print('member_name:' + member_name)
					data = (
					title_value.encode('gbk', 'ignore'),
					href_value.encode('gbk', 'ignore'),
					product_value.encode('gbk','ignore'),
					member_name.encode('gbk','ignore'),
					job_value.encode('gbk','ignore'),
					tel.encode('gbk','ignore'),
					address.encode('gbk','ignore')
					)
					writer.writerow(data)
				except Exception as e:
				# driver.refresh()
				# time.sleep(30)
					pass
				js = 'var q=document.documentElement.scrollTop=30000'
				driver.execute_script(js)
				time.sleep(1)
				page = driver.find_element_by_css_selector("a[class=page-next]")
				page.click()
				time.sleep(2)
				print("stop)..................")
		except Exception as e:
			print(e)
csvfile.close()
driver.close()