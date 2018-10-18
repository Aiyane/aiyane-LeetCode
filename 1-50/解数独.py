#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 解数独.py
"""
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。

Note:

给定的数独序列只包含数字 1-9 和字符 '.' 。
你可以假设给定的数独只有唯一解。
给定数独永远是 9x9 形式的。
"""
"""
思路：回溯法
"""
__author__ = 'Aiyane'


class Solution:
    def check(self, board, i, j):
        tem = []
        for ch in board[i]:
            if ch != '.':
                if ch in tem:
                    return False
                tem.append(ch)
        tem.clear()
        for line in board:
            if line[j] != '.':
                if line[j] in tem:
                    return False
                tem.append(line[j])
        tem.clear()
        for x in range(i // 3 * 3, i // 3 * 3 + 3):
            for y in range(j // 3 * 3, j // 3 * 3 + 3):
                if board[x][y] != '.':
                    if board[x][y] in tem:
                        return False
                    tem.append(board[x][y])
        return True
    
    def solve(self, board, i, j):
        if board[i][j] == '.':
            for ch in range(1, 10):
                board[i][j] = str(ch)
                if self.check(board, i, j):
                    if j < 8:
                        if self.solve(board, i, j+1):
                            return True
                    elif i < 8:
                        if self.solve(board, i+1, 0):
                            return True
                    else:
                        return True
            board[i][j] = '.'
            return False
        elif j < 8:
            return self.solve(board, i, j+1)
        elif i < 8:
            return self.solve(board, i+1, 0)
        return True

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board, 0, 0)
