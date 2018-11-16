#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 岛屿的个数.py
"""
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。
你可以假设网格的四个边均被水包围。

示例 1:
输入:
11110
11010
11000
00000

输出: 1

示例 2:
输入:
11000
11000
00100
00011

输出: 3
"""
"""
思路：深度优先遍历。
"""
__author__ = 'Aiyane'


class Solution:
    def numIslandsDFS(self, grid, x, y, m, n):
        grid[x][y] = '0'
        if x - 1 >= 0 and grid[x-1][y] == '1':
            self.numIslandsDFS(grid, x-1, y, m, n)
        if x + 1 < m and grid[x+1][y] == '1':
            self.numIslandsDFS(grid, x+1, y, m, n)
        if y - 1 >= 0 and grid[x][y-1] == '1':
            self.numIslandsDFS(grid, x, y-1, m, n)
        if y + 1 < n and grid[x][y+1] == '1':
            self.numIslandsDFS(grid, x, y+1, m, n)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        res = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    res += 1
                    self.numIslandsDFS(grid, x, y, m, n)
        return res
