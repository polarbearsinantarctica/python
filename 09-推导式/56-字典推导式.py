#-*- coding: utf-8 -*-
# @Time    : 2020/5/3 1:36
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 56-字典推导式.py
dict1 = {}
print(type(dict1))
list1 = []
for i in range(1,5):
    list1.append(i)
print(list1)
for i in list1:
    dict1[i] = i**2
print(dict1)

#推导式
dict1 = {}
dict1 = {i: i**2 for i in range(1,5)}
print(dict1)

#两个列表合并为一个字典
list3 = ['name','age','gender']
list4 = ['Tom',20,'man','llllll']

dict1 = {}
dict1 = {list3[i]: list4[i] for i in range(len(list3)) if i <=((len(list3)-1) if (len(list3)< len(list4)) else (len(list4)-1))} #两个列表长度要求一致
print(dict1)

#提取字典中目标数据
counts = {'MBP': 268,'HP': 125,'DELL': 201, 'Lenovo':199,'acer':99}
count1 = {key: value for key,value in counts.items() if value >= 200}
print(count1)