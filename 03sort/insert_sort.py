#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   insert_sort.py
@Time    :   2020/08/11 22:34:54
@Author  :   huang xu 
@Version :   1.0
@Contact :   1475559715@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   这是插入排序的实现
'''

# here put the import lib
def insert_sort(li):
    for i in range(1,len(li)):    # 手中已经有一张牌了(index=0)
                                  # 还要摸n-1张牌
                                  # 此时是摸第i张牌
        tmp=li[i]                 # 将摸起来的这张牌存起来
        j=i-1        # 手里的最后一张牌是i-1;手里的牌是有序区
        
        while j>=0 and li[j]>tmp:  # 当手里的牌(li[j])小于摸得牌时,  #必须时li[j]>tmp,摸起来的牌是存在tmp中的
                                   # 或者手里的牌已经全部小于摸得牌时 index=-1 停止循环
            li[j+1]=li[j]        # 将手里的牌向后移动一位(2,4,6,7>>>5 7移动一位(一次循环)，6移动一位（一次循环）)
            j=j-1                # 摸得牌与手里的倒数第二张牌(j-1)比较
        li[j+1]=tmp              #将摸得牌放在j+1的位置
        print(li)

l=[4,5,3,1,8,6,7,9,2]
l1=[8,6,9,7,1,2,3,4,5]
insert_sort(l)