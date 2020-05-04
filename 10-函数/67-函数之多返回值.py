#-*- coding: utf-8 -*-
# @Time    : 2020/5/3 18:54
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 67-函数之多返回值.py

def return_num():
    # return 1,2
    # return [1,2]
    # return {1,2}
    return {0:1,1:2}

res = return_num()
print(res) # 元组类型