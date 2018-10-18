#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 组合总和2.py
"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 

示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

示例 2:
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
"""
"""
思路：回溯法，和上一题差不多
"""
__author__ = 'Aiyane'



class Solution:
    def comp(self, candidates, lst, target):
        res = []
        i = 0
        l = len(candidates)
        if l == 0:
            return res
        sch = candidates[0]
        while i < l:
            ch = candidates[i]
            if i == 0 or ch != sch:
                tem = lst.copy()
                tem.append(ch)
                if sum(tem) == target:
                    res.append(tem)
                elif sum(tem) < target:
                    res.extend(self.comp(candidates[i+1:], tem, target))
                else:
                    return res
                sch = candidates[i]
            i += 1
        return res

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.comp(candidates, [], target)

def main():
    sol = Solution()
    print(sol.combinationSum2([3,1,3,5,1,1], 8))
    print(sol.combinationSum2([2,5,2,1,2], 5))

if __name__ == '__main__':
    main()