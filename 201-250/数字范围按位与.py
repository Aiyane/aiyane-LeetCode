#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 数字范围按位与.py
"""
给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。

示例 1: 

输入: [5,7]
输出: 4
示例 2:

输入: [0,1]
输出: 0
"""
"""
思路：在相同的高位中，表示这个范围的二进制全是相同的，在不同的低位中，只要开始有不同，那么与的结果肯定是 0。
"""
__author__ = 'Aiyane'

class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        count = 0
        while n != m:
            count += 1
            m >>= 1
            n >>= 1
        return m << count
