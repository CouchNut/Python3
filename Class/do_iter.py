# 使用isinstance()判断一个对象是否是Iterable对象：

print('------------- Iterable -----------')
from collections import Iterable

print(isinstance([], Iterable))	# True
print(isinstance({}, Iterable))	# True
print(isinstance('abc', Iterable)) # True
print(isinstance((x for x in range(10)), Iterable))	# True
print(isinstance(100, Iterable))	# False

print('------------- Iterator -----------')
from collections import Iterator

print(isinstance((x for x in range(10)), Iterator))	# True
print(isinstance([], Iterator))	# False
print(isinstance({}, Iterator))	# False
print(isinstance('abc', Iterator))	# False

# 生成器都是 Iterator 对象，但 list， dict， str 虽然是 Iterable, 却不是 Iterator
# 把 list、dict、str、等 Itearble 变成 Iterator 可以使用 iter() 函数：
print('------------- iter() 函数 -----------')
print(isinstance(iter([]), Iterator))	# True
print(isinstance(iter('abc'), Iterator))	# True

# 小结
# 凡是可作用于 for 循环的对象都是 Iterable 类型
# 凡是可作用于 next() 函数的对象都是 Iterator 类型，它们表示一个惰性计算的序列
# 集合数据类型如 list、dict、str等是 Iterable 类型，但不是 Iterator，不过可以通过iter() 函数获得一个Iterator对象。
# Python的for循环本质上就是通过不断调用next() 函数实现的




