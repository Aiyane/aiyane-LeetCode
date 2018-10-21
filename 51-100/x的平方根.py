#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# x的平方根.py
"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:
输入: 4
输出: 2

示例 2:
输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。
"""
"""
思路：采用牛顿法，不过有一个最快的，只有 python 中才有的：
def mySqrt(x):
    return int(x**0.5)
"""
__author__ = 'Aiyane'


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        old = a = 1
        while True:
            a = (x+a*a)/(2*a)
            if old == int(a):
                return old
            old = int(a)
