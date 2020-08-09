#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   searchDemo.py
@Time    :   2020/08/09 18:14:20
@Author  :   huang xu 
@Version :   1.0
@Contact :   1475559715@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   这是一个线性查找和二分查找的实现demo
'''

# here put the import lib

def liear_search(li,val):
    """
    线性查找,时间复杂度为O(n)
    """
    for i,v in enumerate(li):
        if v==val:
            return i 

def binary_search(li, val):
    """
    二分查找,时间复杂度为O(logn)
    """
    left = 0
    right = len(li)-1
    while left < right:
        mid=(left+right)//2     # 整除
        if mid==val:
            return mid
        elif val>mid:
            left=mid+1     # 候选区变为右半部分
        else : # val<mid
            right=mid-1     # 候选区变为左半部分
    return None

n=range(1000)        
print(f"线性查找的索引为{liear_search(n,346)}")
print(f"线性查找的索引为{binary_search(n,346)}")    

