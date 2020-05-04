#-*- coding: utf-8 -*-
# @Time    : 2020/5/3 18:14
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 61-函数之return.py

#debug可以看清楚函数的执行过程
def buy():
    return '烟'
    print('酒')

product = buy()
print(product)