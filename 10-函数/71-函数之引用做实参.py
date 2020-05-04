#-*- coding: utf-8 -*-
# @Time    : 2020/5/3 21:13
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 71-函数之引用做实参.py
def test1(a):
    print(a)
    print(id(a))

    a+=a
    print(a)
    print(id(a))
# 不可变类型可以当做实参传入
b = 100
test1(b)
# 可变类型可以当做实参传入
c = [10,20]
test1(c)