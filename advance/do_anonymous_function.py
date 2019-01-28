# -*- coding: utf-8 -*-

'''
lambda x: x * x
关键字lambda表示匿名函数，冒号前面的x表示函数参数。
匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

'''
import numpy as n

# 练习：


def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))
# 改造为匿名函数
L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)
