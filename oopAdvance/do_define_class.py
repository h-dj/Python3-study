#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 定制类 '

__author__ = 'H_DJ'

'''
__xxx__这样的变量可以用来定制类
__slots__ ： 变量可以限制类添加变量
__len__()： 方法我们也知道是为了能让class作用于len()函数。
更多可定制的方法，请参考Python的官方文档。
https://docs.python.org/3/reference/datamodel.html#special-method-names
'''


# __str__ 类似java中的toString()方法
class Student(object):
    def __init__(self, name):
        self.name = name

    # 用于规范打印类实例信息
    def __str__(self):
        return 'Student object (name: %s)' % self.name


print(Student('lisi'))


# __iter__ 定义一个类变为可迭代对象，可被用于for ... in循环

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

    #
    def __getitem__(self, n):
        # 如果n是数字，则直接取出下标对应的值
        if (isinstance(n, int)):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a

        if isinstance(n, slice):  # n是切片
            start = n.start  # 切片的开始位置
            stop = n.stop  # 切片的末位置
            step = n.step  # 切片的跨度
            if start is None:
                start = 0
            if step is None:
                step = 1
            a, b = 1, 1
            L = []
            for x in range(start, stop, step):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


for i in Fib():
    print(i)

# __getitem__ ： 用于一个类实例使用 []语法
f = Fib()
print('第3个数', f[2])

# 实现切片方法：
L = f[:10:2]
print('取出数列前十个：', L)
for x in range(1, 10, 2):
    print(x)
