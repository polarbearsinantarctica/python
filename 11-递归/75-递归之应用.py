#-*- coding: utf-8 -*-
# @Time    : 2020/5/4 0:47
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 75-递归之应用.py
#1.函数内部自己调用自己 2.函数有出口
def sum_numbers(num):
    """递归调用"""
    if num == 1:
        return 1
    return  num + sum_numbers(num-1)

res = sum_numbers(10)
print(res)

#无出口可能要报最大递归深度错误
#递归深度根据计算机不同深度不同，不会出现死循环