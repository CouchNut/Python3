#!/usr/local/bin python3

# -*- coding: utf-8 -*-

' try sample'

__author__ = 'Copper'

try:
	print('try...')
	r = 10 / 2
	print('result:', r)
except ZeroDivisionError as e:
	print('except:', e)
else:
	print('no error!')
finally:
	print('finally...')

print('END')

try:
	print('try...')
	r = 10 / int('a')
	print('result:', r)
except ValueError as e:
	print('ValueError:', e)
except ZeroDivisionError as e:
	print('ZeroDivisionError:', e)
finally:
	print('finally...')

print('END')

# Python的错误其实也是class，所有的错误类型都继承自BaseException，
# 所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：
'''
try:
	foo()
except ValueError as e:
	print('ValueError')
except UnicodeError as e:
	print('UnicodeError')
'''
#  第二个 UnicodeError 永远也捕获不到，因为 UnicodeError 是 ValueError的子类，如果有，也被第一个except给捕获了

# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，
# 比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理：

def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	try:
		bar('0')
	except Exception as e:
		print('Error:', e)
	finally:
		print('finally...')

main()










































