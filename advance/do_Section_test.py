# -*- coding: utf-8 -*-
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：


def trim(s):
    if s[:1] != " " and s[-1:] != " ":  # 如果首尾都没有空格，则返回字符串
        return s
    elif s[:1] == " ":  # 如果前面有则把空格去掉，再递归检查
        return trim(s[1:])
    # elif s[-1:] == " ":
    else:  # 如果尾部有则把空格去掉，再递归检查
        return trim(s[:-1])


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
