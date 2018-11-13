#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 乘积最大子序列.py
"""
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""
"""
思路：非注释代码中，每一次取相乘或者原数中最大与最小的数，因为最小的数是负数与原数相乘也可能最大，最大数与正数相乘可能最大。
注释中，用 0 分开数组，用负数的个数区分，偶数就返回全部相乘，奇数就将每一个奇数分开数组，可以改成 DB。
"""
__author__ = 'Aiyane'

# from functools import reduce

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = big = small = nums[0]
        for n in nums[1:]:
            big, small = max(n, n * big, n * small), min(n, n * big, n * small)
            maximum = max(maximum, big)
        return maximum
        # if not nums: return float('-inf')
        # if 0 not in nums:
        #     sig = 0
        #     sm = []
        #     for i, num in enumerate(nums):
        #         if num % 2 != 0:
        #             sig += 1
        #         if num < 0:
        #             sm.append(i)
        #     if sig % 2 == 0:
        #         return reduce(lambda x,y: x*y, nums)
        #     else:
        #         maxNum = float('-inf')
        #         while sm:
        #             i = sm.pop()
        #             maxNum = max(maxNum, self.maxProduct(nums[:i]), self.maxProduct(nums[i+1:]), nums[i])
        #         return maxNum
        # else:
        #     index = nums.index(0)
        #     return max(self.maxProduct(nums[:index]), self.maxProduct(nums[index+1:]), 0)
