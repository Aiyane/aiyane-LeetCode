#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 不同的二叉搜索树.py
"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:
输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
"""
思路：典型的动态规划问题。
"""
__author__ = 'Aiyane'


class Solution:
    def start(self, l):
        if l == 1:
            return 1
        if l == 0:
            return 0
        if l in self.map:
            return self.map[l]
        res = 0
        i = 0
        while i < l:
            kids1 = self.start(i)
            kids2 = self.start(l-i-1)
            if kids1 and kids2:
                res += kids1 * kids2
            elif kids1:
                res += kids1
            elif kids2:
                res += kids2
            i += 1
        self.map[l] = res
        return res

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.map = {}
        return self.start(n)
