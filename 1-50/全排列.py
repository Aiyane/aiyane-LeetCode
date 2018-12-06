#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 全排列.py
"""
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
"""
思路：常规解法
"""
__author__ = 'Aiyane'


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, res, visited, path):
            if len(path) == len(nums):
                res.append(path.copy())
            else:
                for num in nums:
                    if num not in visited:
                        visited.add(num)
                        path.append(num)
                        dfs(nums, res, visited, path)
                        path.pop()
                        visited.remove(num)
        res = []
        dfs(nums, res, set(), [])
        return res
