#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 存在重复元素3.py
"""
给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 k。

示例 1:
输入: nums = [1,2,3,1], k = 3, t = 0
输出: true

示例 2:
输入: nums = [1,0,1,1], k = 1, t = 2
输出: true

示例 3:
输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false
"""
"""
思路：当t=0时，就是需要判断相等才符合条件，所以可以优化这一段。
"""
__author__ = 'Aiyane'


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        l = len(nums)
        if l < 2 or k == 0:
            return False
        if t == 0 and len(nums) == len(set(nums)):
            return False
        for i, num in enumerate(nums):
            for j in range(i + 1, i + k + 1):
                if j >= l:
                    break
                if abs(num - nums[j]) <= t:
                    return True
        return False
