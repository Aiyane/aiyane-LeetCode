#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 完全平方数.py
"""
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:
输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4.

示例 2:
输入: n = 13
输出: 2
解释: 13 = 4 + 9.
"""
"""
思路：使用最短路径算法或者四平方和定理。前一个算法更加容易想到。路径长度都是 1，每一个数字代表一个地点，每个地点有至多 小于其的完全平方数 个路径。
将每一次地点出现都保存地点-路径距离。第一次遍历时肯定是最近距离，所以之后遇见就忽略。第二个方法是个数学问题。。。
"""
__author__ = 'Aiyane'

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # from queue import Queue
        # que = Queue()
        # que.put((n, 0))
        # had = [False for __ in range(n+1)]
        # had[n] = True

        # while que.not_empty:
        #     num, step = que.get()
        #     i = 1
        #     newNum = num - i*i
        #     while newNum >= 0:
        #         if newNum == 0:
        #             return step + 1
        #         if not had[newNum]:
        #             had[newNum] = True
        #             que.put((newNum, step + 1))

        #         i += 1
        #         newNum = num - i*i
        
        # 四平方和定理
        import math
        while (n % 4 == 0):
            n /= 4
        if (n % 8 == 7):
            return 4
        
        a = 0
        while a*a<=n:
            b = int(math.sqrt(n-a*a))
            if a*a+b*b == n:
                if 0 in [a, b]:
                    return 1
                else:
                    return 2
            a+=1
        return 3
