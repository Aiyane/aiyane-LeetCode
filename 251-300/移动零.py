#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 移动零.py
"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""
__author__ = 'Aiyane'


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = n = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                n += 1
            else:
                i += 1
        for _ in range(n):
            nums.append(0)

