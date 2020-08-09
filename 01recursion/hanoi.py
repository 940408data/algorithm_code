# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 16:29:35 2020

@author: huangxu

这是一个汉诺塔问题的demo
"""

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

