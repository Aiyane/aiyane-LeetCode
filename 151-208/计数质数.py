#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 计数质数.py
"""
统计所有小于非负整数 n 的质数的数量。

示例:
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""
__author__ = 'Aiyane'


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [True for __ in range(n)]
        cnt = 0
        for i in range(2, n):
            if nums[i]:
                j = i + i
                while j < n:
                    nums[j] = False
                    j += i
                cnt += 1
        return cnt
