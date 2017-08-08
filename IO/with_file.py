#!/usr/local/bin python3

# -*- coding: utf-8 -*-

f = open('/Users/apple/Desktop/Copper/Code/Python/test.txt', 'r')

# 如果打开一个不存在的文件，就会抛出错误
# f = open('/Users/apple/Desktop/Copper/Code/Python/notfound.txt', 'r')
'''
Traceback (most recent call last):
  File "with_file.py", line 8, in <module>
    f = open('/Users/apple/Desktop/Copper/Code/Python/notfound.txt', 'r')
FileNotFoundError: [Errno 2] No such file or directory: '/Users/apple/Desktop/Copper/Code/Python/notfound.txt'
'''
print(f.read())

f.close()

# 由于文件读写是都有可能产生IOError, 一旦出错，后面的 f.close() 就不会调用。
# 所以为了保证无论是否出错都能正确的关闭文件，可以使用 try ... finally 来实现
try:
	f2 = open('/Users/apple/Desktop/Copper/Code/Python/test.txt', 'r')
	print(f2.read())
finally:
	f2.close()
# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
print('----- 使用with打开文件 -----')
with open('/Users/apple/Desktop/Copper/Code/Python/test.txt', 'r') as f3:
	print(f3.read())
	for line in f3.readlines():
		print(line.strip())	# 把末尾的 '\n' 删掉

print('----- test.png -----')
f4 = open('/Users/apple/Desktop/Copper/Code/Python/test.png', 'rb')
print(f4.read())


print('----- 写文件 -----')

f5 = open('/Users/apple/Desktop/Copper/Code/Python/test.txt', 'w')
f5.write('Hello Copoper!')
f5.close()


with open('/Users/apple/Desktop/Copper/Code/Python/test.txt', 'w') as f6:
	f6.write('Hello!!!')






































