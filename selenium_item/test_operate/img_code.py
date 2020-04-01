# coding = utf-8
from selenium import webdriver
from PIL import Image   # 需要安装 pillow 这个库
import pytesseract      # 识别验证码图片的库
from ShowapiRequest import ShowapiRequest
driver = webdriver.Chrome()
driver.get('http://5itest.cn/register')

# 解决图片验证码的问题（该方法适用干扰项很少的图片验证码）
driver.save_screenshot('D://imooc.png')
code_element = driver.find_element_by_id('getcode_num')
print(code_element.location)     # {'x':123,'y':345}
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width'] + left
height = code_element.size['height'] + top
page_img = Image.open('D://imooc.png')
code_img = page_img.crop((left,top,right,height))
code_img.save('D://imooc1.png')
img_text = pytesseract.image_to_string(code_img)


# 识别干扰项很多的图片验证码
r = ShowapiRequest("http://route.showapi.com/26-4","my_appId","my_appSecret" )
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image",r"D:\\imooc.png")
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(res.text)
