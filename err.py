#!/usr/local/bin python3

# -*- coding: utf-8 -*-

# 调用堆栈
print('----- 调用堆栈 -----')
def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	bar('0')

main()

