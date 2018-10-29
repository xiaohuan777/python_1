# coding:utf-8
import socket

# 客户端
s = socket.socket()
s.connect(('127.0.0.1',6666))
print(s.recv(1024))
s.close()