#-*- coding:utf-8 -*-
'''
webdriver set_headless()
'''

from time import sleep
from selenium import webdriver
import os


pic = os.path.join(os.path.dirname(__file__), 'baidu-no.png')
opt = webdriver.ChromeOptions()
opt.add_argument('window-size=1902,1080')
opt.set_headless()
driver = webdriver.Chrome(options=opt)

driver.get('http://172.16.100.22:6002/')
# driver.maximize_window()
sleep(1)
#driver.save_screenshot(pic)
username = driver.find_element_by_id('username')
username.send_keys('admin')
sleep(1)
passwd = driver.find_element_by_id('password')
passwd.send_keys('tebon2017')
sleep(1)
kaptcode = driver.find_element_by_id('kaptchacode')
kaptcode.send_keys('888888')
sleep(1)
login = driver.find_element_by_xpath('/html/body/div/form/ul/li[5]/button')
login.click()
driver.close()

# print(driver.page_source)