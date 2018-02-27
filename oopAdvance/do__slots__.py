#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'H_DJ'


# 特殊的__slots__变量，来限制该class实例能添加的属性：
# python是动态语言，可以才类创造后任务绑定变量和函数
class Student(object):
    pass


# 为Studnet类绑定name属性, 通过实例绑定的变量或函数只能本实例能访问到
s = Student();

s.name = 'abc'
print(s.name)

s2 = Student()
# print(s2.name)  # 会抛出异常： AttributeError: 'Student' object has no attribute 'name'

# 为了让全部的实例能绑定变量或函数，可以通过类来绑定
Student.age = 12  # 有类Student创建的实例都有age属性绑定
s3 = Student()
print('the age of s3 is ', s3.age)


# 为了限制类任意绑定任何属性和方法； 可以使用特殊变量  __slots__
class Student2(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称, 除了属性name和age，不能绑定其他属性



s4 = Student2()
s4.name = 's4'
s4.age = 20


# s4.weight = 56   # 会抛出异常 AttributeError: 'Student2' object has no attribute 'weight'

# 注意：使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class Student3(Student2):
    pass


s6 = Student3()
s6.weight = 56
