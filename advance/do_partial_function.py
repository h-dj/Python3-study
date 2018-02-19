# -*- coding: utf-8 -*-

# 偏函数
'''
functools.partial 就是帮助我们创建一个偏函数的

  def __init__(self, func, *args, **keywords):
  可知道partial 可以接收函数对象、*args和**kw这3个参数
'''
from functools import partial


def sqrt(x):
    return x * x

# functools.partial 可以可以更改参数的默认值，即使原先没有设置默认值
sqrt2 = partial(sqrt, x=2)
print(sqrt2())

