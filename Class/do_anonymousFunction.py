# 匿名函数
f = lambda x : x * x
print(f)

print(f(5))

def build(x, y):
	return lambda: x * x + y * y

f2 = build(12, 13);
print(f2())