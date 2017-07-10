# 创建一个generator，有很多种方法。
# 第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：

L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))
# print(g)

for n in g:
	print(n)

# 斐波那契
print('-------------- 斐波那契 -------------')
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		# print(b)
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'

print(fib(10))

# 如果一个函数定义中包含 yield 关键字，那么这个函数就不再是一个普通的函数，而是一个 generator


def odd():
	print('step 1')
	yield 1
	print('step 2')
	yield(3)
	print('step 3')
	yield(5)

o = odd()

# print(next(o))

for n in fib(6):
	print(n)

g = fib(6)
while True:
	try:
		x = next(g)
		print("g:", x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break


# 杨辉三角
def triangles():
	max_len = 10
	a = [1]
	yield a
	while len(a) < max_len:
		a = [1] + [a[k] + a[k+1] for k, v in enumerate(a) if k >= 0 and k < len(a) - 1] + [1]
		yield a

n = 0
for t in triangles():
	print(t)
	n = n + 1
	if n == 10:
		break






