#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 编辑距离.py
"""
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符

示例 1:
输入: word1 = "horse", word2 = "ros"
输出: 3
解释: 
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

示例 2:
输入: word1 = "intention", word2 = "execution"
输出: 5
解释: 
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
"""
"""
思路：动态规划问题，a,b 表示字符串，i,j 表示两个长度。
三个转移方程，1.当 min(i,j) == 0; lev(i,j) == max(i,j) 2.当 a[i] == b[j]; lev(i,j) == lev(i-1,j-1)
3.否则 lev(i,j) == min(
    lev(i-1,j) + 1,
    lev(i,j-1) + 1,
    lev(i-1,j-1)+1
)
取一行矩阵，注意遍历第一个字符时是一个'0'字符，直接加1
"""
__author__ = 'Aiyane'


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))
        word2 = '0' + word2
        res = [i for i in range(len(word2))]
        for ch1 in word1:
            old = res[0]
            for i, ch2 in enumerate(word2):
                new = old
                old = res[i]
                if i == 0:
                    res = new + 1
                elif ch1 == ch2:
                    res[i] = new
                else:
                    res[i] = min(res[i-1], res[i], new) + 1
        return res[-1]
