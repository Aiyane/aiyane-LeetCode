#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 重复的DNA序列.py
"""
所有 DNA 由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来查找 DNA 分子中所有出现超多一次的10个字母长的序列（子串）。

示例:
输入: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

输出: ["AAAAACCCCC", "CCCCCAAAAA"]
"""
"""
思路：两个集合，一个已读一个考察。
"""
__author__ = 'Aiyane'

class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l = len(s)
        if l <= 10:
            return []
        res = set()
        st = set()
        i = 0
        while i + 9 < l:
            if s[i:i+10] in st:
                res.add(s[i:i+10])
            else:
                st.add(s[i:i+10])
            i += 1
        return list(res)
