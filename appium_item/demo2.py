# coding = utf-8
import uiautomator2 as u2

# wifi 连接手机
d = u2.connect('192.168.2.4')
# print(d.device_info)

# 打开 app
d.app_start('cn.com.open.mooc')

'''
img = d.app_icon('cn.com.open.mooc')
img.save('icon.png')
print(d.app_info('cn.com.open.mooc'))

'''

d.wait_activity('cn.com.open.mooc', timeout=3)
# d.exists(text='推荐')

d(description="账号").click()
d(resourceId="cn.com.open.mooc:id/rl_login_before").click()
d(resourceId="cn.com.open.mooc:id/accountClear").click()
d(resourceId="cn.com.open.mooc:id/accountEdit").send_keys('13162819403')
d(resourceId="cn.com.open.mooc:id/passwordEdit").send_keys('Aa111111')
d(resourceId="cn.com.open.mooc:id/login").click()
# d.exists(text='点击登录')
d.wait_activity('cn.com.open.mooc', timeout=2)
d.swipe(0.5, 0.5, 0.5, 0.2)
d(resourceId="cn.com.open.mooc:id/ie_setting").click()
d(resourceId="cn.com.open.mooc:id/logout").click()
d(resourceId="cn.com.open.mooc:id/positiveBtn").click()

d.wait_activity('cn.com.open.mooc', timeout=1)

d.app_stop('cn.com.open.mooc')