from selenium import webdriver
import time
import os       #调用本地文件，引入os包

# 配置文件地址
firefox_dir = r'C:\Users\肖欢\AppData\Roaming\Mozilla\Firefox\Profiles\2qs152iz.default'
# 加载配置
firefox_config = webdriver.FirefoxProfile(firefox_dir)
# 启动浏览器配置
dr = webdriver.Firefox(firefox_config)

file_path = 'file:///' + os.path.abspath('checkbox/checkbox.html')
dr.get(file_path)

inputs = dr.find_elements_by_css_selector('input[type=checkbox]')

for input in inputs:
    input.click()
time.sleep(2)

print (len(inputs))

inputs.pop().click()        #去掉最后一个
time.sleep(2)
dr.close()
  