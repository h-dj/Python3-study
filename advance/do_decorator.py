# -*- coding: utf-8 -*-

'''
装饰器
    在面向对象（OOP）的设计模式中，decorator被称为装饰模式。
    OOP的装饰模式需要通过继承和组合来实现，
    而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。
    Python的decorator可以用函数实现，也可以用类实现。
'''

# 例子：
# 定义一个装饰器；用来打印日记
import time


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


def now():
    print('2015-3-25')


# 自己调用装饰器;
now = log(now)
print(now.__name__)  # 现在的函数now.__name__为wrapper
now()


# 但是python有内置的装饰器语法糖 @
@log  # 相当于调用了 now = log(now)
def now():
    print('2015-3-25')


# 问题： 使用装饰器 会使原函数的元信息不见了，比如函数的docstring、__name__、参数列表等信息
# 解决： 在包装函数前加上内置装饰器@functools.wraps(func) 可以把原来的元信息复制到包装函数中
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2015-3-25')


print(now.__name__)  # 使用@functools.wraps(func)后，函数的now.__name__为now
now()


# 带参数的装饰器，只要再包一层函数来保存
def log(text):
    # 最外层函数来传递参数
    def decorator(fn):
        # 这里才装饰函数
        @functools.wraps(fn)
        def warpper(*args, **kwargs):
            print("call %s , log text : %s "  %(fn.__name__, text))
            fun = fn(*args, **kwargs)
            return fun

        return warpper

    # 检测对象text是否可被调用,
    # 如果没有调用text,则执行decorator函数返回warpper对象引用，否则返回decorator对象引用
    if callable(text):
        fn = text;
        text = ""
        return decorator(fn)
    else:
        return decorator


functools.partial(log, "")


@log
def now():
    print('2015-3-25')


print('函数的签名为： ', now.__name__)
now()


@log('测试')
def now():
    print('2015-3-25')


print('函数的签名为： ', now.__name__)
now()
# 练习：

'''
请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
'''


def metric(fn):
    @functools.wraps(fn)
    def warpper(*args, **kwargs):
        start_time = time.time()
        fun = fn(*args, **kwargs)
        end_time = time.time()
        print('%s executed in %s ms' % (fn.__name__, (end_time - start_time)))
        return fun

    return warpper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;


f = fast(11, 22)
s = slow(11, 22, 33)

print(f, s)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
