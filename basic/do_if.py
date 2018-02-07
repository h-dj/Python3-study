# -*- coding: utf-8 -*-

'''
练习
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
'''

height=1.75
weight=80.5

bmi=weight/(height*height)
if bmi<18.5:
    print('过轻')
elif 18.5<bmi<25:
    print('正常')
else:
    print('肥胖')