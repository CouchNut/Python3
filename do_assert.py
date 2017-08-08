#!/usr/local/bin python3

# -*- coding: utf-8 -*-

def foo(s):
	n = int(s)
	assert n != 0, 'n is zero!'
	return 10 / n

def main():
	foo('0')

main()

# 启动Python解释器时可以用-O参数来关闭assert：
# 关闭后，你可以把所有的assert语句当成pass来看。