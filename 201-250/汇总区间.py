#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 汇总区间.py
"""
给定一个无重复元素的有序整数数组，返回数组区间范围的汇总。

示例 1:
输入: [0,1,2,4,5,7]
输出: ["0->2","4->5","7"]
解释: 0,1,2 可组成一个连续的区间; 4,5 可组成一个连续的区间。

示例 2:
输入: [0,2,3,4,6,8,9]
输出: ["0","2->4","6","8->9"]
解释: 2,3,4 可组成一个连续的区间; 8,9 可组成一个连续的区间。
"""
__author__ = 'Aiyane'


class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        nums.append(-1)
        cur = start = nums[0]
        mid = "->"
        res = []
        for num in nums[1:]:
            if num != cur + 1:
                if cur == start:
                    res.append(str(start))
                else:
                    res.append(str(start)+mid+str(cur))
                cur = start = num
            else:
                cur = num
        return res
