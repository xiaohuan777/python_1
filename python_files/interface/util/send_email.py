# coding:utf-8

import smtplib
from email.mime.text import MIMEText

class SendEmail():
    def send_email(self, receive_list, sub, content):
        send_user = '1164821471@qq.com'
        # send_user = 'xiaohuan077.sina.com'
        # qq授权码：ikayhdcmxlmpffdi
        password = 'ikayhdcmxlmpffdi'
        host = 'smtp.qq.com'
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = sub
        message['From'] = send_user
        message['To'] = ';'.join(receive_list)
        server = smtplib.SMTP_SSL(host, 465)
        # server.connect(host, 25)
        # server.starttls()
        server.login(send_user, password)
        server.sendmail(send_user, receive_list, message.as_string())
    
    def main(self, pass_list, fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num
        sub = '接口自动化测试报告'
        receives = ['1139723906@qq.com','xiaohuan077@163.com']
        pass_result = '%.2f%%' %(pass_num/count_num*100)
        fail_result = '%.2f%%' %(fail_num/count_num*100)
        content = '此次一共运行%s个,通过个数为%s个，失败个数为%s个；通过率为%s，失败率为%s' %(count_num, pass_num, fail_num, pass_result, fail_result)
        self.send_email(receives, sub, content)

if __name__ == '__main__':
    send = SendEmail()
    send.main([1,2,3,5], [3,4,5,6,7,8])
