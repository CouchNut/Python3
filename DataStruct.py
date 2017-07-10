#@/usr/bin/python3

# List方法的使用

a = [66.25, 333, 333, 1, 1234, 5]

print(a.count(333), a.count(66.25), a.count('x'))  # 2 1 0


print(a)			# [66.25, 333, 333, 1, 1234, 5]

a.insert(2, -1)		
print(a)			# [66.25, 333, -1, 333, 1, 1234, 5]

a.append(333)
print(a)			# [66.25, 333, -1, 333, 1, 1234, 5, 333]

print(a.index(333)) # 1  index(333) 获取第一个333所在的位置

a.remove(333)		# 删除第一个333
print(a)			# [66.25, -1, 333, 1, 1234, 5, 333]

a.reverse()			# 反转该列表
print(a)			# [333, 5, 1234, 1, 333, -1, 66.25]

a.sort()			# 对列表中的元素排序
print(a)			# [-1, 1, 5, 66.25, 333, 333, 1234]


# 将列表当做堆栈使用
print('-------------- 将列表当做堆栈使用 -------------')
stack = [3, 4, 5]
stack.append(6)		# 追加元素
stack.append(7)

print(stack)

stack.pop()		# 移除栈顶元素

print(stack)

# 将列表当作队列使用
print('-------------- 将列表当作队列使用 -------------')

from collections import deque

queue = deque(['Eric', 'Jhon', 'Michael'])
queue.append("Terry")
queue.append("Graham")
queue.popleft()

print(queue)

queue.popleft()

print(queue)

# 列表推导式
print('--------------列表推导式-------------')

vec = [2, 4, 6]

print([3 * x for x in vec])
print([[x, x ** 2] for x in vec])

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([wepon.strip() for wepon in freshfruit])

print([3 * x for x in vec if x > 3])
print([3 * x for x in vec if x < 2])

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print([x * y for x in vec1 for y in vec2])
print([x + y for x in vec1 for y in vec2])

print([vec1[i] * vec2[i] for i in range(len(vec1))])

print([str(round(355/113, i)) for i in range(1, 6)])


# 嵌套列表解析
print('--------------嵌套列表解析-------------')
print('-------------- 3X4 矩阵列表 -------------')

matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
]

print(matrix)

# 将 3 X 4的矩阵转换为 4 X 3 列表
print([[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
	transposed.append([row[i] for row in matrix])

print(transposed)

transposed2 = []

for i in range(4):
	transposed_row = []
	for row in matrix:
		transposed_row.append(row[i])
	transposed2.append(transposed_row)

print(transposed2)


# del 语句
print('-------------- del 语句 ---------------')

a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)
del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)

# 元组和序列
print('-------------- 元组和序列 ---------------')
t = 12345, 54321, 'hello!'

print(t[0])

print(t)

u = t, (1, 2, 3, 4, 5)
print(u)

# 集合
print('-------------- 集合 -----------------')
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)	# {'pear', 'orange', 'apple', 'banana'}

print ('orange' in basket)	# True

print('crabgrass' in basket) # False

# 以下演示了两个集合的操作
a = set('abracacadabra')
b = set('alacazam')

# a 中唯一的字母
print(a)

# 在 a 中的字母，但是不在 b 中
print(a - b)  

# 在 a 中或在 b 中的字母
print(a | b)

# 在 a 中也在b中的字母
print(a & b)

# 在 a 或 b 中的字母，但不同时在 a 和 b 中
print(a ^ b)

print('-------------- 字典 ---------------')
tel = {'jack' : 4098, 'sape' : 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])

del tel['sape']
print(tel)
tel['irv'] = 4127
print(tel)

print(list(tel.keys()))

print(sorted(tel.keys()))

print('guido' in tel)

print('jack' in tel)

print('-------------- 遍历技巧 ---------------')
print('遍历字典')
knights = {'gallahad': 'the pure', 'robin' : 'the brave'}
for k, v in knights.items():
	print(k,v)

print('遍历序列')
# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
for i, v in enumerate(['tic', 'tac', 'toe']):
	print(i, v)

# 同时遍历两个或更多的序列，可以使用 zip() 组合：
question = ['name', 'quest', 'favorite color']
answer = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(question, answer):
	print('What is your {0}? It is {1}.'.format(q, a))
