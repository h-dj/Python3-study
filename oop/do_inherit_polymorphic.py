#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'H_DJ'

'''
类继承和多态的学习

继承有什么好处？最大的好处是子类获得了父类的全部功能

'''


# 继承的写法
class Animate(object):
    _name = None  # 本类实例和子类可用
    __type = 'Animate'  # 只有在本类可用
    _food = None

    def __init__(self, _name, _food):
        super().__init__()
        self._name = _name
        self._food = _food

    def run(self):
        print('%s is running ' % self._name)


class Dog(Animate):

    def eat(self):
        print('%s like eat raw' % self._name)


class Cat(Animate):
    pass


# 这里定义一个工厂的类，用来喂养动物的
class FeedingFactory(object):

    # 在没有用多态时，每喂养一种动物，则需要定义特定的方法
    def feed_dog(self):
        print('dog feed raw')

    def feed_cat(self):
        print('cat feed fish')

    # 使用多态后，可以之定义一种喂养的方法，无论喂多少种动物都不需要更改此方法
    def feed(self, animate):
        print('%s feed %s' % (animate.__getattribute__('_name'), animate.__getattribute__('_food')))


factory = FeedingFactory()

dog = Dog('dog', 'raw')
cat = Cat('cat', 'fish')

factory.feed(dog)
factory.feed(cat)
