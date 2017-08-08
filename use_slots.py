#!/usr/local/bin/python3

# -*- coding: utf-8 -*-

# 当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，
# 这就是动态语言的灵活性。
# 先定义class：
 

class Student():
	pass


s = Student()
print('------ 给实例绑定一个属性 ------')
s.name = 'Michale' # 动态的给实例绑定一个属性
print(s.name)

print('---- 给实例绑定一个方法 ----')
def set_age(self, age):
	self.age = age

from types import MethodType
# 给实例绑定一个方法
s.set_age = MethodType(set_age, s)
s.set_age(24)
print(s.age)

# 给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student()
# s2.set_age(34)
'''
Traceback (most recent call last):
  File "use_slots.py", line 31, in <module>
    s2.set_age(34)
AttributeError: 'Student' object has no attribute 'set_age'
'''

# 为了给所有的实例绑定方法，可以给class绑定方法
def set_score(self, score):
	self.score = score

Student.set_score = set_score

s.set_score(90)
print(s.score)

s2.set_score(89)
print(s2.score)

print('-------- 使用 __slots__ --------')

# 如果我们想要限制实例的属性怎么办？
# 比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，
# 定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

class Person():
	__slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

p = Person()
p.name = 'Copper'	# 绑定属性 'name'
p.age = 25			# 绑定属性 'age'
# p.score = 99		# 绑定属性 'score'
'''
绑定属性 'score'出现的问题：

	Traceback (most recent call last):
	  File "use_slots.py", line 64, in <module>
	    p.score = 99		# 绑定属性 'score'
	AttributeError: 'Person' object has no attribute 'score'
'''

# 注意：
# 使用__slots__时，__slots__ 定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

class OldPerson(Person):
	pass

op = OldPerson()
op.score = 99
print(op.score)
	
# 除非在子类中也定义了 __slots__ ，这样子类实例允许定义的属性就是自身的 __slots__ 加上父类的 __slots__








