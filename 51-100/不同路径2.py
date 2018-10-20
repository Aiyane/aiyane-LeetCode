#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 不同路径2.py
"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
https://leetcode-cn.com/problems/unique-paths-ii/
网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。

示例 1:
输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2

解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
"""
"""
思路：和不同路径1一样，注意绕开障碍即可。
"""
__author__ = 'Aiyane'


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        self.tem = {}
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[-1][-1] == 1:
            return 0
        return self.getRes(m-1, n-1, obstacleGrid)

    def getRes(self, m, n, obj):
        if (m, n) in self.tem:
            return self.tem[(m, n)]
        if m == 0 and n == 0:
            return 1
        num = 0
        if m > 0 and obj[m-1][n] != 1:
            num = self.getRes(m-1, n, obj)
        if n > 0 and obj[m][n-1] != 1:
            num += self.getRes(m, n-1, obj)
        self.tem[(m, n)] = num
        return num
