#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 螺旋矩阵2.py
"""
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:
输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
"""
思路：除去第一行，之后的规则是：下、左、上、右，并且下左的长度和上右的长度一样。例如 n=7，
除去第一行的1到7。之后，下6->左6、上5->右5、下4->左4、上3->右3、下2->左2、上1->右1。注意结束条件两种情况
"""
__author__ = 'Aiyane'


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[i+1 for i in range(n)] for __ in range(n)]
        l = n - 1
        x = 1
        y = n - 1
        v = n+1
        while l:
            k = l
            while k > 0:
                res[x][y] = v
                v += 1
                k -= 1
                x += 1
            x -= 1
            y -= 1

            k = l
            while k > 0:
                res[x][y] = v
                v += 1
                k -= 1
                y -= 1
            y += 1
            x -= 1

            l -= 1
            if l == 0:
                return res

            k = l
            while k > 0:
                res[x][y] = v
                v += 1
                k -= 1
                x -= 1
            x += 1
            y += 1

            k = l
            while k > 0:
                res[x][y] = v
                v += 1
                k -= 1
                y += 1
            y -= 1
            x += 1

            l -= 1
        return res