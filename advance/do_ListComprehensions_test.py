# -*- coding: utf-8 -*-

# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [s.lower() for s in L1]

L2 = [s.lower() for s in L1 if (isinstance(s, str))]


# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
