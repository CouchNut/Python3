print(type(123))
print(type('str'))
print(None)


print(type(abs))

# print(type(a))

# 判断一个对象是否是函数
import types
def fn():
	pass

print( type(fn)==types.FunctionType)
print( abs==types.BuiltinFunctionType)

print((type(lambda x:x)==types.LambdaType))

print(type((x for x in range(10))) == types.GeneratorType) 


class Animal(object):
	pass

class Dog(Animal):
	pass

class Husky(Dog):
	pass

	
class Cat(Animal):
	pass
		

a = Animal()
b = Dog()
c = Cat()
h = Husky()

print(isinstance(a, Animal))
print(isinstance(h, Dog))
print(isinstance(h, Animal))

print(isinstance([1,2,4], (list, tuple)))
print(isinstance((1,2,4), (list, tuple)))


print(dir('ABC'))

class MyDog(object):
	def __len__(self):
		return 100

dog = MyDog()
print(len(dog))
		

class MyObject(object):
	"""docstring for MyObject"""
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x

obj = MyObject()

# 有属性 ‘x’ 吗
print(hasattr(obj, 'x'))
print(obj.x)

# 设置一个属性'y'
setattr(obj, 'y', 19)
# 有属性‘y’吗
print(hasattr(obj, 'y'))
# 获取属性'y'
print(getattr(obj, 'y'))

# 获取属性'y'
print(obj.y)

# 如果获取不存在的属性，会抛出AttributeError的错误
# getattr(obj, 'z') # 获取属性'z'
'''
Traceback (most recent call last):
  File "get_type.py", line 84, in <module>
    getattr(obj, 'z') # 获取属性'z'
AttributeError: 'MyObject' object has no attribute 'z'
'''

# 可以传入一个default参数，如果属性不存在，就返回默认值
print(getattr(obj, 'z', 404))

# 获取对象的方法

# 有属性 power 吗
print(hasattr(obj, 'power'))

# 获取属性 prowe
print(getattr(obj, 'power'))
# <bound method MyObject.power of <__main__.MyObject object at 0x10799b048>>

fn = getattr(obj, 'power')
print(fn)

# 调用fn() 与调用obj.power() 是一样的
print(fn())





