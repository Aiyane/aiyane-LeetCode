#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 组合.py
"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
"""
思路：回溯法，还有一个方法就是使用
from itertools import combinations
def combine(n, k):
    return list(combinations(range(1,n+1),k))
"""
__author__ = 'Aiyane'


class Solution:
    def start(self, lst, k):
        if k == 0:
            return [[]]
        res = []
        for i, v in enumerate(lst):
            for line in self.start(lst[i+1:], k-1):
                res.append([v] + line)
        return res
            
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.start([v for v in range(1, n+1)], k)