#!/sur/local/bin python3

# -*- coding: utf-8 -*-

# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：

class Fib(object):
	
	# 不支持切片去下标值
	def __getitem__(self, n):
		a, b = 1, 1
		for x in range(n):
			a, b, = b, a + b
		return a
		
		
f = Fib()
print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[4])

print(list(range(100))[5:10])

print('--------- 支持切片的类 ----------')

class Fib2(object):
	
	def __getitem__(self, n):
		if isinstance(n, int):		# n 是索引
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a

		if isinstance(n, slice):	# n 是切片
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b  = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b 
			return L



# 试试切片
f2 = Fib2()
print(f2[0:5])

print(f2[:10:2])





			
		
		