#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   stack_sort.py
@Time    :   2020/08/19 15:42:59
@Author  :   huang xu 
@Version :   1.0
@Contact :   huangxu@xyebank.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   这是堆排序的实现
'''

# here put the import lib
def shift(li,low,high):
    """

    """
    i = low  # 父亲结点
    j = 2*i+1  # 子结点
    tmp=li[low]  # 将顶端结点暂时空置存储起来
    while j<=high: # 子结点小于high ,子结点有数
        if li[j+1]>li[j] and j+1<=high : # 如果有有右孩子，且比做孩子大
            j=j+1        # 就和右孩子比较（j:指向较大的孩子）
        if li[j]>tmp:     # 如果子结点大于父亲结点(县长的能力大于省长)，则提升
            li[i]=li[j]   
            i=j      #  往下一层看
            j=2*i+1  #  往下一层看 
        else:      #  tmp<li[j]    #  如果县长的能力小于省长(tmp),则tmp就任当前岗位li[i]
            li[i]=tmp
            break
        print(li)       
    else:
        li[i] = tmp  # 将顶部元素暂时放在合适的位置

li=[3,8,7,6,5,4,2,1]
print("原始序列:",li)
shift(li,0,6)
print("调整后的序列:",li)