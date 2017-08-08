#!/usr/local/bin python3

# -*- coding: utf-8 -*-

class FooError(ValueError):
	pass

def foo(s):
	n = int(s)
	if n == 0:
		raise FooError('invalid value: %s' % s)
	return 10 / n

def bar():
	try:
		foo('0')
	except ValueError as e:
		print('ValueError!')
		raise


bar()

# foo('0')





		



