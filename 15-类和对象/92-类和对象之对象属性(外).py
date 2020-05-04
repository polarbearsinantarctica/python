#-*- coding: utf-8 -*-
# @Time    : 2020/5/4 17:15
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 92-面向对象之对象属性(外).py

#对象属性 既可以在类外面添加和获取，也可以在类里面添加和获取 (动态语言特点。java和其不同，java是静态语言)
#1.对象属性在外操作
class Washer(): #类名遵循驼峰
    def wash(self): #方法
        print(self) # self是调用该函数的对象(类似java的this)
        print('wash函数')

haier1=Washer()
print('-'*10+'对象属性添加之前'+'-'*10)
haier1.wash()
haier1.width=500 # 添加属性
haier1.height=600
print('-'*10+'对象属性添加之后'+'-'*10)
haier1.wash()
print(haier1.width) # 获取属性