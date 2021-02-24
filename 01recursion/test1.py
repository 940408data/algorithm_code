#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test1.py
@Time    :   2021/02/23 14:33:48
@Author  :   huang xu 
@Version :   1.0
@Contact :   1475559715@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   1输入：一个M*N二维格子地图，每一个格子今天被盗或者没有。
              输出：地图上连续被盗最大区域的格子数
              连续的定义：上下左右相邻
              样例输入：被盗写为1，没有被盗写为0
'''

# here put the import lib
def get_continu_num(arr,i,j):
    num=1
    arr[i][j]=0 
    m=len(arr)
    n=len(arr[0])
    if i-1>-1 and arr[i-1][j]==1:
        num=num+get_continu_num(arr,i-1,j)
    if i+1<m  and arr[i+1][j]==1:
        num=num+get_continu_num(arr,i+1,j)
    if j-1>-1 and arr[i][j-1]==1:
        num=num+get_continu_num(arr,i,j-1)
    if j+1<n and arr[i][j+1]==1:
        num=num+get_continu_num(arr,i,j+1)
    return num

def get_max_num(arr):
    max_num = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]==1:
                num = get_continu_num(arr,i,j)
                if num>max_num:
                    max_num = num

    return max_num

arr=[[1,0,0,1,0],
     [1,0,1,0,0],
     [0,0,1,0,1],
     [1,0,1,0,1],
     [1,0,1,1,0]]

print(get_max_num(arr))


