#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 单词接龙.py
"""
给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。

说明:
如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

示例 1:
输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出: 5

解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。

示例 2:
输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: 0
解释: endWord "cog" 不在字典中，所以无法进行转换。
"""
"""
思路：头尾向中间靠近，beginWord 与 endWord 其实是等价的，那么由 beginWord 得到的集合与 endWord 得到的集合比较长度，哪一个更短，
就将哪一个集合作为下一次考察的对象，只要每一次添加的单词在另一个集合中，就可以停止，返回结果。另外就是，使用 26 个字母替换会比遍历全部
wordList 快的多。
"""
__author__ = 'Aiyane'
import profile


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        wl = len(beginWord)
        begin_set, end_set = {beginWord}, {endWord}

        i = 1
        while begin_set and end_set:
            i += 1
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set

            nextLst = set()
            for word in begin_set:
                for j in range(wl):
                    for k in range(26):
                        nextWord = word[:j] + chr(k+97) + word[j+1:]
                        if nextWord in end_set:
                            return i
                        if nextWord in wordList:
                            nextLst.add(nextWord)
                            wordList.remove(nextWord)
            begin_set = nextLst
        return 0

def main():
    sol = Solution()
    sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])

if __name__ == '__main__':
    profile.run('main()')
