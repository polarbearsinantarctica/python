#-*- coding: utf-8 -*-
# @Time    : 2020/4/25 18:51
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 18-break-continue.py
num = 1
while num <= 5:
    num += 1
    if num == 3:
        continue
        print('我是continue')
    print(num)
num1 = 1
print('------------------')
while num1 <= 5:
    num1 += 1
    if num1 == 3:
        print('我是break')
        break
    print(num1)