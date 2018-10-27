#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 三角形最小路径和.py
"""
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：
如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
"""
__author__ = 'Aiyane'


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle: return 0
        vals = [v for v in triangle[-1]]
        for line in triangle[:-1][::-1]:
            for i, v in enumerate(line):
                vals[i] = v + min(vals[i], vals[i+1])
        return vals[0]
