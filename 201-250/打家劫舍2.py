#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 打家劫舍2.py
"""
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。
同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:
输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

示例 2:
输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
"""
"""
思路：典型的动态规划问题。需要注意边界条件，以及限制条件，所以保存的数据需要将限制条件一起保存。
"""
__author__ = 'Aiyane'


class Solution:
    def __init__(self):
        self.map = dict()

    def robDB(self, nums, i, l, hadFirst):
        if i == l:
            if hadFirst:
                return 0
            return nums[i]
        if i > l:
            return 0
        key = (i, hadFirst)
        if key in self.map:
            return self.map[key]
        if i == 0:
            return max(self.robDB(nums, i+1, l, False), nums[i] + self.robDB(nums, i+2, l, True))
        res = max(self.robDB(nums, i+1, l, hadFirst), nums[i] + self.robDB(nums, i+2, l, hadFirst))
        self.map[key] = res
        return res

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        return self.robDB(nums, 0, len(nums) - 1, False)
