#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 存在重复元素2.py
"""
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:
输入: nums = [1,2,3,1], k = 3
输出: true

示例 2:
输入: nums = [1,0,1,1], k = 1
输出: true

示例 3:
输入: nums = [1,2,3,1,2,3], k = 2
输出: false
"""
__author__ = 'Aiyane'


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        l = len(nums)
        if l <= k + 1:
            return len(set(nums)) < l
        if len(set(nums)) == l:
            return False
        i = 0
        while i+k < l:
            if len(set(nums[i:i+k+1])) <= k:
                return True
            i += 1 
        return False
