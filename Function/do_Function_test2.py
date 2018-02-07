# -*- coding: utf-8 -*-

# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    print("跟踪 n=" + str(n) + " a=" + a + " b=" + b + " c=" + c)
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


# 可分解为三个步骤
'''
汉诺塔有A，B,C根柱子
A柱子上有n个盘子
1. 把A柱子上n-1的盘子(第n个盘子为最大的盘子)移到B柱子上
2. 在A柱子上的n-1个盘子都移到B柱子上后，剩余的一个最大的盘子移到C柱子上
3. 然后再把B上的盘子按照第一个步骤从B柱子移到C柱子
'''

move(4, "A", "B", "C")
