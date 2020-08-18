#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   select_sort.py
@Time    :   2020/08/09 22:02:26
@Author  :   huang xu 
@Version :   1.0
@Contact :   1475559715@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   这是选择排序的实现
'''

# here put the import lib

def select_sort(li):
    for i in range(len(li)-1):  # 第i趟，总共进行n-1趟
        min_loc=i       # 假设无序区中的最小值在无序区的首位
        for j in range(i+1,len(li)):   # 进行无序区最小值的确定(无序区的范围为i到n)
            if li[j] < li[min_loc]:
                li[j],li[min_loc]=li[min_loc],li[j] # 最小值和无序区的首位元素进行交换
        print(li)

l=[4,5,3,1,8,6,7,9,2]
l1=[8,6,9,7,1,2,3,4,5] 
print(f"原始序列：{l1}")
select_sort(l1)      

