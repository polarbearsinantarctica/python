#-*- coding: utf-8 -*-
# @Time    : 2020/5/4 1:04
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 76-lambda表达式之定义.py
#定义：lambda 参数列表: 表达式

#函数
def fn1():
    return 200
print(fn1)
print(fn1())
#lambda表达式 匿名函数
fn2=lambda: 100
print(fn2)
print(fn2())

#函数
def add(a,b):
    return a+b
res=add(1,2)
print(res)
#lambda表达式
fn3=lambda a,b:a+b
print(fn3(1,2)) #调用时，函数和lambda表达式传参方式相同