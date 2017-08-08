#!/usr/local/bin python3

# -*- coding: utf-8 -*-

class Student(object):

	def get_score(self):
		return self._score

	def set_score(self, score):
		if not isinstance(score, int):
			raise ValueError('score must be an integer!')
		if score < 0 or score > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._score = score

s = Student()
s.set_score(89) # ok!
print(s.get_score())

# s.set_score(9999)


# 装饰器（decorator）可以给函数动态加上功能
# 对于类的方法，装饰器一样起作用。
# Python内置的@property装饰器就是负责把一个方法变成属性调用的：

class Person(object):
	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, score):
		if not isinstance(score, int):
			raise ValueError('score must be an integer!')
		if score < 0 or score > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._score = score

p = Person()
p.score = 80	# ok 实际转化为 s.set_score(60)
print(p.score)	# ok 实际转化为 s.get_score()


class Men(object):
	
	@property
	def birth(self):
		return self._brith

	@birth.setter
	def birth(self, value):
		self._brith = value

	@property
	def age(self):
		return 2017 - self._brith

m = Men()

m.birth = 1992
print(m.birth)
print(m.age)
	
# m.age = 18	# 错误
'''
错误提示：

Traceback (most recent call last):
  File "use_property.py", line 66, in <module>
    m.age = 18
AttributeError: can't set attribute
'''


print('-------- 练习 --------')

class Screen(object):
	
	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, width):
		self._width = width


	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, height):
		self._height = height


	@property
	def resolution(self):
		return self._width * self._height


s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)




