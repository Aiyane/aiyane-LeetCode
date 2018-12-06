#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 在排序数组中查找元素的第一个和最后一个位置.py
"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""
"""
思路：二分法，但是边界值需要测试
"""
__author__ = 'Aiyane'


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1, -1]
        l = len(nums)
        i, j = 0, l - 1
        mid = l // 2
        while True:
            if target > nums[mid]:
                i = mid + 1
            elif target < nums[mid]:
                j = mid - 1
            else:
                i = j = mid
                while j + 1 < l and nums[j + 1] == target:
                    j += 1
                while 0 <= i - 1 and nums[i - 1] == target:
                    i -= 1
                return [i, j]
            mid = (i + j) // 2
