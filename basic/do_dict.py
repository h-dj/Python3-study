# -*- coding: utf-8 -*-
# 字典练习

personInfo = {'name': '李四', 'age': 20, "height": 172}

# 获取字典中的某个key对应的值
#1. 直接使用key获取
print(personInfo['name'])
#2. 使用内置函数get()
print(personInfo.get('name'))
#3. 使用内置函数get(), 如果key不存在，可以返回None，或者自己指定的value：
print(personInfo.get('12',12))

# 更换某个key对应的值
personInfo['age'] = 25

# 添加新的key-value;
personInfo['weight'] = 55
print(personInfo)

#删除字典中的key
personInfo.pop('name')