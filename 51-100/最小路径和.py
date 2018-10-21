#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 最小路径和.py
"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""
"""
思路：动态规划，和不同路径那道题思路一样
"""
__author__ = 'Aiyane'

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 每一个坐标到终点的最小距离
        self.map = {}
        m = len(grid)
        n = len(grid[0])
        return self.start(grid, m-1, n-1)
    
    def start(self, grid, m, n):
        if (m, n) in self.map:
            return self.map[(m, n)]
        
        if m == 0 and n == 0:
            return grid[0][0]
        
        res = grid[m][n] 

        if m > 0:
            if n > 0:
                res += min(self.start(grid, m-1, n), self.start(grid, m, n-1))
            else:
                res += self.start(grid, m-1, n)
        elif n > 0:
            res += self.start(grid, m, n-1)

        self.map[(m, n)] = res
        return res
