#-*- coding: utf-8 -*-
# @Time    : 2020/5/3 0:05
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 53-方法.py
str1 = 'aqMeweqzweqw'
list1 = [10,20,30,40,40,50]
t1 = (10,20,30,40,40,50)
s1 = {10,20,30,40,40,50}
dict1 = {'name': 'TOM','age':18}

print('-'*10+'len()'+'-'*10)
print(len(str1))
print(len(list1))
print(len(t1))
print(len(s1)) #集合长度是去重之后的长度
print(len(dict1))

print('-'*10+'del或del()'+'-'*10)
# del str1
# print(str1)
# del (list1)
# # print(list1)
# del list1[0]
# print(list1)
# del(s1)
# print(s1)
# del dict1['name']
# print(dict1)

print('-'*10+'max()或min()'+'-'*10)
print(max(str1))
print(min(str1))
print(max(list1))
print(min(list1))

print('-'*10+'范围range(start,end,step)'+'-'*10)
print(range(1,10)) #返回的是一个对象
for i in range(1,10,1): # 左闭右开函数
    print(i)
for i in range(1,10,2):
    print(i)
for i in range(10): # end参数 默认步长1
    print(i)

print('-'*10+'enumerate()'+'-'*10)
list2 = ['a','b','c','d','e','r']
for i in enumerate(list2):
    print(i) #元组 (原迭代数据对象的数据对应的下标,原迭代数据对象的数据)
for i in enumerate(list2,start=1):
    print(i) #元组 (原迭代数据对象的数据对应的下标,原迭代数据对象的数据)