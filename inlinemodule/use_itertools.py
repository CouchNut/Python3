#!/usr/local/bin python3

# -*- coding: utf-8 -*-

# 无限迭代器
import itertools

# count() 会创建一个无限的迭代器，
# 所以下列代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。
# natuals = itertools.count(1)
# for n in natuals:
# 	print(n)

# cycle() 会把传入的一个序列无限重复下去
cs = itertools.cycle('ABC')	# 注意字符串也是序列的一种
# for cc in cs:
# 	print(cc)

# repeat()负责把一个元素无限重复下去，
# 不过如果提供第二个参数就可以限定重复次数：
ns = itertools.repeat('A', 10)
for n in ns:
	print(n)


# 无限序列虽然可以无限迭代下去，
# 但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：	
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

# chain() 可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
	print(c)


# groupby() 把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBCCCAAA'):
	print(key, list(group))

print('=========')
# 如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
for key, group in itertools.groupby('AaaBBBbCcCAAa', lambda c : c.upper()):
	print(key, list(group))




