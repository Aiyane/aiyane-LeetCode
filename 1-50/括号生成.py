#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
# 括号生成.py
"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
"""
思路: 使用树的深度优先遍历来解决, 左右括号分别为左节点和右节点, l和r为还剩多少, tem为此时的字符串, res为结果
使用回溯以及减枝的策略
"""


class Solution:
    def getRes(self, l, r, tem, res):
        if l > r:
            return res

        if l == 0 and r == 0:
            res.append(tem)
        else:
            if l > 0:
                res = self.getRes(l-1, r, tem+'(', res)
            if r > 0:
                res = self.getRes(l, r-1, tem+')', res)

        return res

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.getRes(n, n, '', [])
