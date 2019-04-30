# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# 配置文件地址
firefox_dir = r'C:\Users\肖欢\AppData\Roaming\Mozilla\Firefox\Profiles\2qs152iz.default'
# 加载配置
firefox_config = webdriver.FirefoxProfile(firefox_dir)
# 启动浏览器配置
dr = webdriver.Firefox(firefox_config)
dr.get('https://imooc.com')

dr.find_element_by_id('js-signin-btn').click()
WebDriverWait(dr, 5).until(lambda x: x.find_element_by_name('email').is_displayed)
dr.find_element_by_name('email').send_keys('13764236295')
dr.find_element_by_name('password').send_keys('1164821471')
dr.find_element_by_class_name('xa-login').click()

