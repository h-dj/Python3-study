# -*- coding: utf-8 -*-

# 迭代


# list的迭代, 打印元素
list_ = [1, 2, 3, 4, 5]
for i in list_:
    print(i)

# 字典迭代
dict_ = {'name': 'a1', 'age': 10, 'weight': 55}
# 字典默认迭代键
for key in dict_:
    print(key)

# 迭代字典的值
for value in dict_.values():
    print(value)

# 键值一起迭代
for key, value in dict_.items():
    print("key=" + key + " value=" + str(value))

# 元组的迭代
tuple_ = (1, 2, 'v')
for t in tuple_:
    print(t)

# 字符串
str_ = "ABCD"
for s in str_:
    print(s)

# 通过collections模块的Iterable类型判断一个对象是可迭代对象;
from collections import Iterable

if (isinstance("abc", Iterable)):
    print("str 可迭代")
if (isinstance([1, 2, 3], Iterable)):
    print("list 可迭代")
if (isinstance({'name': 'a1', 'age': 10, 'weight': 55}, Iterable)):
    print("dict 可迭代")
if (isinstance(('a', 'b', 'c'), Iterable)):
    print("tuple 可迭代")
if (isinstance(123, Iterable)):
    print("int 可迭代")

# Python内置的enumerate函数可以把一个list变成索引-元素对,从而实现java下标迭代

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
