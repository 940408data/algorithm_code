#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo.py
@Time    :   2020/08/09 18:14:20
@Author  :   huang xu 
@Version :   1.0
@Contact :   1475559715@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   这是一个汉诺塔问题的demo
'''

# here put the import lib

def hanoi(n,a,b,c):
    if n==1:
        print(f"moving from  {a} to {c}")
    if n>1:
        hanoi(n-1,a,c,b)
        print(f"moving from  {a} to {c}")
        hanoi(n-1,b,a,c)
    
# hanoi(3,"A","B","C")

while True:
    n=int(input("请输入汉诺塔的层数"))
    print(hanoi(n,"A","B","C"))
    if n==5:
        break

