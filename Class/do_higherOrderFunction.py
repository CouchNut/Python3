print(abs(-10))


print(abs)

x = abs(-10)
print(x)


f = abs
print(f)

print(f(-10))

# abs = 10
# print(abs(-10))

def add(x, y, f):	
	return f(x) + f(y)

print(add(-5, 6, abs))
