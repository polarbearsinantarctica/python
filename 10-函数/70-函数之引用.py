#-*- coding: utf-8 -*-
# @Time    : 2020/5/3 19:58
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 70-函数之引用.py

#不可变类型
a = 1
b = a

print(a)
print(b)
print(id(a))
print(id(b))

a = 2
print(a) # 赋值之后内存地址变化

#可变类型
list1=[1,2,3]
list2 = list1

print(id(list1))
print(id(list2))

list1.append(4)
print(id(list1))
print(id(list2)) # 赋值之后内存地址不变化