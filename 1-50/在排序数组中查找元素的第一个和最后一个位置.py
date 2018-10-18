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
        i = 0
        j = len(nums)-1
        while i <= j and nums[i] != nums[j]:
            m = (i + j) // 2
            if target > nums[m]:
                i = m + 1
            elif target < nums[m]:
                j = m - 1
            else:
                i_m = j_m = m

                while i < i_m and nums[(i + i_m) // 2] == target:
                    i_m = (i + i_m) // 2

                while j > j_m and nums[(j + j_m + 1) // 2] == target:
                    j_m = (j + j_m + 1) // 2

                i = (i + i_m + 1) // 2

                if nums[j] != target:
                    j = (j + j_m) // 2
        if j >= 0 and nums[i] == nums[j] == target:
            return i, j
        return -1, -1

        
def main():
    sol = Solution()
    print(sol.searchRange([5,7,7,8,8,10], 8))
    print(sol.searchRange([5,7,7,8,8,10], 6))
    print(sol.searchRange([1,2,2], 2))

if __name__ == '__main__':
    main()