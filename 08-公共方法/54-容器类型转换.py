#-*- coding: utf-8 -*-
# @Time    : 2020/5/3 0:29
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 54-容器类型转换.py
list1 = [10,20,30,40,50]
s1 = {100,200,300,500}
t1 = ('a','b','c','d','e')

#tuple()
print(tuple(list1))
print(tuple(s1))

#list()
print(list(s1))
print(list(t1))

#set()
print(set(list1))
print(set(s1))