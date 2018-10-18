#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File Name: 最长回文字串.py
# Created Time: Tue 01 May 2018 04:48:48 PM CST
"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"
"""
"""
思路: 确定回文的开始字符和最大长度字符, 每一次更新最大长度和回文开始字符
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return 0

        maxLen = 1  # 回文的长度
        start = 0  # 回文开始的位置
        
        for i in range(len(s)):
            # 审查是否与最大长度前面那个字符对应
            if i-maxLen >= 1 and s[i-maxLen-1:i+1] == s[i-maxLen-1:i+1][::-1]:
                start = i-maxLen-1
                maxLen += 2 
            # 审查是否与最大长度第一个字符对应
            if i-maxLen >= 0 and s[i-maxLen:i+1] == s[i-maxLen:i+1][::-1]:
                start = i-maxLen
                maxLen += 1
        return s[start:start+maxLen]

