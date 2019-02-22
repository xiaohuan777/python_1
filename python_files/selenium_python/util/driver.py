# coding:utf-8

from selenium import webdriver
from .get_by import GetByLocal
import time

class ActionDriver():
    
    # 打开浏览器
    def open_browser(self, *args):
        self.browser = args[0]
        if self.browser == 'chrome':
            self.dr = webdriver.Chrome()
        # elif self.browser == 'firefox':
        #     # 配置文件地址
        #     firefox_dir = r'C:\Users\肖欢\AppData\Roaming\Mozilla\Firefox\Profiles\2qs152iz.default'
        #     # 加载配置
        #     firefox_config = webdriver.FirefoxProfile(firefox_dir)
        #     self.dr = webdriver.Firefox(firefox_config)
        # else:
        #     self.dr = webdriver.Ie()
        return self.dr

    # 打开URL
    def get_url(self, *args):
        url = args[0]
        self.dr.get(url)

    # 获取定位元素
    def get_element(self, *args):
        ele = args[0]
        get_by_element = GetByLocal(self.dr)
        element = get_by_element.get_by_ele(ele)
        return element

    def send_key(self, *args):
        ele = args[0]
        value = args[1]
        element = self.get_element(ele)
        element.send_keys(value)

    def click_element(self, *args):
        ele = args[0]
        element = self.get_element(ele)
        element.click()

    def sleep_time(self, *args):
        time.sleep(5)

    def close_browser(self, *args):
        self.dr.close


if __name__ == '__main__':
    dr = ActionDriver()
    dr.open_browser('chrome')

