#!/usr/local/bin python3

# -*- coding: utf-8 -*-

# 枚举的使用

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():	
	print(name, '=>', member, ',', member.value)


# @unique 可以帮助我们检查保证没有重复值
@unique
class weekday(Enum):
	Sun = 0			# Sun 的value被设定为0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

day1 = weekday.Mon
print(day1)
print(weekday.Tue)
print(weekday['Tue'])
print(weekday.Tue.value)
print(day1 == weekday.Mon)
print(day1 == weekday.Tue)
print(weekday(1))
print(day1 == weekday(1))
# print(weekday(7))
'''
Traceback (most recent call last):
  File "use_enum.py", line 35, in <module>
    print(weekday(7))
  File "/usr/local/Cellar/python3/3.6.1/Frameworks/Python.framework/Versions/3.6/lib/python3.6/enum.py", line 291, in __call__
    return cls.__new__(cls, value)
  File "/usr/local/Cellar/python3/3.6.1/Frameworks/Python.framework/Versions/3.6/lib/python3.6/enum.py", line 533, in __new__
    return cls._missing_(value)
  File "/usr/local/Cellar/python3/3.6.1/Frameworks/Python.framework/Versions/3.6/lib/python3.6/enum.py", line 546, in _missing_
    raise ValueError("%r is not a valid %s" % (value, cls.__name__))
ValueError: 7 is not a valid weekday
'''

for name, member in weekday.__members__.items():
	print(name, '=>', member)




		

