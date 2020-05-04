#-*- coding: utf-8 -*-
# @Time    : 2020/5/4 19:18
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 98-继承之认识.py
class A(object):
    def __init__(self):
        self.num=1
    def info(self):
        print(self.num )
class B(A): #()中为继承的类的类名，默认是object,子类默认继承父类的多有属性和方法
    pass

res=B()
res.info()