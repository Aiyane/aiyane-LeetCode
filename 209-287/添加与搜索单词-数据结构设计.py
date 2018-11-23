#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 添加与搜索单词-数据结构设计.py
"""
设计一个支持以下两种操作的数据结构：

void addWord(word)
bool search(word)
search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。

示例:
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

说明:
你可以假设所有单词都是由小写字母 a-z 组成的。
"""
"""
思路：使用TrieTree数据结构解决，似乎使用 长度-word 字典两重循环更快一些？
"""
__author__ = 'Aiyane'

class TrieNode:
    def __init__(self, x):
        self.val = x
        self.next = []
        self.word = False

class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = set()
        self.trieRoot = TrieNode('#')

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if word:
            self.table.add(word)
            i = 0
            l = len(word)
            root = self.trieRoot
            while i < l:
                for node in root.next:
                    if node.val == word[i]:
                        root = node
                        i += 1
                        break
                else:
                    break
            while i < l:
                node = TrieNode(word[i])
                root.next.append(node)
                root = node
                i += 1
            root.word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if '.' not in word:
            return word in self.table
        root = self.trieRoot
        i = 0
        l = len(word)

        nodes = root.next

        while 1:
            if word[i] != '.':
                nodes = filter(lambda node: word[i] == node.val, nodes)
            tmp = []
            if i + 1 == l or not nodes:
                for node in nodes:
                    if node.word:
                        return True
                return False
            for node in nodes:
                tmp.extend(node.next)
            nodes = tmp
            i += 1
