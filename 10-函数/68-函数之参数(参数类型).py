#-*- coding: utf-8 -*-
# @Time    : 2020/5/3 19:24
# @Author  : polarbear
# @Email   : 3196355931@qq.com
# @File    : 68-函数之参数(参数类型).py

#1.位置参数
def user_info1(name,age,gender):
    print(f'您的名字是{name},年龄是{age},性别是{gender}')
user_info1('小明',32,'男') #参数位置不能乱、个数不能少

#2.关键字参数 无key的必须写在最前面,且只能有一个

user_info1('Rose',age=20,gender='女')
user_info1('小明',gender='女',age=20)

#3.缺省参数 某些参数赋默认值
def user_info3(name,age,gender='男'):
    print(f'您的名字是{name},年龄是{age},性别是{gender}')

user_info3('Tom',20)
user_info3('Rose',18,'女')

# 4.不定长参数(可变参数) 传入不确定个数的参数

def user_info4(*args): #包裹位置参数传递
    print(args)
user_info4('Tom') # 元组
user_info4('TOM',18)

def user_info5(**args): #包裹关键字参数传递
    print(args)

user_info5(name = 'Tom',age=20) # 字典 必须有关键字