#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
from typing import Any

__author__ = 'H_DJ'

'''
 类的定义有关键字class定义
 所有定义的类会自动继承于Object这个类
 
 __name两个下划线为private成员变量，只能本类使用，_name一个下划线为protected成员变量，可以在本类和子类中使用。
 
 
 实例属性 ：实例属性只能本实例能访问
 类属性 ：该类的全部实例都能访问
 
'''


# 下面定义一个学生的类
class Student(object):
    profession = 'Student'  # 定义一个公开变量，职业； 所有的实例都可以访问
    __name = None  # 私有变量, 外界不可直接访问
    __age = None

    '__init__ 初始化方法， 当有定义有__init__方法时，创建类实例时会自动反射获取该方法进行初始化'

    def __init__(self, name, age):
        self._name = name  # name、age变量只对创建的类的实例可用
        self._age = age
        print("init class", self._age)

    # 定义一个看书的方法
    def read_book(self, book_name):
        print('%s 正在看的书是 : %s' % (self._name, book_name))

    '''定义一个静态方法'''

    @staticmethod
    def static_method():
        print('this is a static method ')

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age


s = Student('abc', 20)
s.read_book('python ')
print(s.get_name(), s.get_age())
print(s._name)
