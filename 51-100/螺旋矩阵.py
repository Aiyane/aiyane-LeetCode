#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 螺旋矩阵.py
"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]

示例 2:
输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
"""
思路：注意判断列表空的情况
"""
__author__ = 'Aiyane'


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        while matrix:
            res.extend(matrix[0])
            matrix.pop(0)
            for line in matrix[:-1]:
                if line:
                    res.append(line[-1])
                    line.pop()
            if matrix:
                res.extend(matrix[-1][::-1])
                matrix.pop()
            for line in matrix[::-1]:
                if line:
                    res.append(line[0])
                    line.pop(0)
        return res


def main():
    sol = Solution()
    print(sol.spiralOrder(
        [[7], [9], [6]]
    ))


if __name__ == '__main__':
    main()
