#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 寻找旋转排序数组中的最小值.py
"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

示例 1:
输入: [3,4,5,1,2]
输出: 1

示例 2:
输入: [4,5,6,7,0,1,2]
输出: 0
"""
"""
思路：二分法，注意旋转数组的特征。
"""
__author__ = 'Aiyane'


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        while i < j and nums[i] >= nums[j]:
            mid = (i + j) // 2
            if nums[mid] >= nums[i]:
                i = mid + 1
            else:
                j = mid
        return nums[i]
