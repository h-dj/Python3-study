# -*- coding: utf-8 -*-

# 排序函数 sorted
'''
函数定义： sorted(iterable, *, key=None, reverse=False)
第一个参数iterable 可迭代的对象
* 后面为key/value参数对
第二个参数 key定义排序的函数
第三个参数为 reverse 是否把序列反转
'''

# 1. 调用排序
# 对list进行排序
list_ = [1, 42, 0, 9, 4, 3, 82]
print(sorted(list_))

# 只要是 iterable 可迭代的对象就可调用sorted进行排序
# 如dict, 但默认只对key排序
dict_ = {"a": 1, "b": 3, "c": 1}
print(sorted(dict_))

# 2. 自定义排序的key函数

'''
这个key关键字参数的值应该是一个接收单一参数的函数，并且该函数返回一个关键字用来比较排序
'''
list_ = ['a', 'Z', 'b', 'C']
#  按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。但忽略大小进行比较
print(sorted(list_, key=str.lower))


# 输出结果 ['a', 'b', 'C', 'Z']

# 变为负数
def negative(s):
    # 变负数的方法
    # s = ~s + 1
    s = -s
    return s


nums = [1, 5, 3, 7, 2]
print("变为负数再比较 结果为：", sorted(nums, key=negative))
# [7, 5, 3, 2, 1]


# 3. 可以在排序后反转序列
new_list = sorted(list_, key=str.lower, reverse=True)
print(new_list)
# 输出结果 ['Z', 'C', 'b', 'a']


# 练习

'''
假设我们用一组tuple表示学生名字和成绩：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
请用sorted()对上述列表分别按名字排序：
'''
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


# 测试练习
L2 = sorted(L, key=by_name)
print(L2)


def by_score(t):
    return -t[1]


L2 = sorted(L, key=by_score)
print(L2)
