#!/usr/local/bin/python3

'''
class Student(object):
	def __init__(self, name):
		super(Student, self).__init__()
		self.name = name

s  = Student('Copper')
s.score = 90
print(s.score)
'''

class Student(object):
	name = 'Student'

# 创建实例s
s = Student()
# 打印 name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(s.name)

# 打印类的name属性
print(Student.name)

s.name = 'Michale'
print(s.name)
print(Student.name)

print('删除s.name之后')
del s.name
print(s.name)