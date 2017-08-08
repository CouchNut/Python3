#!/usr/local/bin python3

# -*- coding: utf-8 -*-

# 多重继承
# 功能类
class Runnable(object):	
	def run(self):
		print('Running...')
		

class Flyable(object):
	def fly(self):
		print('Flying...')

# 具体类
class Animal(object):
	pass

# 哺乳类
class Mammal(Animal):
	pass

# 鸟类
class Bird(Animal):
	pass

# 各种动物
class Dog(Mammal, Runnable):
	pass

class Bat(Mammal, Flying):
	pass

class Parrot(Bird, Flying):
	pass

class Ostrich(Bird, Runnable):
	pass



		
		
		
		
		



		
