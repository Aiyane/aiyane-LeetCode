#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 最长连续序列.py
"""
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:
输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
"""
"""
思路：使用集合，看代码。
"""
__author__ = 'Aiyane'


class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        maxLen = 0
        for num in nums:
            if num - 1 not in nums:
                cur = num + 1
                while cur in nums:
                    cur += 1
                maxLen = max(maxLen, cur - num)
        return maxLen
                