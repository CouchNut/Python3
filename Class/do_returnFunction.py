# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。


def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n

    return ax



def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

# 当我们调用lazy_sum() 时，返回的并不是求和结果，而是求和函数
f = lazy_sum(1, 3, 7, 5, 9)
print(f)
# 当调用函数 f 时，才真正计算求和的结果
print(f())

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
    
print(f1 == f2)     # false

# 闭包
def count():
    fs = []
    for i in range(1, 4):   
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())



# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# 如果一定要引用循环变量，方法是创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count1():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))     # f(i) 立刻被执行，因此i的当前值被传入f()
    return fs

f4, f5, f6 = count1()

print(f4())
print(f5())
print(f6())








































