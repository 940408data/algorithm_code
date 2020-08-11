#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   fib.py
@Time    :   2020/08/11 15:09:47
@Author  :   huang xu 
@Version :   1.0
@Contact :   huangxu@xyebank.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   这是斐波拉契数列的一个实现
'''

# here put the import lib
class Solution:
    def fib(self, n: int) -> int:
        if n<2:
            return 1 if n>0 else 0
        elif n>=2:
            x,y=0,1
            for _ in range(n-1):
                x,y=y,x+y
            return y % 1000000007

if __name__ == "__main__":
    f=Solution()
    print(f.fib(5))