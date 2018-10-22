#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 单词搜索.py
"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.
"""
"""
思路：使用回溯算法。
"""
__author__ = 'Aiyane'


class Solution:
    def start(self, board, x, y, word, n):
        if board[x][y] != word[0]:
            return False
        if len(word) == 1:
            return True
        n.append((x, y))
        if (x-1, y) not in n and x > 0 and self.start(board, x-1, y, word[1:], n):
            return True
        if (x, y-1) not in n and y > 0 and self.start(board, x, y-1, word[1:], n):
            return True
        if (x+1, y) not in n and x < len(board)-1 and self.start(board, x+1, y, word[1:], n):
            return True
        if (x, y+1) not in n and y < len(board[0])-1 and self.start(board, x, y+1, word[1:], n):
            return True
        n.pop()
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for x, line in enumerate(board):
            for y, ch in enumerate(line):
                if self.start(board, x, y, word, []):
                    return True
        return False
