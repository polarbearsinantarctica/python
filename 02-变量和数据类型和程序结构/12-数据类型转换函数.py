#-*- coding: utf-8 -*-
# @Time    : 2020/4/25 0:47
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 12-数据类型转换函数.py
num=1
str1='10'
print(type(float(num)))
print(float(num))

print(type(float(str1)))
print(float(str1))

print(type(str(num)))
print(str(num))

list1=[10,20,30]
print(type(list1))

t1=(100,200,300)
print(list(t1))

str2='1'
str3='1.1'
str4='[10,20,30]'
str5='(100,200,300)'
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))