#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 搜索插入位置.py
"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:
输入: [1,3,5,6], 5
输出: 2

示例 2:
输入: [1,3,5,6], 2
输出: 1

示例 3:
输入: [1,3,5,6], 7
输出: 4

示例 4:
输入: [1,3,5,6], 0
输出: 0
"""
"""
思路：二分法，注意右边不需要减1
"""
__author__ = 'Aiyane'


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        j = len(nums) - 1
        i = 0

        while i < j:
            m = (i + j) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                j = m
            if nums[m] < target:
                i = m + 1

        if target > nums[i]:
            return i + 1
        return i

def main():
    sol = Solution()
    print(sol.searchInsert([1,3,5,6], 5))
    print(sol.searchInsert([1,3,5,6], 2))
    print(sol.searchInsert([1,3,5,6], 7))
    print(sol.searchInsert([1,3,5,6], 0))

if __name__ == '__main__':
    main()        