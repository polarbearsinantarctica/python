#-*- coding: utf-8 -*-
# @Time    : 2020/5/2 22:57
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 46-字典之查找.py
dict1={'name': 'Tom','age':20,'gender': '男'}

#1.[key] 存在返回值，不存在报错
print(dict1['name'])
#2.get() 查找，不存在返回默认值
print(dict1.get('name',0))
print(dict1.get('names'))
#3.keys() 返回结果是列表
print(dict1.keys())

#4.values() 返回结果是列表
print(dict1.values())
#5.items() 返回结果是列表
print(dict1.items())