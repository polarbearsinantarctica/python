#-*- coding: utf-8 -*-
# @Time    : 2020/4/25 22:37
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 26-切片.py
str1 = 'qwertyu'
print(str1)

print(str1[1:5:2]) # 左闭: 右开: 步长
print(str1[:5])
print(str1[-4:-1]) # 数轴负数思维 负数步长是从右向左 选取方向和步长方向相反，则无法选取