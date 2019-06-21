#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 组合总数3.py
"""
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：
所有数字都是正整数。
解集不能包含重复的组合。 

示例 1:
输入: k = 3, n = 7
输出: [[1,2,4]]

示例 2:
输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
"""
"""
思路：回溯法即可，注意数组中数字不能大于9.
"""
__author__ = 'Aiyane'


class Solution:
    def combinationSum3DFS(self, k, start, n):
        if n < start:
            return []
        if k == 1 and start <= n and n < 10:
            return [[n]]

        res = []
        for num in range(start, 9):
            tmp = self.combinationSum3DFS(k-1, num+1, n-num)
            if tmp:
                for lst in tmp:
                    res.append([num] + lst)
        return res

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return self.combinationSum3DFS(k, 1, n)