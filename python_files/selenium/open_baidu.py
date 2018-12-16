# -*- coding: utf-8 -*- 
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys     #引入键盘按键操作keys包
from selenium.webdriver.common.action_chains import ActionChains        #引入鼠标事件包

# 配置文件地址
# firefox_dir = r'C:\Users\肖欢\AppData\Roaming\Mozilla\Firefox\Profiles\2qs152iz.default'
# 加载配置
# firefox_config = webdriver.FirefoxProfile(firefox_dir)
# 启动浏览器配置
dr = webdriver.Firefox()

dr.get('https://baidu.com')
dr.find_element_by_id('kw').send_keys('selenium')

#清除输入框的信息
dr.find_element_by_id('kw').clear()

# dr.find_element_by_id('kw').send_keys(Keys.TAB)     #用tab清除

#再输入Python
dr.find_element_by_id('kw').send_keys('python')

#submit操作百度搜索
# dr.find_element_by_id('su').submit()

dr.find_element_by_id('su').send_keys(Keys.ENTER)     #用enter键替代submit   

time.sleep(2)
#获取text
# data_text = dr.find_element_by_link_text('新闻').text
# print(data_text)
time.sleep(2)

#调整浏览器大小
# dr.set_window_size(480,800)

#模拟浏览器前进，后退
first_url = 'http://www.baidu.com'
second_url = 'http://news.baidu.com'
dr.get(first_url)
print('now access %s' %first_url)
dr.get(second_url)
dr.back()
time.sleep(2)
dr.forward()
time.sleep(2)

#浏览器全屏显示
# dr.maximize_window()

# dr.find_element_by_id('kw').send_keys(u'中文乱码问题，前面加u，头部加utf-8')

#鼠标事件
# qqq = dr.find_element_by_id('abc')
# ActionChains(dr).context_click(qqq).perform()     #鼠标右键操作
# ActionChains(dr).double_click(qqq).perform()      #双击

# element = dr.find_element_by_name('source')
# target = dr.find_element_by_name('target')
# ActionChains(dr).drag_and_drop(element,target).perform()      #拖拽


dr.close()








