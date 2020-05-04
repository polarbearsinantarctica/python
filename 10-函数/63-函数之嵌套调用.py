#-*- coding: utf-8 -*-
# @Time    : 2020/5/3 18:25
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 63-函数之嵌套调用.py

def testB():
    print('-'*10+'testB start'+'-'*10)
    print('testB函数执行体')
    print('-' * 10 + 'testB end' + '-' * 10)
def testA():
    print('-'*10+'testA start'+'-'*10)
    testB()
    print('-' * 10 + 'testA end' + '-' * 10)
testA()