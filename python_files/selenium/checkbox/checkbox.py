from selenium import webdriver
import time
import os
# 配置文件地址
firefox_dir = r'C:\Users\肖欢\AppData\Roaming\Mozilla\Firefox\Profiles\2qs152iz.default'
# 加载配置
firefox_config = webdriver.FirefoxProfile(firefox_dir)
# 启动浏览器配置
dr = webdriver.Firefox(firefox_config)

file_path = 'file:///' + os.path.abspath('checkbox/checkbox.html')

inputs = dr.find_elements_by_tag_name('input')
print(inputs)
for input in inputs:
    if input.get_attribute('type') == 'checkbox':
        input.click()
time.sleep(2)
  