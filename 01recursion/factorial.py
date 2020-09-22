#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   factorial.py
@Time    :   2020/08/09 18:14:20
@Author  :   huang xu 
@Version :   1.0
@Contact :   1475559715@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   这是一个阶乘的demo
'''

# here put the import lib
def ft(n):
    if n==1:
        return 1
    elif n>1:
        print(n)
        # return n*ft(n-1)
        ft(n-1)
        # print(n)
    else:
        print("非法的输入")
print(ft(6))