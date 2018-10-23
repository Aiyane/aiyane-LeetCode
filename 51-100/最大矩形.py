#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 最大矩形.py
"""
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:
输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6
"""
"""
思路：这道题应该与“柱状图中最大的矩形”结合来解决，每一行都可以看作“柱状图中最大的矩形”问题来解决，所以直接使用了那道题的程序。
"""
__author__ = 'Aiyane'


class Solution:
    def start(self, heights, l):
        if l == 1:
            return heights[0]
        min_v = min(heights)
        d = heights.index(min_v)
        maxs = min_v*l
        tem1 = tem2 = 0
        if d > 0:
            tem1 = self.start(heights[:d], d)
        if d < l - 1:
            tem2 = self.start(heights[d+1:], l - d - 1)
        return max(tem1, tem2, maxs)

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        if len(set(heights)) == 1:
            return heights[0]*len(heights)
        v = -1
        for ch in heights:
            v += 1
            if v != ch:
                return self.start(heights, len(heights))
        if v % 2 == 0:
            return heights[(v//2)]*(v//2+1)
        return heights[(v//2+1)]*(v//2+1)

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        res = 0
        h = [0 for __ in range(n)]
        for i, line in enumerate(matrix):
            for j, v in enumerate(line):
                h[j] = h[j] + 1 if v == '1' else 0
            res = max(self.largestRectangleArea(h), res)
        return res
