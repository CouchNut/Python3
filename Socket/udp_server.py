#!/usr/local/bin python3

# -*- coding: utf-8 -*-

import socket, threading, time

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 监听端口 9999
s.bind(('127.0.0.1', 9999))

# 开始监听，并设置等待连接的最大数量
print('Bind UDP on 9999')

# 通过一个永久循环来接受来自客户端的连接
while True:
	# 接受一个新的连接
	data, addr = s.recvfrom(1024)
	print('Received from %s:%s.' % addr)
	s.sendto(b'Hello, %s!' % data, addr)


