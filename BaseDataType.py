#!/usr/bin/python3

counter = 100
miles = 1000.0
name = "runoob"

print(counter)
print(miles)
print(name)

# python 多个变量赋值
a = b = c = 1

print(a,b,c)

a, b, c = 1, 2, "runoob"

print("a =",a, "b =",b, "c =",c)

print("=============  Number 数字类型 ==============")

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

print("=============  instance 判断 ==============")

a = 111
print(isinstance(a, int))

# isinstance 和 type 的区别在于
class A(object):
	pass

class B(A):
	pass

print(isinstance(A(), A))	# True
print(type(A()) == A)		# True
print(isinstance(B(), A))	# True
print(type(B()) == A)		# False

# 区别就是 ：
# type() 不会认为子类是一种父类类型
# isinstance() 会认为子类是一种父类类型


#  使用 del 删除一些对象引用

var1 = 1
var2 = 10

del var1

print("=============  字符串操作 ==============")

# 字符串截取的语法是
# 变量[头下标:尾下标]  包括尾下标那个字符
# + 是字符串的连接符，星号(*)表示复制当前字符串，紧跟的数字为复制的次数
str = 'Runoob'

print(str)			# Runoob
print(str[0:-1])	# Runoo
print(str[0])		# R
print(str[2:5])		# noo  输出第三个到第五个之间的所有字符，包括第三个字符，包括第五个字符
print(str[2:])		# noob	输出第三个开始之后的所有字符
print(str * 2)		# RunoobRunoob 输出两边该字符串
print(str + 'Test') # RunoobTest  连接字符串

# 修改字符串
var1 = 'Hello World'
print("已更新字符串：" + var1[:6] + 'Runoob')

# Python字符串格式化输出
print('我叫 %s 今年 %d 岁' % ('Copper', 10))

print("=============  List(列表)操作 ==============")
# 列表截取的语法格式如下：
# 变量[头下标:尾下标]
list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)			# ['abcd', 786, 2.23, 'runoob', 70.2] 输出完整列表
print(list[0]) 		# abcd 输出第一个元素 
print(list[1:3])	# [786, 2.23] 从第二格元素开始输出直到第三个元素
print(list[2:])		# [2.23, 'runoob', 70.2] 输出从第三个元素开始到最后一个元素
print(tinylist * 2) # [123, 'runoob', 123, 'runoob'] 输出两次列表
print(list + tinylist) # ['abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob'] 链接列表

#  列表中的元素可改变
a = [1, 2, 3, 4, 5]
print(a) 			# [1, 2, 3, 4, 5]


a[0] = 2
print(a)			# [2, 2, 3, 4, 5]

a[3:] = []			
print(a)			# [2, 2, 3]

print("=============  Tuple(元组)操作 ==============")
# 元组写在 () 里，列表是写在 [] 里
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple) 		# ('abcd', 786, 2.23, 'runoob', 70.2)  整体输出
print(tuple[0])		# abcd  输出第一个元素
print(tuple[1:3])	# (786, 2.23) 第二个元素到第三个元素
print(tuple[2:])	# (2.23, 'runoob', 70.2) 输出第三个元素以及之后的所有元素
print(tinytuple * 2) # (123, 'runoob', 123, 'runoob') 输出两次元组
print(tuple + tinytuple) # ('abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob') 连接两个元组

tup1 = () # 空元组
tup2 = (20,) # 一个元素的元组，需要在后面添加逗号
# 注意事项：
# 元组元素不能修改


print("=============  Set(集合)操作 ==============")
# 创建一个空集合, 不能用 {}, {} 是用来创建空字典
set1 = set()
student = {'Tom', 'Jim', 'Mary', 'Jack', 'Rose'}
print(student)		# {'Rose', 'Jack', 'Mary', 'Tom', 'Jim'} 输出集合所有的元素

# 成员测试
if ('Rose' in student):
	print('Rose 在集合中')
else :
	print('Rose 不在集合中')

# set可以进行集合运算
b = set('asdfasdga')
c = set('sdfsadfasdfsdaf')

print(b)	# 集合中的元素只能有一个
print(c)
print(b - c) 	# {'g'}	 两个集合的差集
print(b | c) 	# {'s', 'd', 'f', 'a', 'g'} 两个集合的并集
print(b & c) 	# {'s', 'd', 'a', 'f'} 两个集合的交集
print(b ^ c) 	# {'g'} 两个集合中的不同时存在的元素

print("=============  Dictionary(字典)操作 ==============")
dict = {}  # 创建一个空字典
dict['one'] = "1 - 菜鸟教程"
dict[2]	 = "2 - 菜鸟工具"

tinyDict = {'name' : 'runoob', 'code' : 1, 'site': 'www.runoob.com'}

print(tinyDict)			# {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print(dict[2])			# 2 - 菜鸟工具 输出键为 ’2‘ 的值
print(dict.keys())		# dict_keys(['one', 2]) 输出这个字典的所有key值
print(dict.values())	# dict_values(['1 - 菜鸟教程', '2 - 菜鸟工具'])


def test(*args):
	print(args)
	return args

print(test(1, 2, 3, 4))






































