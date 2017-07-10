#!/usr/bin/python3

x = "a"
y = "b"

# 换行输出
print(x)
print(y)

print('------------------------------')

# 不换行输出
print(x, end = ' ')
print(y, end = ' ')


print()

# 导入 sys 模块
import sys
print('=================== Pyhton import mode =================')
print('命令行参数为:')
for i in sys.argv:
	print(i)
print('\npython 路径为', sys.path)

