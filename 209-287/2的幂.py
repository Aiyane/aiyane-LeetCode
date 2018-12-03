#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 2的幂.py
"""
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:
输入: 1
输出: true

解释: 20 = 1
示例 2:
输入: 16
输出: true
解释: 24 = 16

示例 3:
输入: 218
输出: false
"""
"""
思路：每一次乘以2就是左移，所以不可能有重合的位。
"""
__author__ = 'Aiyane'


class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not n & (n - 1)
