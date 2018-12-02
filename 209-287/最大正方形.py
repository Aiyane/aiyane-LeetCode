#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 最大正方形.py
"""
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4
"""
"""
思路：注意题目是正方形，所以动态规划记录边长就行。
"""
__author__ = 'Aiyane'

class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        dp = [[0]*len(matrix[0]) for i in range(0, len(matrix))]
        ans = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == "1":
                    if i == 0:
                        dp[i][j] = 1
                    elif j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    ans = max(ans, dp[i][j])
        return ans*ans
