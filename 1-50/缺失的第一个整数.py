#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 缺失的第一个整数.py
"""
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:
输入: [1,2,0]
输出: 3

示例 2:
输入: [3,4,-1,1]
输出: 2

示例 3:
输入: [7,8,9,11,12]
输出: 1

说明:
你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。
"""
"""
思路：注意数字可能相等，该结果可能为最大数字
"""
__author__ = 'Aiyane'


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        i = 0
        while i < l:
            if 0 <= nums[i]-1 < l and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1
        for i in range(l):
            if nums[i] != i+1:
                return i+1
        return l + 1
