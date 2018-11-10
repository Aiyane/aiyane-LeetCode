#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 被围绕的区域.py
"""
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:
X X X X
X O O X
X X O X
X O X X

运行你的函数后，矩阵变为：
X X X X
X X X X
X X X X
X O X X
解释:
被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，
或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
"""
"""
思路：典型的深度优先搜索或者广度优先搜索都可以。
"""
__author__ = 'Aiyane'


class Solution:
    def solveDFS(self, x, y, board):
        if (x, y) not in self.o_set:
            self.o_set.add((x, y))
            if x - 1 >= 0:
                if board[x-1][y] == 'O':
                    self.solveDFS(x-1, y, board)
            if y - 1 >= 0:
                if board[x][y-1] == 'O':
                    self.solveDFS(x, y-1, board)
            if x + 1 < self.row_num:
                if board[x+1][y] == 'O':
                    self.solveDFS(x+1, y, board)
            if y + 1 < self.col_num:
                if board[x][y+1] == 'O':
                    self.solveDFS(x, y+1, board)

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        self.row_num = len(board)
        self.col_num = len(board[0])
        self.o_set = set()
        for y, ch in enumerate(board[0]):
            if ch == 'O':
                self.solveDFS(0, y, board)
        for y, ch in enumerate(board[-1]):
            if ch == 'O':
                self.solveDFS(self.row_num - 1, y, board)
        for x, line in enumerate(board[1:-1], 1):
            if line[0] == 'O':
                self.solveDFS(x, 0, board)
            if line[-1] == 'O':
                self.solveDFS(x, self.col_num - 1, board)
        for x in range(self.row_num):
            for y in range(self.col_num):
                if board[x][y] == 'O':
                    if (x, y) not in self.o_set:
                        board[x][y] = 'X'
                    
