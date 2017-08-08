#!/usr/local/bin python3



# 使用 metaclass 动态的为自定义的 MyList增加一个add方法

# meatclass是类的模板，所以必须从 ‘type’ 类型派生
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):	
		attrs['add'] = lambda self, value : self.append(value)
		return type.__new__(cls, name, bases, attrs)
		

class MyList(list, metaclass = ListMetaclass):
	pass


L = MyList()

L.add(1)

print(L)


# 普通的list没有add() 方法
L2 = list()

# l2.add(1)
'''
Traceback (most recent call last):
  File "use_metaclass.py", line 28, in <module>
    l2.add(1)
NameError: name 'l2' is not defined
'''












































































