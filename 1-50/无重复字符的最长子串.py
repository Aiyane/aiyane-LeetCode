# -*- coding: utf-8 -*-
#!/usr/bin/python3
# File Name: 无重复字符的最长子串.py
# Created Time: Mon 30 Apr 2018 12:15:47 AM CST
"""
给定一个字符串，找出不含有重复字符的最长子串的长度。

示例：

给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。

给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。

给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。
"""
"""
思路: 首先第一个指针指向相同元素的下一个位置, 另外用字典来找到相同元素的下标, 值为value, 下标为key
最大长度为原来的最大长度和当前下标减指针加一中的大的
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashTable = {}
        max_len = 0
        cur = 0

        for i, c in enumerate(s):
            if c in hashTable and cur <= hashTable[c]:
                cur = hashTable[c] + 1
            else:
                max_len = max(max_len, i - cur + 1)
            hashTable[c] = i

        return max_len

