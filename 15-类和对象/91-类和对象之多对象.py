#-*- coding: utf-8 -*-
# @Time    : 2020/5/4 17:11
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 91-面向对象之多对象.py

class Washer(): #类名遵循驼峰
    def wash(self): #方法
        print(self) # self是调用该函数的对象(类似java的this)
        print('wash函数')

haier1=Washer()
print('-'*10+'第一个对象'+'-'*10)
haier1.wash()
print(haier1)
haier2=Washer()
print('-'*10+'第二个对象'+'-'*10)
haier2.wash()
print(haier2)