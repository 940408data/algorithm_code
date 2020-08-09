#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   bubble_sort.py
@Time    :   2020/08/09 19:46:48
@Author  :   huang xu 
@Version :   1.0
@Contact :   1475559715@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   这是冒泡排序的实现。
'''

# here put the import lib

def bubble_sort(li):
    for i in range(len(li)-1):   # 第i趟排序，总共要进行i-1趟
        for j in range(len(li)-i-1):  # 无序区为n-i个元素，指针只需要走到i-1的位置
            if li[j]>li[j+1]:  # 升序排序，if要降序，则li[j]<li[j+1]
                li[j],li[j+1]=li[j+1],li[j]  # 交换元素
        print(i,li)

def bubble_sort1(li):
    """
    针对已经部分有序的序列的进行优化
    比如 [8,6,9,7,1,2,3,4,5]
    如果在一趟里面已经排好序了，那么就不用再排序了。
    设置一个交换标记位置，如果这一趟没有交换，说明数组已经有序了，可以直接返回了。
    """
    for i in range(len(li)-1):   # 第i趟排序，总共要进行i-1趟
        exchange=False
        for j in range(len(li)-i-1):  # 无序区为n-i个元素，指针只需要走到i-1的位置
            if li[j]>li[j+1]:  # 升序排序，if要降序，则li[j]<li[j+1]
                li[j],li[j+1]=li[j+1],li[j]  # 交换元素
                exchange=True
        print(i,li)
        if not exchange:
            return

l=[4,5,3,1,8,6,7,9,2]
l1=[8,6,9,7,1,2,3,4,5]

print(f"原始序列：{l1}")
bubble_sort1(l1)

