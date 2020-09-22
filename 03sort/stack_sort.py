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
        if  j+1<=high and li[j+1]>li[j] : # 如果有有右孩子，且比左孩子大
                         # 注意li[j+1]>li[j] and j+1<=high 前面
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



def stack_sort(li):
    ## 构造堆
    low=0
    high=len(li)-1
    j=(high-1)//2  ##最后一个父亲结点
    for i in range(j,-1,-1):
        shift(li,i,high)   ### 每一个大根堆的的high,都默认为整个堆的high
    for i in range(high,-1,-1):
        li[low],li[i]=li[i],li[low]  ## 顶部元素出堆(放在末尾位置i)
        shift(li,low,i-1)   ## 进行一次向下调整。调整次high-1的位置

def stack_sort1(data):
    n=len(data)
    for i in range(n//2-1,-1,-1):
        shift(data,i,n-1)
    for i in range(n-1,-1,-1):
        li[0],li[i]=li[i],li[0]
        shift(data,0,i-1) #

li=[3,8,7,6,5,4,2,1]
print("原始序列:",li)
stack_sort1(li)
print("调整后的序列:",li)