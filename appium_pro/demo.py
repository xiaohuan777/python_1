#coding = utf-8
from appium import webdriver
def get_driver():
    capabilities = {
        "deviceName": "QLXBBBA631500990",
        "platformName": "Android",
        "appPackage":"cn.com.open.mooc",
        "appActivity":"com.imooc.component.imoocmain.splash.MCSplashActivity"
        "noreset":"true"
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
    return driver


#获取屏幕的高度
def get_size():
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return(width,height)

#向左滑动
def swipe_left():
    x1 = get_size()[0]/10
    x2 = get_size()[0]/10*9
    y = get_size()[1]/2
    driver.swipe(x2,y,x1,y)

#向右滑动
def swipe_right():
    driver = get_driver()
    x1 = get_size()[0]/10
    x2 = get_size()[0]/10*9
    y = get_size()[1]/2
    driver.swipe(x1,y,x2,y)


#向上滑动
def swipe_up():
    y1 = get_size()[0]/10
    y2 = get_size()[0]/10*9
    x = get_size()[1]/2
    driver.swipe(x,y2,x,y1)


#向下滑动
def swipe_down():
    y1 = get_size()[0]/10
    y2 = get_size()[0]/10*9
    x = get_size()[1]/2
    driver.swipe(x,y1,x,y2)


def swipe_on(direction):
    if direction == 'up':
        swipe_up()
    elif direction == 'down':
        swipe_down()
    elif direction == 'left':
        swipe_left()
    else:
        swipe_right()


def go_login():
    driver.find_element_by_xpath("//*[@content-desc='账号']").click()
    driver.find_element_by_id('cn.com.open.mooc:id/header_line').click()
    driver.find_element_by_id('cn.com.open.mooc:id/accountEdit').send_keys('16621175178')
    driver.find_element_by_id('cn.com.open.mooc:id/passwordEdit').send_keys('1164821471')
    driver.find_element_by_id('cn.com.open.mooc:id/login').click()




    
#启动app
driver = get_driver()
time.sleep(1)
go_login()