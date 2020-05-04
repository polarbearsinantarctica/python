#-*- coding: utf-8 -*-
# @Time    : 2020/5/3 18:16
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 62-函数之说明文档.py

# 内部 函数说明文档
help(len) #该函数可以查询函数的说名文档

# 自定义 函数说明文档
# 函数说明文档的列子
def info_test():
    """函数说明文档列子"""
    return ''

info_test()

help(info_test) # 放的是函数名

# 推荐做法
def sum_num1(a,b):
    """
    统计函数
    :param a:
    :param b:
    :return:
    """
    # """ 之后回车可以获取到当前函数的参数、返回值

help(sum_num1)