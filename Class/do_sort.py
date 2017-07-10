# sorted()函数就可以对list进行排序：
print(sorted([35,26,34,23,14]))

# sorted()函数也是一个高阶函数，
# 它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print(sorted([34,23,45,67,-65,19], key = abs))

# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。

# 字符串排序
print(sorted(['bob', 'about', 'Zoo', 'Credit']))

# 输出结果
# ['Credit', 'Zoo', 'about', 'bob']

# 默认情况下，对字符串排序，是按照ASCII的大小比较的


# 忽略大小写进行排序：
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

# 反向排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

'''
假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

请用sorted()对上述列表分别按名字排序：

'''
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
	return t[0]

def by_score(t):
	return t[1]

print('--------------- 按名称排序 --------------')
L2 = sorted(L, key=by_name)
print(L2)


print('--------------- 按成绩降序排序 --------------')
L3 = sorted(L, key=by_score, reverse=True)
print(L3)







