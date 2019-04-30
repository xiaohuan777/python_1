# coding:utf-8
import socket

# 服务端
s = socket.socket()
s.bind(('127.0.0.1', 6666))
s.listen(5)

while True:
    c,addr = s.accept()
    print('连接地址',addr)
    c.send('welcome')
    c.close()