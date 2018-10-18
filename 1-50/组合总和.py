#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 组合总和.py
"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 

示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]

示例 2:
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
"""
思路：回溯法
"""
__author__ = 'Aiyane'


class Solution:
    def comp(self, candidates, lst, target):
        res = []
        for i, ch in enumerate(candidates):
            tem = lst.copy()
            tem.append(ch)
            if sum(tem) == target:
                res.append(tem)
            elif sum(tem) < target:
                res.extend(self.comp(candidates[i:], tem, target))
            else:
                return res
        return res
            

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.comp(candidates, [], target)

def main():
    sol = Solution()
    print(sol.combinationSum([2,3,6,7], 7))
    print(sol.combinationSum([2,3,5], 8))

if __name__ == '__main__':
    main()