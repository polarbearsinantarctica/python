#-*- coding: utf-8 -*-
# @Time    : 2020/5/5 2:50
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 102-继承之子父类同名同时使用.py
class A(object):
    def __init__(self):
        self.kongfu = 'A父方法'
    def make_cake(self):
        print(f'运用{self.kongfu}')
class B(object):
    def __init__(self):
        self.kongfu = 'B父方法'
    def make_cake(self):
        print(f'运用{self.kongfu}')
class C(A,B):
    def __init__(self): #重写之后将继承的父类的方法中的内容完全覆盖
        self.kongfu = 'C方法'
    def make_cake(self):
        self.__init__()# 必须初始化，避免属性污染
        print(f'运用{self.kongfu}')
    def make_cakea(self): #若想使用父类的同名属性和函数，需要重定义方法，重新初始化父类相关函数
        A.__init__(self)
        A.make_cake(self)
    def make_cakeb(self):
        B.__init__(self) #同名属性的情况下，需重新初始化，初始化之后才能调用父类的方法中的属性(视情况使用)
        B.make_cake(self)
    # pass

c=C()
c.make_cake()
c.make_cakea()
c.make_cakeb()
c.make_cake()
