#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 单词搜索2.py
"""
给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

示例:
输入: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

输出: ["eat","oath"]
说明:
你可以假设所有输入都由小写字母 a-z 组成。

提示:
你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。
"""
__author__ = 'Aiyane'


class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        m = len(board)
        n = len(board[0])
        # 初始化
        chs = dict()
        for x, line in enumerate(board):
            for y, ch in enumerate(line):
                chs.setdefault(ch, []).append((x, y))
        ans = set()

        # 构建trieTree
        head = []
        for word in words:
            i = 0
            l = len(word)
            root = ['#', head]
            while i < l:
                for node in root[1]:
                    if node[0] == word[i]:
                        root = node
                        i += 1
                        break
                else:
                    break
            while i < l:
                node = [word[i], [], False]
                root[1].append(node)
                root = node
                i += 1
            root[2] = True
        
        def findWordsDFS(board, node, pos, ans, word, x, y, m, n):
            ch = node[0]
            if node[2]:
                ans.add(word)
            for node in node[1]:
                ch = node[0]
                if x + 1 < m and (x+1, y) not in pos and board[x+1][y] == ch:
                    findWordsDFS(board, node, pos | {(x+1, y)}, ans, word+ch, x+1, y, m, n)
                if x - 1 >= 0 and (x-1, y) not in pos and board[x-1][y] == ch:
                    findWordsDFS(board, node, pos | {(x-1, y)}, ans, word+ch, x-1, y, m, n)
                if y + 1 < n and (x, y+1) not in pos and board[x][y+1] == ch:
                    findWordsDFS(board, node, pos | {(x, y+1)}, ans, word+ch, x, y+1, m, n)
                if y - 1 >= 0 and (x, y-1) not in pos and board[x][y-1] == ch:
                    findWordsDFS(board, node, pos | {(x, y-1)}, ans, word+ch, x, y-1, m, n)
        # 遍历树
        for node in head:
            ch = node[0]
            if ch in chs:
                for x, y in chs[ch]:
                    findWordsDFS(board, node, {(x, y)}, ans, ch, x, y, m, n)
        return list(ans)
