#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 只出现一次的数字3.py
"""
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

示例 :
输入: [1,2,1,3,2,5]
输出: [3,5]

注意：
结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
"""
"""
思路：位运算，想办法找出两个单一的数的中间数字，取最后一位为 1 的数字，用 i = i & -i 可以取出。那个单一的数在该位必定一个为 0，
一个为 1。所以取 & 时就可以得到一个大于0的数一个等于0。
"""
__author__ = 'Aiyane'


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        for num in nums:
            i ^= num
        i = i & -i
        a = b = 0
        for num in nums:
            if num & i:
                a ^= num
            else:
                b ^= num
        return [a, b]
