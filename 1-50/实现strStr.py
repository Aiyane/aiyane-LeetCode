#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
# 实现strStr.py
"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2

示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1

说明:
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
"""
"""
思路: 比较字符串, 注意不相同时指针加1, 不会直接加needle长度个单位
"""


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        i = 0
        j = 0
        h_len = len(haystack)
        n_len = len(needle)
        while i < h_len:
            if haystack[i] != needle[0]:
                i += 1
            else:
                if i+n_len <= h_len and haystack[i:i+n_len] == needle:
                    return i
                elif i+n_len <= h_len:
                    i += 1
                else:
                    return -1
        return -1
