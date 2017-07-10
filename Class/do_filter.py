# filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。

# 在一个list中，删掉偶数，只保留奇数，可以这么写：
def is_add(n):
	return n % 2 == 1

L = list(filter(is_add, [1, 2, 3, 4, 5]))
print(L)

# 把一个序列中的空字符串删掉
def not_empty(s):
	return s and s.strip()
L2 = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(L2)

# 用filter 求素数

# 构造一个从3开始的奇数序列
def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

# 定义一个筛选函数
def _not_divisible(n):
	return lambda x: x % n > 0

# 定义一个生成器，不断返回下一个素数
def primes():
	yield 2
	it = _odd_iter()	# 初始序列
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n), it)	# 构造新序列

for n in primes():
	if n < 1000:
		print(n)
	else:
		break


# 判断一个数是否是回数
def is_palindrome(n):
	number = str(n)
	return number[:] == number[::-1]
		


output = filter(is_palindrome, range(1, 100000))
print(list(output))








