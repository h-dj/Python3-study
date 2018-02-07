# -*- coding: utf-8 -*-
# 计算两个数的乘积

def product(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("bad operand type")
    return x * y


print(product(1, 2))


# 默认参数
def product(x, y=1):
    return x * y


print('''======================================''')


# 加上可变参数
# 默认参数
def product(x, *args):
    num = 1 * x;
    for n in args:
        num = num * n;
    return num;


# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
