#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 只出现一次的数字2.py
"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
输入: [2,2,3,2]
输出: 3

示例 2:
输入: [0,1,0,1,0,1,99]
输出: 99
"""
"""
思路：位运算中写出一个式子能够对三个相同数操作完成之后结果不变，对单个数操作完保存数。
"""
__author__ = 'Aiyane'


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # a = b = 0
        # for num in nums:
        #     b = b ^ num & ~a
        #     a = a ^ num & ~b
        # return b
        return (sum(set(nums))*3 - sum(nums)) // 2
