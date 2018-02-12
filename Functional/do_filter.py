# -*- coding: utf-8 -*-

# filter : 过滤序列; filter()接收一个函数和一个序列, 然后根据返回值是True还是False决定保留还是丢弃该元素。
# 使用filter求素数
'''
# 素数： 质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数。
# 求素数的方法： 埃氏筛法
# 筛选步骤：
（1）先把1删除（现今数学界1既不是质数也不是合数）
（2）读取队列中当前最小的数2，然后把2的倍数删去
（3）读取队列中当前最小的数3，然后把3的倍数删去
（4）读取队列中当前最小的数5，然后把5的倍数删去
（5）如上所述直到需求的范围内所有的数均删除或读取
'''


# 实现算法
# 1. 构造一个生成器来生成奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 2. 过滤的函数
def _not_divisable(n_):
    return lambda x: x % n_ > 0


def _not_divisable_(n_):
    def fn(x):
        return x % n_ > 0

    return fn


# 3. 定义一个返回素数的生成器

def primes():
    # 先返回2素数
    yield 2
    it = _odd_iter()  # 初始化序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisable(n), it)  # 构造新序列


def main():
    # 打印1000以内的素数:
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break


if __name__ == '__main__':
    main()


# 练习： 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：

def is_palindrome(num):
    # 先把传入的数字转为字符串
    str_ = str(num)
    return str_ and str_ == (str_[::-1])


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
