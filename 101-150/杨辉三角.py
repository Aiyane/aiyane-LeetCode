#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 杨辉三角.py
"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
__author__ = 'Aiyane'


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows > 0:
            res = [[1]]
            for i in range(numRows-1):
                res.append([1]+[num+res[-1][i-1] for i, num in enumerate(res[-1][1:], 1)]+[1])
            return res
        return []
