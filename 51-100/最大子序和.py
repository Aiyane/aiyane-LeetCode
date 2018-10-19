#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 最大子序和.py
"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""
"""
思路：ptr 为序列和，当考察到当前数字时，如果序列和大于0，有积极影响，所以该序列加上该数字。否则序列和换成该数字，结果则是所有序列和中最大的。
"""
__author__ = 'Aiyane'


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = ptr = float('-inf')
        for num in nums:
            ptr = num if ptr < 0 else ptr + num
            m = max(m, ptr)
        return m

def main():
    sol = Solution()
    print(sol.maxSubArray([8,-19,5,-4,20]))

if __name__ == '__main__':
    main()
