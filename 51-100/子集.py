#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 子集.py
"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
"""
从[]开始依次增加元素，每一个数字增加到每一个元素后面。
"""
__author__ = 'Aiyane'


class Solution:
    def subsets(self, nums):
        res = [[]]
        for v in nums:
            tem = []
            for line in res:
                tem.append(line+[v])
            res.extend(tem)
        return res
