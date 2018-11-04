#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 单词接龙2.py
"""
给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。

说明:
如果不存在这样的转换序列，返回一个空列表。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

示例 1:
输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

示例 2:
输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: []

解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
"""
__author__ = 'Aiyane'


class Solution(object):
    def diff(self, s1, s2):

        count = 0
        for ch1, ch2 in zip(s1, s2):
            if ch1 != ch2:
                count += 1
                if count > 1:
                    return False
        return True
    
    def helper(self, res):
        wordList = self.wordList - set(res)
        for word in wordList:
            if self.diff(word, res[-1]): 
                if word == self.endWord:
                    self.res.append(res + [word])
                    return []
                yield res + [word]

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        self.res, self.wordList, self.endWord, allPaths = [], set(wordList), endWord, [[beginWord]]

        for __ in range(len(wordList)):

            allPaths = [newPath for path in allPaths for newPath in self.helper(path)]
            if self.res:
                return self.res

        return self.res