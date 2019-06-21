#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 三的幂.py
"""
给定一个整数，写一个函数来判断它是否是 3 的幂次方。

示例 1:
输入: 27
输出: true

示例 2:
输入: 0
输出: false

示例 3:
输入: 9
输出: true

示例 4:
输入: 45
输出: false
进阶：
你能不使用循环或者递归来完成本题吗？
"""
"""
思路：在整数范围内，3**19是最大的3的幂次。所以n必须是该数的因子。
"""
__author__ = 'Aiyane'


class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 3**19 % n == 0
