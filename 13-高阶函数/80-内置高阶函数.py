#-*- coding: utf-8 -*-
# @Time    : 2020/5/4 2:14
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 80-内置高阶函数.py
#map(fuc,ll) 将传入的函数变量作用于变量的每一个数据，返回组成新的迭代器
list1=[1,2,3,4,5]
def func(x):
    return x**2
res=map(func,list1) #迭代器
print(res)
print(list(res))#类型强转
#reduce(func,ll) func必须要有两个参数 func计算的结果继续和序列的下一个元素做累积计算
import functools
list2=[1,2,3,4,5]
def func(a,b):
    return a+b
res2=functools.reduce(func,list2)
print(res2)
#filter(func,ll) 过滤掉不符合条件的元素，返回一个filter对象，可以强转为list
list3=[1,2,3,4,5,6,7,8,9,10]
def func(x):
    return x%2==0
res3=filter(func,list3) #过滤掉不符合传入的func规则的
print(res3)
print(list(res3))