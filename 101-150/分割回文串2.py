#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 分割回文串2.py
"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回符合要求的最少分割次数。

示例:

输入: "aab"
输出: 1
解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
"""
__author__ = 'Aiyane'


class Solution:
    def __init__(self):
        self.map = {}

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s in self.map:
            return self.map[s]
        if s == s[::-1]:
            return 0

        l = len(s)
        minNum = float('inf')
        for i in range(1, l):
            if s[:i] == s[:i][::-1]:
                minNum = min(1 + self.minCut(s[i:]), minNum)
                if minNum == 1:
                    self.map[s] = minNum
                    return minNum
        self.map[s] = minNum
        return minNum
