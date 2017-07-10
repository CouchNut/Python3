#!/usr/local/bin/python3

# Filename: python_print.py

# 输出格式美化

s = 'Hello, Runoob'
print(str(s))

print(repr(s))

print(str(1/7))

x = 10 * 3.25
y = 200 * 200

s = 'x 的值为：' + repr(x) + ', y 的值为：' + repr(y) + '...'
print(s)

# repr() 函数可以转义字符串中的特殊字符
hello = 'hello, runoob\n'
hellos = repr(hello)
print(hellos)

# repr() 的参数可以是 python 的任何对象
print(repr((x, y, ('Google', 'Runoob'))))

# 两种方式输出一个平方与立方的表
for x in range(1,11):
	print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
	# 注意前一行 'end' 的使用
	print(repr(x*x*x).rjust(4))

for x in range(1,11):
	print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。
# 还有类似的方法, 如 ljust() 和 center()。 
# 这些方法并不会写任何东西, 它们仅仅返回新的字符串。
# 另一个方法 zfill(), 它会在数字的左边填充 0

print('12'.zfill(5))
print('-3.14'.zfill(7))

print('3.14159265359'.zfill(5))

# str.format() 的基本使用如下:
print('{}网址："{}!"'.format('菜鸟教程', 'www.runoob.com'))


# 括号及其里面的字符（称作格式化字段）将会被format() 中的参数替换
# 在括号中的数字用于指向传入对象在format() 中的位置，如下所示

print('{0} 和 {1}'.format('Google', 'Runoob'))
print('{1} 和 {0}'.format('Google', 'Runoob'))

# 如果在 formar() 中使用了关键字参数，那么他们的值会指向使用该名字的参数
print('{name}网址：{site}'.format(name='菜鸟教程', site="www.runoob.com"))

# 位置及关键字参数任意的结合
print('站点列表 {0}, {1}, 和 {other}.'.format('google', 'Runoob', other="TaoBao"))


# '!a'(使用ascii()), '!s'(使用str()) 和 '!r'(使用repr())可以用于在格式化某个值之前对其进行转化

import math
print('常量 PI 的值近似为：{}。'.format(math.pi))

print('常量 PI 的值近似为：{!r}。'.format(math.pi))

# 可选项 ':' 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 
# 下面的例子将 Pi 保留到小数点后三位：

print('常量 PI 的值近似为：{0:.3f}。'.format(math.pi))

# 在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。

table = {'Google' : 1, 'Runoob' : 2, 'Taobao' : 3}

for name, number in table.items():
	print('{0:10} ==> {1:10d}'.format(name, number))
# 如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
# 最简单的就是传入一个字典, 然后使用方括号 '[]' 来访问键值 :

print('Runoob : {0[Runoob]:d}; Google:{0[Google]:d}; Taobao:{0[Taobao]:d}'.format(table))


# 读取键盘输入
print('--------------- 读取键盘输入 ----------------')

str = input("请输入：")
print("你输入的内容是：", str)


# 读和写文件
print('--------------- 读和写文件 ----------------')
# 将字符串写入到文件 foo.txt 中：

# 打开一个文件
f = open("/tmp/foo.txt", "w")

f.write("Python 是一个非常好的语言。\n是的，的确非常好！！\n")

str = f.read()
print(str)

# 关闭打开的文件
f.close()


file = open("/tmp/wifi-07-01-2017__20:22:37.log", "r")

str = file.read()
print(str)

file.close()
