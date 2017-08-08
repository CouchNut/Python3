#!/sur/local/bin python3

# -*- coding: utf-8 -*-

class Student(object):
	def __init__(self):
		self.name = 'Michale'

s = Student()
print(s.name)

# print(s.score)
'''
Traceback (most recent call last):
  File "special_getattr.py", line 12, in <module>
    print(s.score)
AttributeError: 'Student' object has no attribute 'score'
'''

# 要避免这个错误，除了可以加上一个score属性外，
# Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。
# 修改如下：
	
class Person(object):
	def __init__(self):
		self.name = 'Michale'

	def __getattr__(self, attr):	
		if attr=='score':
			return 99
		return AttributeError('\'Person\' object has no attribute \'%s\'' % attr)
		
p = Person()
print(p.score)
print(p.age)


# 利用完全动态的__getattr__，我们可以写出一个链式调用：
class Chain(object):
	def __init__(self, path=''):
		self._path = path

	def __getattr__(self, path):	
		return Chain('%s/%s' % (self._path, path))

	def __str__(self):
		return self._path

	__repr__ = __str__
		

print(Chain().status.user.timeline.list)



