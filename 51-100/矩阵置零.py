#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 矩阵置零.py
"""
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:
输入: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

示例 2:
输入: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

进阶:
一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个常数空间的解决方案吗？
"""
"""
思路：将一行中的0添加到数组，一行行置零，最后遍历数组，列置零。
"""
__author__ = 'Aiyane'


class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        m = len(matrix[0])
        i = 0
        res = []
        changed = False
        while i < l:
            for j, num in enumerate(matrix[i]):
                if num == 0:
                    res.append(j)
                    changed = True
            if changed:
                for j in range(m):
                    matrix[i][j] = 0
                changed = False
            i += 1
        for i, line in enumerate(matrix):
            if i in res:
                line[i] = 0
