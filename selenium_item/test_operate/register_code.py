from selenium import webdriver
import time
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest

driver = webdriver.Chrome()

def driver_init():
    driver.get('http://www.5itest.cn/register')
    driver.maximize_window()
    time.sleep(5)

# 获取element 信息
def get_element(id):
    element = driver.find_element_by_id(id)
    return element

# 获取随机数
def get_range_user():
    user_info = ''.join(random.sample('1234567890abcdefg',8))
    return user_info


# 获取图片
def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_element = driver.find_element_by_id('getcode_num')
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width'] + left
    height = code_element.size['height'] + top
    page_img = Image.open(file_name)
    code_img = page_img.crop((left,top,right,height))
    code_img.save(file_name)

# 解析图片，获取验证码
def code_online(file_name):
    r = ShowapiRequest("http://route.showapi.com/184-4","118735","4ff2b63a42cf46f9a7f3d8b635ba260d" )
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "0")
    r.addFilePara("image",file_name)
    res = r.post()
    print(res.text)
    text = res.json()['showapi_res_body']['Result']
    return text

# 运行主程序
def run_main():
    user_name_info = get_range_user()
    user_email = user_name_info + '@163.com'
    file_name = 'D:/imooc_image/imooc.png'
    driver_init()
    get_element('register_email').send_keys(user_email)
    get_element('register_nickname').send_keys(user_name_info)
    get_element('register_password').send_keys('111111')
    get_code_image(file_name)
    text = code_online(file_name)
    get_element('captcha_code').send_keys(text)
    get_element('register-btn').click()
    driver.close()

run_main()