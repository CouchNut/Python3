
l1 =  list(range(1, 11))
print(l1)

# 生成[1x1, 2x2, 3x3],方法一是循环：
L = []
for x in range(1, 11):
	L.append(x * x)

print(L)
	
# 但是循环太繁琐，而列表生成则可以用一行语句代替循环生成上面的list
print([x * x for x in range(1, 11)])

print([x * x for x in range(1, 11) if x % 2 == 0])

# 两层循环，可以生成全排列

print([m + n for m in 'ABC' for n in 'XYZ'])

# 列出当前目录下的所有文件和目录名，
import os 

print([d for d in os.listdir('.')])	# os.dirlist可以列出文件可目录


# for 循环其实可以同时使用两个甚至多个变量，比如dict 的 items() 可以同时迭代key 和 value

d = {'x' : 'A', 'y' : 'B', 'z' : 'C'}
for k, v in d.items():
	print(k, '=', v)

# 列表生成式也可以使用两个变量来生成list：

print([k + '=' + v for k, v in d.items()])

# 把一个list中的所有字符串变成小写
L = ["Hello", "World", "IBM", "Apple"]

print([s.lower() for s in L])

L = ["Hello", "World", "IBM", "Apple", 123]
# print([s.lower() for s in L])	# AttributeError: 'int' object has no attribute 'lower'

x = 'abc'
y = 123

print(isinstance(x, str))	# True
print(isinstance(y, str))	# False


L1 = ["Hello", "World", 18, "Apple", None]

L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)































































