#-*- coding: utf-8 -*-
# @Time    : 2020/5/2 23:13
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 47-字典之循环.py
dict1={'name': 'Tom','age':20,'gender': '男'}

for key in dict1.keys():
    print(key)

for key in dict1.values():
    print(key)

for key in dict1.items():
    print(key)

for key ,value in dict1.items():
    print('%s=%s' %(key,value))