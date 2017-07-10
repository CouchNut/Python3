for ch in 'ABC':
	print(ch)

# 判断一个对象是否是可迭代对象
# 通过 collections 模块的 Iterable 类型判断

from collections import Iterable
 
print(isinstance('abc', Iterable))	# str 是否可迭代 True

print(isinstance([1, 2, 3], Iterable)) # list 是否可迭代  True

print(isinstance(123, Iterable))	# 整数是否可迭代	False


for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)

for x, y in [(1, 2), (2, 4), (3, 9)]:
	print(x, y)
	