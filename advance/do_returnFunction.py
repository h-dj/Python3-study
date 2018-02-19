# -*- coding: utf-8 -*-

# 1. 把函数作为返回值
# 如懒加载进行求和
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


sum = lazy_sum(*[1, 2, 3])
# sum 的类型为函数
print(type(sum))
# 调用sum才完成求和
print(sum())

# 2. 闭包（Closure）：是引用了自由变量的函数。
# 3. 注意： 返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 4. 练习：
'''
利用闭包返回一个计数器函数，每次调用它返回递增整数：

python引用变量的顺序： 当前作用域局部变量->外层作用域变量>当前模块中的全局变量->python内置变量
python 对外层作用域变量只能读不能修改

nonlocal关键字用来在函数或其他作用域中修改外层(非全局)变量
global关键字则是用于修改为全局变量
'''


def createCounter():
    count = 0

    def counter():
        nonlocal count
        count = count + 1
        print(id(count))
        return count

    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
list_ = [counterB(), counterB(), counterB(), counterB()]
print(list_)
if list_ == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
