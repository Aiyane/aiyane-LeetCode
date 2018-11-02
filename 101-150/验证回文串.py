#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 验证回文串.py
"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
"""
"""
思路：注意不排除数字，长度为1时返回True。
"""
__author__ = 'Aiyane'


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        if j == 0:
            return True
        while i < j:
            while not s[i].isalpha() and not s[i].isdigit() and i < j:
                i += 1
            while not s[j].isalpha() and not s[j].isdigit() and i < j:
                j -= 1
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True
