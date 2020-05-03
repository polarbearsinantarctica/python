#-*- coding: utf-8 -*-
# @Time    : 2020/5/3 1:17
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 55-列表推导式.py

list1 = []
i = 0
while i<10:
    list1.append(i)
    i +=1
print(list1)

list1 = []
for i in range(0,10,1):
    list1.append(i)
print(list1)

#列表推导式
list1 = []
list1 = [i for  i in range(10)] #左i为要返回的数据
print(list1)
list2 = [i for  i in list1] #左i为要返回的数据
print(list2)

list1 = []
for i in range(10):
    if i%2 == 0:
        list1.append(i)
print(list1)

#带if的列表推导式
list1 = []
list1 = [i for  i in range(10) if i%2==0] #左i为要返回的数据
print(list1)

#多个for循环实现列表推导式
list1 = []
for i in range(1,3):
    for j in range(0,3):
        list1.append((i,j))
print(list1)

list1 = []
list1 = [(i,j) for i in range(1,3) for j in range(0,3)]
print(list1)

