#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 合并区间.py
"""
给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2:
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""
"""
思路：首先对 intervals 按 start 排序，for 循环会快一些。
"""
__author__ = 'Aiyane'


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        l = len(intervals)
        if l == 1:
            return intervals
        i = 1
        intervals.sort(key=lambda x:x.start)
        while i < l:
            if intervals[i].start <= intervals[i-1].end:
                if intervals[i].end > intervals[i-1].end:
                    intervals[i-1].end = intervals[i].end
                intervals.pop(i)
                l -= 1
            else:
                i += 1
        return intervals
