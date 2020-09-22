#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   quick_sort.py
@Time    :   2020/08/16 19:00:17
@Author  :   huang xu 
@Version :   1.0
@Contact :   1475559715@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   这是快速排序的实现
'''

# here put the import lib
def quick_sort(li,left,right):
    if left<right:  # 只要left=right一次递归就完成了
        mid=partition(li,left,right)   # 找到归为的位置(调用归位函数)
        quick_sort(li,left,mid-1)  # 对左边进行递归
        print("right",right)
        print("left",left)
        print("左")
        quick_sort(li,mid+1,right) # 对右边进行递归
        print("left",left)
        print("right",right)
        print("右")
    # left=riht 递归就完成了
    

def partition(li,left,right):
    tmp=li[left]
    while left<right: # 只要left=right归位就完成了
        # 这个while就在完成归位的操作
        # 从右边找比tmp小的数填充左边的空位
        while li[right]>=tmp and left<right:  #可能右边全部都是比tmp大的数,最终就会left=right.然后这次递归就完成了
            right-=1
        # 当循环结束时就找到比tmp小的数的位置了
        li[left]=li[right]   # 将该数填充到左边的空位上
        # print(f"左边第{left}空位填充完毕:{li}")

        # 此时右边上有空位
        # 在左边找比tmp大的数填充在右边的空位上
        while li[left]<=tmp and left<right:  
            left += 1
        li[right]=li[left]
        # print(f"右边第{right}空位填充完毕:{li}")

    li[left]=tmp   # 归位，此时left=right
    print(li)
    return left # 把归位的位置返回给mid


l=[5,3,7,4,8]
# print("原始序列",l)
# partition(l,0,len(l)-1)
print("原始序列",l)
quick_sort(l,0,len(l)-1)
print(l)