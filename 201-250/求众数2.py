#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 求众数2.py
"""
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

示例 1:
输入: [3,2,3]
输出: [3]

示例 2:
输入: [1,1,1,3,3,2,2,2]
输出: [1,2]
"""
"""
思路：摩尔投票法，整个数组最多只有两个数能够为众数，所以遍历数组，对数字进行计数，如果下一个数等于该数，则计数加一，如果下一个数小于该数，
计数减一，当计数为0时数字被替换。最后再验证两个候选数是否为众数即可。
"""
__author__ = 'Aiyane'


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        a = b = ca = cb = 0
        for num in nums:
            if num == a:
                ca += 1
            elif num == b:
                cb += 1
            elif ca == 0:
                a = num
                ca = 1
            elif cb == 0:
                b = num
                cb = 1
            else:
                ca -= 1
                cb -= 1
        ca = cb = 0
        for num in nums:
            if num == a:
                ca += 1
            elif num == b:
                cb += 1
        res = []
        if ca > l // 3:
            res.append(a)
        if cb > l // 3:
            res.append(b)
        return res
