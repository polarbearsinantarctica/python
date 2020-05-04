#-*- coding: utf-8 -*-
# @Time    : 2020/5/3 19:44
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 69-函数之拆包和交换变量值.py
def return_num():
    return 1,2

res = return_num()
print(res)

# 元组拆包
res1,res2=return_num() # 变量不能多于返回的参数
print('-'*10+'元组拆包'+'-'*10)
print(res1)
print(res2)

#字典拆包
dict1={'name': 'Tom','age': 18}
a,b=dict1

print('-'*10+'字典拆包'+'-'*10)
print(a)
print(b)

print(dict1[a])
print(dict1[b])

#交换变量值
#1.
i=10
j=20
k=0
k=i
i=j
j=k

print('-'*10+'交换变量值1'+'-'*10)
print(i)
print(j)

#2.
m,n=1,2
m,n=n,m

print('-'*10+'交换变量值2'+'-'*10)
print(n)
print(m)