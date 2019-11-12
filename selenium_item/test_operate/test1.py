# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
import random


# 引入 radom 包，生成随机字符串；解决注册多用户的问题
for i in range(0,5):
    user_name = '137' + ''.join(random.sample('1234567890',8))
    print(user_name)


driver = webdriver.Chrome()
driver.get('http://mp.tt.cn')
time.sleep(2)
EC.title_contains('东方号')       # 通过页面title来判断页面是否正常打开

# visibility_of_element_located 方法，可以判断页面元素是否存在，存在执行后续操作
locator = (By.CLASS_NAME,'el-input')
WebDriverWait(driver,1).until(EC.visibility_of_element_located(locator))


# input_ele1 = driver.find_element_by_id('el-input').send_keys('13764236295')
imput_ele2 = driver.find_elements_by_class_name('el-input__inner')[0]
imput_ele2.send_keys('13764236295')
ele2_attr = imput_ele2.get_attribute('value')   # get_attribute 方法，记住
print(ele2_attr)
# driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[2]/form/div[1]/div/div/input')


time.sleep(2)
driver.close()
