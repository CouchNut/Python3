#!/usr/local/bin python3

# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
	
	def __init__(self):
		super(MyHTMLParser, self).__init__()
		self.getNameInfo = False
		self.getTimeInfo = False
		self.getLocationInfo = False

	def handle_starttag(self, tag, attrs):
		if attrs:
			if attrs[0][1] == 'event-title':
				# print('attrs: %s' % attrs)
				self.getNameInfo = True
			if tag == 'time':
				self.getTimeInfo = True
			if attrs[0][1] == 'event-location':
				self.getLocationInfo = True

	def handle_endtag(self, tag):
		# print('<%s>' % tag)
		pass

	def handle_startendtag(self, tag, attrs):
		# print('<%s>' % attrs)
		pass

	def handle_data(self, data):
		if self.getNameInfo == True:
			print('-----------------------')
			print('Name: %s' % data)
			self.getNameInfo = False
		if self.getLocationInfo == True:
			print('Location: %s' % data)
			self.getLocationInfo = False
		if self.getTimeInfo == True:
			print('Time: %s' % data)
			self.getTimeInfo = False
		

	def handle_comment(self, data):
		# print('<!--', data, '-->')
		pass

	def handle_entityref(self, name):
		# print('&%s;' % name)
		pass

	def handle_charref(self, name):
		# print('&#%s;' % name)
		pass


parser = MyHTMLParser()
parser.feed('''<html>
	<head></head>
	<body>
		<!-- test html parser -->
		<p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
	</body>
	</html>''')

# 找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，
# 然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。

# print('---------------------------------------------------------')
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org/events/python-events/')) as response:
	parser2 = MyHTMLParser()
	parser2.feed(response.read().decode('utf-8'))



