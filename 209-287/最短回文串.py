#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 最短回文串.py
"""
给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。

示例 1:
输入: "aacecaaa"
输出: "aaacecaaa"

示例 2:
输入: "abcd"
输出: "dcbabcd"
"""
"""
思路：找出已 s[0] 开始的最长回文子串，从后往前查找，最后将后面剩余的子串倒过来连在 s 上即可。
"""
__author__ = 'Aiyane'


class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 第一种解法
        # if not s: return s
        # pre = ''
        # for ch in s[::-1]:
        #     now = pre + s
        #     if now == now[::-1]:
        #         return now
        #     pre += ch

        # 第二种解法
        # prv = len(s)
        # while s[:prv] != s[:prv][::-1]:
        #     prv -= 1
        # return s[prv:][::-1] + s

        # 第三种
        if len(s) < 2: 
            return s
        if len(set(s)) == 1:
            return s
        rs = s[::-1]
        if s == rs:
            return s
        ptr = 1
        while rs[ptr:] != s[:-ptr]:
            ptr += 1
        return rs[:ptr] + s
