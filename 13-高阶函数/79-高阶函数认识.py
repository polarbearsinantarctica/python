#-*- coding: utf-8 -*-
# @Time    : 2020/5/4 2:01
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 79-高阶函数认识.py
#把函数作为参数传入 称为高阶函数
#abs 求绝对值
def add_num(a,b):
    return abs(a)+abs(b)
res=add_num(-10,-9)
print(res)
#round 四舍五入
print(round(1.22))
print(round(1.56))

#高阶函数 可以使用内置，也可以自定义
def abs_df(n):
    return abs(n)
def sum_num(a,b,f):
    return f(a)+f(b)
res1=sum_num(-1,2,abs_df)
print(res1)
res2=sum_num(1.1,1.2,round)
print(res2)
