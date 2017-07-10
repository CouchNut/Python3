# 偏函数
print(int('12345'))


def int2(x, base=2):
	return int(x, base)

print(int2('101010'))

# functools.partial就是帮助我们创建一个偏函数的
import functools
int2 = functools.partial(int, base = 2)

print(int2('1000000'))