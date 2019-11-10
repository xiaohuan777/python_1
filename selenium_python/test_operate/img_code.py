#coding = utf-8
from selenium import webdriver
from PIL import Image   #需要安装 pillow 这个库
import pytesseract      #识别验证码图片的库

driver = webdriver.chrome()


# 解决图片验证码的问题
driver.save_screenshot('E://imooc.png')
code_element = driver.find_element_by_id('getcode_num')
print(code_element.location)     #{'x':123,'y':345}
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width'] + left
height = code_element.size['height'] + top
page_img = Image.open('E://imooc.png')
code_img = page_img.crop((left,top,right,height))
code_img.save('E://imooc1.png')
img_text = pytesseract.image_to_string(code_img)
