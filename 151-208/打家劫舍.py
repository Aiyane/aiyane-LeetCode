#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 打家劫舍.py
"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:
输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

示例 2:
输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
"""
"""
思路：典型的动态规划问题，也可以用
last, now = 0, 0
for n in nums:
    last, now = now, max(last+n, now)
return max(last, now)
解决。
"""
__author__ = 'Aiyane'


class Solution:
    def __init__(self):
        self.map = {}

    def robDB(self, nums, i, l):
        if l == i:
            return 0
        if l == i+1:
            return nums[-1]
        if i in self.map:
            return self.map[i]
        res = max(self.robDB(nums, i+1, l), nums[i] + self.robDB(nums, i+2, l))
        self.map[i] = res
        return res

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        return self.robDB(nums, 0, len(nums))
