#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 搜索二维矩阵2.py
"""
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。

示例:
现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。
"""
__author__ = 'Aiyane'


class Solution:
    def _searchMatrix(self, matrix, y, target, m, n):
        if matrix[0][y] > target:
            return False
        elif matrix[0][y] == target:
            return True
        
        for i in range(1, m):
            if matrix[i][y] == target:
                return True
            if matrix[i][y] > target:
                if y+1 < n:
                    return self._searchMatrix(matrix, y+1, target, m, n)
                return False
        if y+1 < n:
            return self._searchMatrix(matrix, y+1, target, m, n)
        return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        if not matrix[0]:
            return False
        return self._searchMatrix(matrix, 0, target, len(matrix), len(matrix[0]))
