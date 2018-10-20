#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 最后一个单词的长度.py
"""
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:
输入: "Hello World"
输出: 5
"""
"""
思路：注意字符串长度只有1个或0个或前后有多个空格的情况
"""
__author__ = 'Aiyane'


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = s.strip().rsplit(' ', 1)
        return len(res[0]) if len(res) < 2 else len(res[1])
        