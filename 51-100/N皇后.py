#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# N皇后.py
"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
https://leetcode-cn.com/problems/n-queens/
上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:
输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]

解释: 4 皇后问题存在两个不同的解法。
"""
"""
思路：注意N皇后问题是每一行都有一个皇后，每一列都有一个皇后，斜方向检查时只检查当前点前面
"""
__author__ = 'Aiyane'
import profile


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
                    res.append(mapping.copy())
                    mapping[i] = mapping[i][:j] + '.' + mapping[i][j+1:]
                    return 
                self.start(mapping, n, res, i+1, tuple(filter(lambda x:x!=j,col)))
                mapping[i] = mapping[i][:j] + '.' + mapping[i][j+1:]
        return res

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n == 1:
            return [['Q']]
        if n < 4:
            return []
        mapping = [ '.'*n for __ in range(n) ]
        return self.start(mapping, n, [], 0, tuple(i for i in range(n)))

def main():
    sol = Solution()
    # print(len(sol.solveNQueens(8)))
    print(sol.solveNQueens(8))

if __name__ == '__main__':
    # main()
    profile.run('main()')