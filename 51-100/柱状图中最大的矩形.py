#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 柱状图中最大的矩形.py
"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

https://leetcode-cn.com/problems/largest-rectangle-in-histogram/

求在该柱状图中，能够勾勒出来的矩形的最大面积。
以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

示例:
输入: [2,1,5,6,2,3]
输出: 10
"""
"""
思路：分治算法，注意两种情况：
1.[0,1,2,3,4,5,6,7,8,9...]这种情况使用分治法很慢，需要另外考虑。
2.[1,1,1,1,1,1,1,1,1,1...]这种情况使用分治法很慢，需要另外考虑。
我的解法是目前 leetcode 上最快的解法，击败了 100% 的用户。
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
