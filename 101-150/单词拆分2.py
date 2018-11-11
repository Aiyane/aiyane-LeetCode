#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 单词拆分2.py
"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：

分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例 1：
输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]

示例 2：
输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。

示例 3：
输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出:
[]
"""
"""
思路：动态规划问题，注意 s 在 wordDict 中并不能直接返回，也可能被切分。
"""
__author__ = 'Aiyane'


class Solution:
    def __init__(self):
        self.map = {}

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def wordBreakDB(s, lens, wordSet):
            res = []
            if s in self.map:
                return self.map[s]
            for wl in lens:
                if s[:wl] in wordSet:
                    res.extend([s] if wl == len(s) else [s[:wl] + ' ' + kid for kid in wordBreakDB(s[wl:], lens, wordSet)])
            self.map[s] = res
            return res
        return wordBreakDB(s, set(len(word) for word in wordDict), set(wordDict))