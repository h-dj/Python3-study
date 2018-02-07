# -*- coding: utf-8 -*-

# 列表生成式

# 1. 形式[ x for x in list]

# 生成1-9的列表
list_ = [x for x in list(range(1, 10))]
print(list_)

# for前的x为得出的结果, 可以进行操作
# 结果的平方
list_2 = [x * x for x in list(range(1, 10))]
print(list_2)

# for循环后可添加条件
# 1-9列表中，筛选出偶数
list_3 = [x for x in list(range(1, 10)) if (x % 2 == 0)]
print(list_3)

# 也可以有多层for循环
# 两层for循环实现打印乘法口诀表
list_4 = [str(n) + " * " + str(m) + "=" + str(n * m) for n in list(range(1, 10)) for m in list(range(1, 10))]
print(list_4)
