#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 运行server.py后 运行client.py 进行测试
import socket
s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)
while True:
	c, addr = s.accept()
	print '连接地址:', addr
	c.send('欢迎访问！')
	c.close();