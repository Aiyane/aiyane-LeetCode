#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 字母异位词分组.py
"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

说明：
所有输入均为小写字母。
不考虑答案输出的顺序。
"""
"""
思路：使用字典。
"""
__author__ = 'Aiyane'


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        table = dict()
        for word in strs:
            count = [0]*26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            key = hash(count)
            table.setdefault(key, []).append(word)
        return [val for val in table.values()]
