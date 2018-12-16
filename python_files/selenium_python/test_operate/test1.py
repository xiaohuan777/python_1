#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.get('https://juejin.im/activities')
time.sleep(2)
EC.title_contains('动态')