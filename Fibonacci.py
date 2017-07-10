#!/usr/bin/python3

#  Fibonacci series

a , b = 0, 1

while b < 10:
	print(b, end=' ')
	# print('a = ', a, 'b = ', b)
	a , b = b, a + b
	# print('a = ', a, 'b = ', b)