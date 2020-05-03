#-*- coding: utf-8 -*-
# @Time    : 2020/5/1 3:47
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 36-列表之修改.py
name_list = ['TOM','Lily','ROSE']
#1.
name_list[0] = 'aaa'
print(name_list)
#2.reverse
list = [1,5,9,8,6,4]
list.reverse()
print(list)
#3.sort
list.sort()
print(list)
list.sort(reverse=True)
print(list)
