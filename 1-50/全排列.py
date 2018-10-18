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
    def start(self, cur, oths):
        if len(oths) == 1:
            cur.append(oths.pop())
            del oths
            return [cur]

        res = []
        for oth in oths:
            new_c = cur.copy()
            new_c.append(oth)
            new_o = oths.copy()
            new_o.remove(oth)
            res.extend(self.start(new_c, new_o))
        return res

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        l = len(nums)
        if l == 1:
            return [nums]
        i = 0
        while i < l:
            new = nums.copy()
            res.extend(self.start([new.pop(i)], new))
            i += 1
        return res

def main():
    sol = Solution()
    print(sol.permute([1,2,3]))

if __name__ == '__main__':
    main()