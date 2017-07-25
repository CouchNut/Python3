#!/sur/local/bin python3

# -*- coding: utf-8 -*-


class Student(object):
	def __init__(self, name):
		self.name = name

	def __call__(self):
		print('My name is %s.' % self.name)

s = Student('Michak')
s()	# self 参数不要传入

print(callable(Student('Copper')))
print(callable(max))
print(callable([1, 2, 3]))
print(None)
print(callable('str'))