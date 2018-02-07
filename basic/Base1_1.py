# -*- coding: utf-8 -*-

# name = input();
# print(name);

# ''' '''  用来打印多行字符串
print("""
fdsafd
fdsa
fdsa
fdsa

""")

# 字符串编码

b = "A"
# 对应A对应编码
print(ord(b));

# 字母A的编码是65,使用chr(65)通过编码号来找对应字符
print(chr(65))

# 如果bytes中包含无法解码的字节，decode()方法会报错：
c = b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
print(c)

print(len('中国'.encode('utf-8')))

# 字符串格式化
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# 转义%字符
d = 'growth rate: %d %%' % 7
print(d)

# 使用format()函数格式化
a = 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
print(a)

# 练习格式化
s1 = 72
s2 = 85
r = 100 * s1 / s2
print("小明成绩提升的百分点 为%.1f %%" % r);

# list学习

# 定义一个list变量
PrograminganguageLs = ['java', 'python', 'c语言']

print("列表中的个数：")
print(len(PrograminganguageLs))

# 获取list中单个值
print(PrograminganguageLs[0])

# 使用函数append()添加值到列表末尾
PrograminganguageLs.append('javascript')
print(PrograminganguageLs)

# 元素插入到指定的位置，使用函数insert()
PrograminganguageLs.insert(2, 'c++')
print(PrograminganguageLs)

# 要删除list末尾的元素，用pop()方法：
a = PrograminganguageLs.pop()
print(a)
print(PrograminganguageLs)
# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
a1 = PrograminganguageLs.pop(2)
print(a1)
print(PrograminganguageLs)

PrograminganguageLs[1] = 'Hello'
print(PrograminganguageLs)

# 列表中的类型；可以为不同的类型
L = ['Apple', 123, True]
print(L)
L2 = ['Apple', 123, True, [1, 2, 3]]
print(L2)
