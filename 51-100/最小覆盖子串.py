#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 最小覆盖子串.py
"""给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。
"""
"""
思路：首先建立字符-次数字典，然后从
"""
__author__ = 'Aiyane'


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        c_set = {}
        n = 0
        for ch in t:
            if ch in c_set:
                c_set[ch] += 1
            else:
                c_set[ch] = 1
            n += 1
        start = end = 0
        i = 0
        # 从第二个开始遍历
        for j, ch in enumerate(s, 1):
            if ch in c_set:
                # ch 在 t 中，且还有余
                if c_set[ch] > 0:
                    n -= 1
                # 无论有没有余，只要在 t 中就减一
                c_set[ch] -= 1
            # 长度为 0
            if n == 0:
                while i < j and (s[i] not in c_set or c_set[s[i]] < 0):
                    if s[i] in c_set and c_set[s[i]] < 0:
                        c_set[s[i]] += 1
                    i += 1
                c_set[s[i]] += 1
                n += 1
                if end == 0 or j-i < end-start:
                    start, end = i, j
                i += 1
        return s[start:end]
