#-*- coding: utf-8 -*-
# @Time    : 2020/5/5 2:31
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 101-继承之重写.py
class A(object):
    def __init__(self):
        self.kongfu = 'A父方法'
    def make_cakea(self):
        print(f'运用A父方法')
class B(object):
    def __init__(self):
        self.kongfu = 'B父方法'
    def make_cakeb(self):
        print(f'运用B父方法')
class C(A,B):
    def __init__(self): #重写之后将继承的父类的方法中的内容完全覆盖
        self.kongfu = 'C方法'
    def make_cakec(self):
        print(f'运用{self.kongfu}')
    # pass

c=C()
# c.make_cakea()
c.make_cakea()
c.make_cakeb()
c.make_cakec()

print(C.__mro__) # 得到继承层级继承关系