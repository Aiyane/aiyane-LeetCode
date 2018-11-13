#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 寻找旋转数组中的最小值2.py
"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

注意数组中可能存在重复的元素。

示例 1：
输入: [1,3,5]
输出: 1

示例 2：
输入: [2,2,2,0,1]
输出: 0

说明：
这道题是 寻找旋转排序数组中的最小值 的延伸题目。
允许重复会影响算法的时间复杂度吗？会如何影响，为什么？
"""
"""
思路：有重复元素，会影响时间复杂度，最后一个相等判断后，必须一个个的遍历检查。
"""
__author__ = 'Aiyane'

# [10,1,10,10,10], [2,2,2,0,1]
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
            if nums[mid] > nums[i]:
                i = mid + 1
            elif nums[mid] < nums[i]:
                j = mid
            else:
                return min(nums[i:j+1])
        return nums[i]
