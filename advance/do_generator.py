# -*- coding: utf-8 -*-

# 生成器generator
# 什么是生成器： 在Python中，这种一边循环一边计算的机制，称为生成器：generator。


# 创建一个generator
# 1. 只要把一个列表生成式的[]改成()， 就创建了一个generator：
g = (x * x for x in range(10))
print(type(g))
'''
g类型为 <class 'generator'>
'''


# 2. 使用函数方式创建generator
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


o = odd()
print(next(o))
print(next(o))

# 执行顺序
'''
函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
'''

# 打印出generator的每一个元素---使用next()函数或迭代
g = (x for x in range(10))
# 使用next()
print("使用next()")
print(next(g))

# 迭代
print("使用迭代")
for n in g:
    print(n)

# 用while循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value(这里不懂！！)
g = (x for x in range(10))
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
