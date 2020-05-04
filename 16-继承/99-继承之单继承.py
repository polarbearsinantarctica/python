#-*- coding: utf-8 -*-
# @Time    : 2020/5/5 2:07
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 99-继承之单继承.py
class Master(object):
    def __init__(self):
        self.kongfu = '父方法'
    def make_cake(self):
        print(f'运用{self.kongfu}')
class Prentice(Master): #以子类出发，只继承一个父类叫单继承
    pass
dafu=Prentice()
print(dafu.kongfu)
dafu.make_cake()