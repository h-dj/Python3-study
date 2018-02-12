# -*- coding: utf-8 -*-

# 高阶函数

# 1. map()和reduce()
# map ; map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
# map接受的函数只能有一个参数
from functools import reduce


def fn(x):
    return x * x


def power(list_):
    return list(map(fn, list_))


print(power([1, 4, 5, 6]))


# reduce() :reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

from functools import reduce


def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))

# pratice
# 1. str2int 字符串转int
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(str_):
    def char2int(s):
        return DIGITS[s]

    def fn(x, y):
        return x * 10 + y

    # 使用lambda    lambda x, y: x * 10 + y
    return reduce(lambda x, y: x * 10 + y, map(char2int, str_))


print(str2int("123456"))


# 2. 把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    return str(name[:1]).upper() + str(name[1:]).lower()


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# 3. Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    def fn(x, y):
        return x * y

    return reduce(fn, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 4. 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


# 实现1 分步处理
def str2float(s):
    spotIndex = str(s).find('.')

    def char2num(c):
        return DIGITS[c]

    def fn_(x, y):
        return x * 10 + y

    def _fn(x, y):
        return x / 10 + y

    def prePart():
        s_ = reduce(fn_, map(char2num, s[:spotIndex]))
        print(s_)
        return s_

    def lastPart():
        s_ = reduce(_fn, map(char2num, s[:spotIndex:-1]))
        print(s_)
        return s_ / 10

    return prePart() + lastPart()


# 实现2 ： 全部变为数字再除，

def str2float_(s):
    spotIndex = str(s).find('.')
    temp = s[:spotIndex] + s[spotIndex + 1:]

    def char2num(c):
        return DIGITS[c]

    def fn_(x, y):
        return x * 10 + y

    def get_num(s_):
        return reduce(fn_, map(char2num, s_))

    return get_num(temp) / pow(10, str(s[::-1]).find("."))


print('str2float(\'123.456\') =', str2float_('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
