#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'H_DJ'

# 创建了一个hello模块
'''
#!/usr/bin/env python3  这注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，
# -*- coding: utf-8 -*-  注释表示.py文件本身使用标准UTF-8编码；

' a test module ' 表示模块的文档注释

__author__ = 'H_DJ'   __author__变量把作者写进去

'''


def test():
    arg = input()  # 系统输入参数
    if len(arg) == 1:
        print('hello world')
    elif len(arg) == 2:
        print('hello , %s' % (arg[0]))
    else:
        print('input to much argument')


if __name__ == '__main__':  # 定义了程序的入口
    test()
else:print(__name__)   # 在其他模块调用时 __name__变量为包名.模块名

