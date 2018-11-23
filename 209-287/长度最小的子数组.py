#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 长度最小的子数组.py
"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例: 
输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。

进阶:
如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
"""
"""
思路：遍历数组，双指针，一个在后一个不动，在后的向前移动，判断当前和是否大于 s，如果大于，另一个就向前移动，判断和是否还是大于 s。
取距离最小值。
"""
__author__ = 'Aiyane'


class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        minLen = 0
        numsLen = len(nums)
        allSum = start = end = 0
        while end < numsLen:
            allSum += nums[end]
            end += 1
            if allSum >= s:
                while allSum - nums[start] >= s:
                    allSum -= nums[start]
                    start += 1
                tmpLen = end - start
                if minLen == 0 or minLen > tmpLen:
                    minLen = tmpLen
        return minLen
