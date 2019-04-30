from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import os
import time 

dr = webdriver.Firefox()
file = 'file:///' + os.path.abspath('level_target/level.html')
dr.get(file)

dr.find_element_by_link_text('Link1').click()

WebDriverWait(dr, 10).until(lambda this_driver:this_driver.find_element_by_id('dropdown').is_displayed())

menu = dr.find_element_by_link_text('Something else here')

webdriver.ActionChains(dr).move_to_element(menu).perform()

time.sleep(2)
dr.close()

