# -*- coding: utf-8 -*-

# 测试递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(5))


# 解决递归调用栈溢出的方法是通过尾递归优化; 主要是要把每一步的乘积传入到递归函数中：
def fact_iter(num, product=1):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact_iter(100))
