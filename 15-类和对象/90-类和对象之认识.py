#-*- coding: utf-8 -*-
# @Time    : 2020/5/4 16:55
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 90-面向对象之认识.py

#1.类定义
class Washer(): #类名遵循驼峰
    def wash(self): #方法
        print(self) # self是调用该函数的对象(类似java的this)
        print('wash函数')
#2.类实例化
haier=Washer()
#3.调用对象
print(Washer)
print(haier)
haier.wash()