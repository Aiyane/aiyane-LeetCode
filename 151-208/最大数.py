#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 最大数.py
"""
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:
输入: [10,2]
输出: 210

示例 2:
输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
"""
"""
思路：转换成字符串，对数字进行前后交换比较。
"""
__author__ = 'Aiyane'


class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        res = []
        for num in nums:
            num = str(num)
            for i, num2 in enumerate(res):
                if num + num2 > num2 + num:
                    res.insert(i, num)
                    break
            else:
                res.append(num)
        if set(res) == {'0'}:
            return '0'
        return ''.join(res)
