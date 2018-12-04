#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 丑数2.py
"""
编写一个程序，找出第 n 个丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

示例:
输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。

说明:  
1 是丑数。
n 不超过1690。
"""
"""
思路：可以考虑通过堆实现，以下是通过三个指针实现。
"""
__author__ = 'Aiyane'


class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        p2 = p3 = p5 = 0
        n -= 1
        while n != 0:
            num2 = res[p2]*2
            num3 = res[p3]*3
            num5 = res[p5]*5
            if num2 < num5 and num2 < num3:
                res.append(num2)
                p2 += 1
            elif num3 < num2 and num3 < num5:
                res.append(num3)
                p3 += 1
            elif num5 < num2 and num5 < num3:
                res.append(num5)
                p5 += 1
            elif num2 == num3 and num2 < num5:
                res.append(num2)
                p2 += 1
                p3 += 1
            elif num2 == num5 and num2 < num3:
                res.append(num2)
                p2 += 1
                p5 += 1
            elif num3 == num5 and num3 < num2:
                res.append(num3)
                p3 += 1
                p5 += 1
            elif num3 == num2 == num5:
                res.append(num3)
                p2 += 1
                p3 += 1
                p5 += 1
            n -= 1
        return res[-1]
