from functools import reduce


# reduce 的用法
# reduce本质：reduce(f, [x1, x2, x3, x4, x5]) ==> f(f(f(f(x1, x2), x3), x4), x5)

def add(x, y):
	return x + y


L =  reduce(add, [1, 3, 5, 6])

print(L)


# 把序列[1, 3, 5, 7, 9]变换成整数 13579，则使用reduce

def fn(x, y):
	return x * 10 + y

result = reduce(fn, [1, 3, 5, 7, 9])
print(result)


# 将 str 转换为 int 的函数

def char2num(s):
	return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]

result2 = reduce(fn, map(char2num, '13579'))
print(result2)

# 将上方代码整理成一个函数就是

def str2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):	
		return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
	return reduce(fn, map(char2num, s))

# str2int函数还可以使用 lambda 函数进一步简化

def str2int(s):
	return reduce(lambda x, y : x * 10 + y, map(char2num, s))

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

def normalize(name):
	return name[0].upper() + name[1:].lower()

L1 = ['Adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
	def multiplication(x, y):	
		return x * y
	return reduce(multiplication, L)

multiResult = prod([3, 5, 7, 9])
print(multiResult)

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def char2num(s):
		return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]

def str2float(s):
	if '.' in s:
		s = s.split('.')
		return reduce(lambda x, y:10*x+y, map(str2num, s[0])) + reduce(lambda x, y:x/10 = y, map(str2num, s[1][::-1]))/10
	else:
		return reduce(lambda x, y:10*x + y, map(str2num, s[0]))


print('str2float(\'123.456\') =', str2float('123.456'))






