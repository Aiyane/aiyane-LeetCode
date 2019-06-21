#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 同构字符串.py
"""
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:
输入: s = "egg", t = "add"
输出: true

示例 2:
输入: s = "foo", t = "bar"
输出: false

示例 3:
输入: s = "paper", t = "title"
输出: true
说明:
你可以假设 s 和 t 具有相同的长度。
"""
__author__ = 'Aiyane'


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        table = dict()
        vals = set()
        for ch1, ch2 in zip(s, t):
            if ch1 not in table:
                if ch2 in vals:
                    return False
                table[ch1] = ch2
                vals.add(ch2)
            elif table[ch1] != ch2:
                return False
        return True
                