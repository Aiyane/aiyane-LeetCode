#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第k个排列.py
"""
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：
给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。

示例 1:
输入: n = 3, k = 3
输出: "213"

示例 2:
输入: n = 4, k = 9
输出: "2314"
"""
"""
思路：利用好阶乘的条件，计算阶乘，当序号大于该阶乘时就直接返回。
"""
__author__ = 'Aiyane'


class Solution:
    def start(self, res, nums, n):
        if n == 0:
            return res
        # 计算阶乘
        s = 1
        for v in range(1, 1 + n):
            s *= v
        # 如果 k 大于该阶乘直接返回
        if self.k > s:
            self.k -= s
            return False
        for i in range(n):
            tem = self.start(res+nums[i], nums[:i]+nums[i+1:], n-1)
            if tem:
                return tem

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.k = k
        return self.start('', [str(i+1) for i in range(n)], n)
        