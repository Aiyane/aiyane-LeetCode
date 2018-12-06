#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 全排列2.py
"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:
输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
"""
思路：在基本全排列基础上添加限制条件。
"""
__author__ = 'Aiyane'


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        def dfs(nums, visited, path, res):
            if len(path) == len(nums):
                res.append(path.copy())
            else:
                for i in range(len(nums)):
                    if i not in visited:
                        if i > 0 and nums[i-1] == nums[i] and i-1 not in visited:
                            continue
                        path.append(nums[i])
                        visited.add(i)
                        dfs(nums, visited, path, res)
                        visited.remove(i)
                        path.pop()
        
        res = []
        dfs(nums, set(), [], res)
        return res
