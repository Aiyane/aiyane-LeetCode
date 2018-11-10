#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 分割回文串.py
"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:
输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
"""
思路：动态规划问题。
"""
__author__ = 'Aiyane'


class Solution:
    def __init__(self):
        self.map = {}

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        l = len(s)
        if l <= 1:
            return [[s]]
        if s in self.map:
            return self.map[s]
        res = [[s[:i]] + lst for i in range(1, l) if s[:i] == s[:i][::-1] for lst in self.partition(s[i:])]
        res = res + [[s]] if s == s[::-1] else res
        self.map[s] = res
        return res
