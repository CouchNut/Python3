#!/usr/local/bin python3

# -*- coding: utf-8 -*-


'''
GET /：首页，返回Home；

GET /signin：登录页，显示登录表单；

POST /signin：处理登录表单，显示登录结果。

'''

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_from():
	return '''
		<form action="/signin" method="post">
		<p><input name="username"></p>
		<p><input name="password" typt="password"></p>
		<p><button type="submit">Sing In</button></p>
		</form>
	'''

@app.route('/signin', methods=['POST'])
def signin():
	# 需要从request对象读取表单内容
	if request.form['username'] == 'admin' and request.form['password'] == 'password':
		return '<h1>Hello, admin!</h1>'
	return '<h3>Bad username or password!</h3>'

if __name__ == '__main__':
	app.run()







