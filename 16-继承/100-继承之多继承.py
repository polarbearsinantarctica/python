#-*- coding: utf-8 -*-
# @Time    : 2020/5/5 2:12
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 100-继承之多继承.py
class A(object):
    def __init__(self):
        self.kongfua = 'A父方法'
    def make_cakea(self):
        print(f'运用{self.kongfua}')
class B(object):
    def __init__(self):
        self.kongfub = 'B父方法'
    def make_cakeb(self):
        print(f'运用{self.kongfub}')
class C(A,B): #以子类出发，继承多个是多继承  (两个父类函数和属性同名的情况下)默认使用第一个父类的属性和方法,其余不同名的属性和函数属于完全继承
    pass

c=C()
# c.make_cakea()
c.make_cakeb()