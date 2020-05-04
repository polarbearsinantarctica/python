#-*- coding: utf-8 -*-
# @Time    : 2020/5/3 18:37
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 65-函数之全局变量.py

a = 100 #全局变量
def testA():
    print(a)

def testB():
    a = 200
    print(a)

def testC():
    global a #关键字修饰该变量，注明当前块中的a是100
    a = 200
    print(a)

testA()
testB()
testC()
print(a)