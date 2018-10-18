#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 搜索旋转排序数组.py
"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4

示例 2:
输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
"""
"""
思路：取中间数字，分四种情况
"""
__author__ = 'Aiyane'


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        i = 0
        j = l-1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == target:
                return m
            if nums[i] <= nums[m]:
                if nums[i] <= target < nums[m]:
                    j = m -1
                else:
                    i = m + 1
            else:
                if nums[m] < target <= nums[j]:
                    i = m + 1
                else:
                    j = m - 1
        return -1

def main():
    sol = Solution()
    print(sol.search([4,5,6,7,0,1,2], 0))
    print(sol.search([4,5,6,7,0,1,2], 3))
    print(sol.search([], 3))
    print(sol.search([1], 1))
    print(sol.search([1], 2))

if __name__ == '__main__':
    main()