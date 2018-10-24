#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 交错字符串.py
"""
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

示例 1:
输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true

示例 2:
输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false
"""
"""
思路：典型的动态规划问题，我的以下解法在 leetcode 上击败了 100% 的答案。
"""
__author__ = 'Aiyane'


class Solution:
    def start(self, s1, s2, s3):
        if (s1, s2) in self.map:
            return self.map[(s1,s2)]
        i = j = 0
        l1 = len(s1)
        l2 = len(s2)
        if l1 == 0:
            return s2 == s3
        if l2 == 0:
            return s1 == s3
        for k, ch in enumerate(s3):
            if i < l1 and j < l2:
                if ch == s1[i] and ch == s2[j]:
                    if self.start(s1[i+1:], s2[j:], s3[k+1:]):
                        self.map[(s1, s2)] = True
                        return True
                    if self.start(s2[j+1:], s1[i:], s3[k+1:]):
                        self.map[(s1, s2)] = True
                        return True
                    self.map[(s1, s2)] = False
                    return False
                elif ch == s1[i]:
                    i += 1
                elif ch == s2[j]:
                    j += 1
                else:
                    self.map[(s1, s2)] = False
                    return False
            elif i < l1 and ch == s1[i]:
                i += 1
            elif j < l2 and ch == s2[j]:
                j += 1
            else:
                self.map[(s1, s2)] = False
                return False
        res = i == l1 and j == l2
        self.map[(s1, s2)] = res
        return res

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        self.map = {}
        return self.start(s1,s2,s3)
