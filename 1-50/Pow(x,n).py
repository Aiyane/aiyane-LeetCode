#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Pow(x, n).py
"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:
输入: 2.00000, 10
输出: 1024.00000

示例 2:
输入: 2.10000, 3
输出: 9.26100

示例 3:
输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25

说明:
-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。
"""
"""
对python来说，这种题没意义。
"""
__author__ = 'Aiyane'


class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x**n
        # 解法2
        # if n < 0:
        #     x, n = 1/x, -n
        # if n == 0:
        #     return 1
        # if n == 1:
        #     return x
        # if n%2 == 0:
        #     return self.myPow(x*x, n//2)
        # else:
        #     return self.myPow(x*x, n//2) * x
        