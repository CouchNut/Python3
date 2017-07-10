# 装饰器
def now():
	print('2017-7-9')

f = now
f()

print(now.__name__)

print(f.__name__)

# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
def log(func):
	def wrapper(*args, **kw):
		print('call %s()' % func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def now2():
	print('2017-7-9')

now2()


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，
# 写出来会更复杂。比如，要自定义log的文本：

def log(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s %s()' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log('execute')
def now3():
	print('2017-07-09')

now3()

print('------- now4() --------')
now4 = log('execute')(now3)
now4()


# 一个完整的decorator的写法如下：
# 无参数
import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s()' % func.__name__)
		return func(*args, **kw)
	return wrapper

# 带参数
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator


