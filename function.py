#!/usr/bin/python3

def hello():
	print("Hello world!")

hello()

# 计算面积函数
def area(width, height):
	return width * height


def print_welcome(name):
	print("Welcome", name)

print_welcome("Copper")

w = 4
h = 5
print('Width = ', w, "Height = ", h, "area = ", area(w,h))


# 定义函数
def printme(str):
	"打印任何传入的字符串"
	print(str)
	return

# 调用函数
printme("我要调用用户自定义函数")
printme("再次调用同一函数")


# 参数传递
a = [1, 2, 3]
a = "runoob"


# python 传不可变对象实例

def changeInt(a):	
	a = 10

b = 2
changeInt(b)
print(b)		# 2

# 传可变对象实例

def changeme(myList):
	"修改传入的列表"
	myList.append([1, 2, 3, 4]);
	print("函数内取值：", myList)
	return

mylist = [10, 20, 30]
changeme(mylist)

print("函数外取值: ", mylist)


# 必需参数

def printmy(str):
	"打印任何传入的字符串"
	print(str)
	return

printmy('sfsdf')

# 关键字参数

def printme3(str):
	"打印任何传入的字符串"
	print(str)
	return

printme3(str = "菜鸟")

# 以下实例中演示了函数参数的使用不需要使用指定顺序：
def printInfo(name, age):	
	"打印任何传入的字符串"
	print("名字：", name)
	print("年龄：", age)
	return

printInfo(age = 50, name = "runoob")


# 默认参数
def printinfo(name, age = 30):
	"打印任何传入的字符串"
	print("名字：", name)
	print("年龄：", age)
	return

printinfo(age = 50, name="copper")
print('-----------------------')
printinfo(name = 'Copper')
print('-----------------------')

# 不定长参数
def functionname(arg1, *vartuple):
	"打印任何传入的字符串"
	print("输出：")
	print(arg1)
	for var in vartuple:
		print(var)
	return

functionname(10)
print('-----------------------')
functionname(70, 60, 50)


# 匿名函数
sum = lambda arg1, arg2: arg1 + arg2

print("相加后的值为：", sum(10, 20))
print("相加后的值为：", sum(20, 20))


# 变量作用域

'''
Python的作用域一共有4中，分别是：
	L （Local） 		局部作用域
	E （Enclosing） 	闭包函数外的函数中
	G （Global） 	全局作用域
	B （Built-in） 	内建作用域
'''

x = int(2.9) 	# 内建作用域

g_count = 0		# 全局作用域

def outer():
	o_count = 1	# 闭包函数外的函数中
	def inner():
		i_count = 2	# 局部作用域

'''
Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
也就是说这这些语句内定义的变量，外部也可以访问
'''

if True:
	mas = "copper"

print(mas)

# 全局变量和局部变量
total = 0 # 这是一个全局变量
def sum(arg1, arg2):
	# 返回两个参数的和
	total = arg1 + arg2		# total在这里是局部变量
	print("函数内是局部变量：", total)
	return total

sum(10, 20)
print("函数外是全局变量：", total)

# global 和 nonlocal关键字
# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。

# 修改全局变量
num = 1
def fun1():
	global num # 需要使用 global 关键字声明
	print(num)
	num = 123
	print(num)

fun1()
print(num)


print('-----------------------')

# 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量
# 则需要 nonlocal 关键字了，如下实例：

def outer():
	num = 10
	def inner():
		nonlocal num
		num = 100
		print(num)
	inner()
	print(num)

outer()




