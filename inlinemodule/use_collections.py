#!/usr/local/bin python3

# -*- coding: utf-8 -*-

# namedtuple
print('----- namedtuple -----')
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

print(isinstance(p, Point))
print(isinstance(p, tuple))

# 使用坐标和半径表示一个园，
Circle = namedtuple('Circle', ['x', 'y', 'r'])

# deque
print('----- deque -----')
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
q.pop()
print(q)
q.popleft()
print(q)

# defaultdict
print('----- defaultdict -----')
from collections import defaultdict
dd = defaultdict(lambda:'N/A')
print(dd)
dd['key1'] = 'abc'
print(dd)
print(dd['key2'])


# OrderedDict
print('----- OrderedDict -----')
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys()))

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：

class LastUpdatedOrderedDict(OrderedDict):
	
	def __init__(self, capacity):
		super(LastUpdatedOrderedDict, self).__init__()
		self._capacity = capacity

	def __setitem__(self, key, value):
		containsKey = 1 if key in self else 0
		if len(self) - containsKey >= self._capacity:
			last = self.popitem(last=False)
			print('remove:', last)
		if containsKey:
			del self[key]
			print('set:', (key, value))
		else:
			print('add:', (key, value))
		OrderedDict.__setitem__(self, key, value)

# Counter
print('----- Counter -----')
# Counter是一个简单的计数器，
# 例如，统计字符出现的个数：
from collections import Counter
c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1

print(c)



