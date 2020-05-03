#-*- coding: utf-8 -*-
# @Time    : 2020/5/2 23:48
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 52-运算符.py
# + *  in not in 字符串 列表 元组 字典(不支持 + * )
str1 = 'aa'
str2 = 'bb'
print('-'*20)
print(str1+str2)
print(str1*6)
print('a' in str1)
print('aaa' not in str1)

list1 = [1,2]
list2 = [10,20]
print('-'*20)
print(list1+list2)
print(list1*2)
print(1 in list1)
print('1' not in list1)

t1 = (1,2)
t2 = (10,20)
print('-'*20)
print(t1+t2)
print(t1*2)
print(1 in t1)
print('1' not in t1)

dict1={'name': 'Python'}
dict2={'age': 30}
print('-'*20)
# print(dict1+dict2)
# print(*dict1)
print('Python' in dict1) # 指定的数据是否存在  支持key为str
print('aaa' not in dict1)