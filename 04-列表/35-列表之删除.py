#-*- coding: utf-8 -*-
# @Time    : 2020/5/1 3:39
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 35-列表之删除.py
name_list = ['TOM','Lily','ROSE']

#1.del 可以删除整个列表，也可以删除指定元素
del name_list[0]
print(name_list)
#2.pop 删除指定下标的数据，不指定则删除最后一个元素，返回值是被删除的元素
pop_name = name_list.pop()
print(pop_name)
print(name_list)
#3.remove
name_list.remove('Lily')
print(name_list)
#4.clear 清空
name_list.clear()
print(name_list)