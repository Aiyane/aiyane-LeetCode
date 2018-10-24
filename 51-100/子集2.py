#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 子集2.py
"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:
输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
"""
思路：和“子集”那道题的思路类似，不过需要分两种情况。一个是当前字符与前一个字符不一样，一个是当前字符与前一个字符一样。
当一样时，则从上一个字符添加的位置开始遍历。
以下是我的解法，应该是最优，在我提交时是 leetcode 上最快的解法，击败了 100% 的答案。
"""
__author__ = 'Aiyane'


class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = [[]]
        v = '-1'
        l = 1
        for num in nums:
            tem = []
            old_l = len(res)
            if v != num:
                for ch in res:
                    tem.append(ch+[num])
            else:
                for ch in res[l:]:
                    if ch and ch[-1] == num:
                        tem.append(ch + [num])
            res.extend(tem)
            v = num
            l = old_l
        return res
