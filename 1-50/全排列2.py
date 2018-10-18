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
    def start(self, cur, oths):
        if len(oths) == 1:
            cur.append(oths.pop())
            del oths
            return [cur]

        res = []
        old = ''
        for oth in oths:
            new_c = cur.copy()
            new_c.append(oth)
            new_o = oths.copy()
            new_o.remove(oth)
            if old != oth:
                res.extend(self.start(new_c, new_o))
            old = oth
        return res

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        l = len(nums)
        if l == 1:
            return [nums]
        nums.sort()
        i = 0
        old = ''
        while i < l:
            new = nums.copy()
            ch = new.pop(i)
            if ch != old:
                res.extend(self.start([ch], new))
            old = ch
            i += 1
        return res

def main():
    sol = Solution()
    print(sol.permuteUnique([1,1,2]))

if __name__ == '__main__':
    main()