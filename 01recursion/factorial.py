# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 16:29:35 2020

@author: huangxu

这是一个阶乘的demo
"""
def ft(n):
    if n>1:
        return n*ft(n-1)
    if n==1:
        return 1

print(ft(7))