#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 下一个排列.py
"""
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
"""
思路：首先写出数组倒序算法，然后从后向前遍历，找出第一对正序的两个数字，例如：8，3，7，6，5，4，2，1。中第一对为 3，7。
然后从 7 开始向后遍历，遇到小于 3 时，例如 2。取前一个与 3 交换 3<->2。然后将 2 之后数组全部倒序。
如果没有正序数字，那么整个数组倒序。
"""
__author__ = 'Aiyane'
import profile

class Solution:
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        pos = l - 2
        while pos >= 0:
            if nums[pos] < nums[pos+1]:
                break
            pos -= 1

        if pos < 0:
            self.reverse(nums, 0, l - 1)
        else:
            p = pos + 1
            while p < l:
                if nums[p] <= nums[pos]:
                    break
                p += 1
            p -= 1
            nums[pos], nums[p] = nums[p], nums[pos]
            self.reverse(nums, pos+1, l-1)
