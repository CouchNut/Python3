#!/usr/bin/python3
import sys


# 迭代器
print("================ 迭代器 ================")

list = [1,2,3,4]

it = iter(list)

# print(next(it))
# print(next(it))

# for 循环遍历

print("--------- for 循环遍历 ----------")
for x in it:
	print(x, end=' ')

print()


# while 循环遍历
print("--------- while 循环遍历 ----------")
list2 = [1, 2, 3, 4]
it2 = iter(list2)
while True:
	try:
		print(next(it2), end=' ')
	except StopIteration:
		sys.exit()
print()