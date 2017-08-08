#!/usr/local/bin python3

# -*- coding: utf-8 -*-

import socket, threading, time

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听端口 9999
s.bind(('127.0.0.1', 9999))

# 开始监听，并设置等待连接的最大数量
s.listen(5)
print('Waiting for connection...')

def tcplink(sock, addr):
	print('Accept new connection from %s:%s' % addr)
	sock.send(b'Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('Connection from %s:%s closed.' % addr)

# 通过一个永久循环来接受来自客户端的连接
while True:
	# 接受一个新的连接
	sock, addr = s.accept()
	# 创建新的线程来处理TCP连接
	t = threading.Thread(target=tcplink, args=(sock, addr))
	t.start()


