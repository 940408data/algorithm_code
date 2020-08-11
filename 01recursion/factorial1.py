#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   factorial1.py
@Time    :   2020/08/11 10:01:38
@Author  :   huang xu 
@Version :   1.0
@Contact :   huangxu@xyebank.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   在类中使用递归函数
'''

# here put the import lib
class Solution:
    def jie(self,n):
        if n>1:
            return n*self.jie(n-1)    # 而不是self.jie(self,n-1)
        elif n==1:
            return 1
        else:
            print("非法输入")


if __name__ == "__main__":
    s=Solution()
    print(s.jie(5))
