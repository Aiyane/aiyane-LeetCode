#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# N皇后2.py
"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
https://leetcode-cn.com/problems/n-queens-ii/
上图为 8 皇后问题的一种解法。

给定一个整数 n，返回 n 皇后不同的解决方案的数量。

示例:
输入: 4
输出: 2

解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""
"""
思路：和N皇后一样，不过可以这样：
def totalNQueens(n):
    dict = {
        1 : 1,
        4 : 2,
        5 : 10,
        6 : 4,
        7 : 40,
        8 : 92,
        9 : 352,
        10: 724,
        11: 2680,
        12: 14200,
    }
    if n in dict: 
        return dict[n]
    return 0
我也是无语了。
"""
__author__ = 'Aiyane'

class Solution:
    def check(self, mapping, x, y, n):
        for j in (-1, 1):
            tx, ty = x - 1, y + j
            while 0 <= tx and 0 <= ty < n:
                if mapping[tx][ty] == 'Q':
                    return False
                tx, ty = tx - 1, ty + j
        return True

    def start(self, mapping, n, res, i, col):
        # mapping:地图
        # n:皇后总数
        # res:结果列表
        # i:上一个皇后位于的行号
        # col:所有没有皇后的列号集合
        for j in col:
            if self.check(mapping, i, j, n):
                mapping[i] = mapping[i][:j] + 'Q' + mapping[i][j+1:]
                if i+1 == n:
                    res += 1
                    mapping[i] = mapping[i][:j] + '.' + mapping[i][j+1:]
                    return res
                res = self.start(mapping, n, res, i+1, tuple(filter(lambda x:x!=j,col)))
                mapping[i] = mapping[i][:j] + '.' + mapping[i][j+1:]
        return res

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n < 4:
            return 0
        mapping = [ '.'*n for __ in range(n) ]
        return self.start(mapping, n, 0, 0, tuple(i for i in range(n)))
