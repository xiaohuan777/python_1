from selenium import webdriver
import os
import time

dr = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('iframe/frame.html')
dr.get(file_path)

dr.switch_to_frame('f1')
dr.switch_to_frame('f2')

dr.find_element_by_id('kw').send_keys('selenium')
dr.find_element_by_id('su').submit()
time.sleep(2)

# dr.switch_to_window('windowName')     #多层窗口定位 



dr.close()

