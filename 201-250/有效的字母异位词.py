#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 有效的字母异位词.py
"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false
说明:

你可以假设字符串只包含小写字母。
进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
"""
__author__ = 'Aiyane'


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        chs = dict()
        for ch in s:
            if ch in chs:
                chs[ch] += 1
            else:
                chs[ch] = 1
        for ch in t:
            if ch in chs and chs[ch] > 0:
                chs[ch] -= 1
                if chs[ch] == 0:
                    chs.pop(ch)
            else:
                return False
        return True if not chs else False
