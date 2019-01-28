#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 多重继承学习'

__author__ = 'H_DJ'


# 1 . 多重继承的写法
class Father1(object):


    def method(self):
        print('father1 method')


class Father2(object):

    def method(self):
        print('Father2 method')


# 子类通过
class Children(Father1, Father2):
    pass


# 在多重继承中，如果多个父类有相同的方法定义，当子类执行该方法时；
# 会按继承的顺序Children(Father1, Father2): 来搜索该方法，找到就执行，然后就不管其他父类所定义的方法
c = Children()
c.method()

