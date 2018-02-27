#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'H_DJ'

'''
Python内置的@property装饰器就是负责把一个方法变成属性调用的：
注意：属性和方法名不要相同，否则后导致不断的调用自身而没有设终止条件而栈溢出
'''


class Student(object):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def score(self):
        return self.score

    '使用@property的好处是：可以在变量赋值时，对变量进行约束检查'
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.score = value


s = Student()
s.name = '123'
print(s.name)

s.score = 60  # OK，实际转化为s.set_score(60)
s.score  # OK，实际转化为s.get_score()
