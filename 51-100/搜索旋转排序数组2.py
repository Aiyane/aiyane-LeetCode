#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 搜索旋转排序数组2.py
"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:
输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true

示例 2:
输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false

进阶:
这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
"""
"""
思路：二分法，利用旋转数组性质。
"""
__author__ = 'Aiyane'


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False

        l = len(nums)
        if l == 1:
            return target == nums[0]

        mid = l//2
        if nums[mid] == target:
            return True

        if nums[mid] < target:
            if nums[mid] == nums[-1]:
                i = mid + 1
                while i < l and nums[i] == nums[-1]:
                    i += 1
                if i == l:
                    return self.search(nums[:mid], target)
                return self.search(nums[mid+1:], target)
            if nums[mid] > nums[-1] or nums[-1] >= target:
                return self.search(nums[mid+1:], target)
            return self.search(nums[:mid], target)

        if nums[mid] == nums[0]:
            i = mid - 1
            while i >= 0 and nums[i] == nums[0]:
                i -= 1
            if i + 1 == 0:
                return self.search(nums[mid+1:], target)
            return self.search(nums[:mid], target)

        if nums[mid] < nums[0] or nums[0] <= target:
            return self.search(nums[:mid], target)
        return self.search(nums[mid+1:], target)
