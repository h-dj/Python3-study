# -*- coding: utf-8 -*-

# 迭代器

# 1. 定义：可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

# 2. 判断是否是迭代器： 使用函数 isinstance
from collections import Iterator

if (isinstance([], Iterator)):
    print("list is Iterator without iter()")

# 3. 转换为可迭代的对象，使用含函数iter()
if (isinstance(iter([]), Iterator)):
    print("list is Iterator with iter()")