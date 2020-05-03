#-*- coding: utf-8 -*-
# @Time    : 2020/4/25 21:37
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 21-for循环.py
str1 = 'qwert'
for i in str1:
    if i == 'e':
        print('遇到e不打印')
        continue
    print(i)