#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 插入区间.py
"""
给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1:
输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
输出: [[1,5],[6,9]]

示例 2:
输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
"""
"""
思路：一个个考察，注意左端取小的那个，注意循环结束后判断。
"""
__author__ = 'Aiyane'


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res = []
        start = None
        for i, interval in enumerate(intervals):
            if newInterval.start > interval.end:
                res.append(interval)
            elif newInterval.end <= interval.end:
                if newInterval.end < interval.start:
                    if start is not None:
                        newInterval.start = start
                    res.append(newInterval)
                elif start is not None and start < interval.start:
                    interval.start = start
                elif newInterval.start < interval.start:
                    interval.start = newInterval.start
                res.extend(intervals[i:])
                return res

            elif start is not None:
                if interval.start < start:
                    start = interval.start
            else:
                start = min(newInterval.start, interval.start)

        if start is not None and newInterval.end > start:
            newInterval.start = start
        res.append(newInterval)
        return res
