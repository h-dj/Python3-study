# -*- coding: utf-8 -*-

# 定义一个函数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 调用函数
print(my_abs(12))


# 默认参数
# 计算平方根
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(2))


# 可变参数
# 定义可变参数需要在参数前加*符号
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# 已经有一个list或者tuple，要调用一个可变参数
a = [1, 2, 3]
# 传入方法一，可以单独取出list或tuple中的元素传入
calc(a[0], a[1], a[2])
# 或者在变量前加符号*； *a表示把a这个list的所有元素作为可变参数传进去。
calc(*a)


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person("张三", 18, weight=40)

# 先组装好一个dict;当作关键字参数传入
extra = {'city': 'Beijing', 'job': 'Engineer'}
# 可以一个个单独传入
person('Jack', 24, city=extra['city'], job=extra['job'])
# 也可以使用**符号标志位关键参数传入； **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意
# kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
person('Jack', 24, **extra)


# 命名关键参数
# 命名关键字参数必须传入参数名
# 命名关键字参数可以有缺省值
# 1. 用于限制用户输入的关键参数
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person(name, age, *, city, job):
    print(name, age, city, job)

person("abc",20,city="123",job="123")

# 已经有了可变参数，那么后边的参数会被识别为命名关键参数；不需要再使用特殊分隔符*标识
def person(name, age, *args, city, job):
    print(name, age, city, job)
