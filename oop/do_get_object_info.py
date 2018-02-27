#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'H_DJ'

'''
获取对象的信息


'''
# type() 返回对象的类型
a = 'abcc'
print(type(a))

# isinstance() 也是判断变量的类型
# 判断a变量是否时str或int类型
print(isinstance(a, (str, int)))

# dir() 获得一个对象的所有属性和方法，
print(dir(a))

# len() 获取对象的长度
print(len(a))


# 自定义对象返回长度的方法; 注意__xxx__这样的变量或函数在Python中都是有特殊用途的
class MyDog(object):
    # 以下的方法是在对象使用len()方法是返回对象的长度为100
    def __len__(self):
        return 100


print(len(MyDog()))  # 结果为100


# getattr()、setattr()以及hasattr() 获取属性、设置属性和判断是否有该属性的方法
class Test(object):
    _name = 'test'

    def test(self):
        print('test function')


t = Test()
# 判断类Test是否有_name属性
print('class Test has _name attr ', hasattr(t, '_name'))

# 设置类Test的属性_name
setattr(t, '_name', 'test132465')
# 打印类Test的属性_name
print(getattr(t, '_name'))
