
# 字符串正则匹配
import re
result1 = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(result1)


result2 = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print(result2)



# from urllib.request import urlopen

# for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
# 	line = line.decode('utf-8')
# 	if 'EST' in line or 'EDT' in line:
# 		print(line)

# 日期和时间
# dates are easily constructed and formatted
from datetime import date
now = date.today()

print(now)

# datetime.date(2003, 12, 2)
# now.strftime('%m-%d-%y. %d %b %Y is a %A on the %d day of %B')
# print(now)


# 数据压缩
import zlib
s = b'witch which has which witchaes wrist watch'
print(len(s))

t = zlib.compress(s)

print(len(t))

print(zlib.decompress(t))

print(zlib.crc32(s))

# 性能度量
print('------------- 性能度量 ------------')
from timeit import Timer

print(Timer('t = a; a = b; b = t', 'a = 1; b = 2').timeit())
print(Timer('a,b = b,a', 'a = 1; b = 2').timeit())

# 测试模块
print('------------- 测试模块 ------------')
def average(values):
	return sum(values) / len(values)

import doctest
doctest.testmod()


