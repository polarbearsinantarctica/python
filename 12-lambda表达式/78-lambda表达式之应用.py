#-*- coding: utf-8 -*-
# @Time    : 2020/5/4 1:54
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 78-lambda表达式之应用.py
#带判断的lambda
fn1=lambda a,b: a if a > b else b
print(fn1(100,200))
#列表排序
list1=[{'name': 'TOM','age': 20},
       {'name': 'ROSE','age': 18},
       {'name': 'Jack','age': 19}]
list1.sort(key=lambda x:x['name'])
print(list1)
list1.sort(key=lambda x:x['name'],reverse=True)
print(list1)
