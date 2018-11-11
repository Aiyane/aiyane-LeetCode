#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 单词拆分.py
"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。

示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""
"""
思路：循环字典中长度，如果可以切分则以某一个长度开始一定能够完成匹配。动态规划。
"""
__author__ = 'Aiyane'


class Solution:
    def __init__(self):
        self.map = {}

    def wordBreakDB(self, s, lens, wordSet):
        if s in wordSet:
            return True
        if s in self.map:
            return self.map[s]

        for wl in lens:
            if s[:wl] in wordSet:
                if self.wordBreakDB(s[wl:], lens, wordSet):
                    self.map[s] = True
                    return True
        self.map[s] = False
        return False

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.wordBreakDB(s, set(len(word) for word in wordDict), set(wordDict))
