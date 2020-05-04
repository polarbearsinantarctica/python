#-*- coding: utf-8 -*-
# @Time    : 2020/5/4 1:17
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 77-lambda表达式之参数.py
#无参数
fn1=lambda :100
print(fn1())
#一个参数
fn2=lambda a:a
print(fn2('hello world'))
#默认参数
fn3=lambda a,b,c=100:a+b+c
print(fn3(10,20))
#可变参数
fn4=lambda *args: args
print(fn4(10,20,30))
#不定长可变参数
fn5=lambda **kwargs: kwargs
print(fn5(name='ddd',age=20))