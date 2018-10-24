#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 扰乱字符串.py
"""
给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。

下图是字符串 s1 = "great" 的一种可能的表示形式。

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
在扰乱这个字符串的过程中，我们可以挑选任何一个非叶节点，然后交换它的两个子节点。

例如，如果我们挑选非叶节点 "gr" ，交换它的两个子节点，将会产生扰乱字符串 "rgeat" 。

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
我们将 "rgeat” 称作 "great" 的一个扰乱字符串。

同样地，如果我们继续将其节点 "eat" 和 "at" 进行交换，将会产生另一个新的扰乱字符串 "rgtae" 。

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
我们将 "rgtae” 称作 "great" 的一个扰乱字符串。

给出两个长度相等的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。

示例 1:

输入: s1 = "great", s2 = "rgeat"
输出: true
示例 2:

输入: s1 = "abcde", s2 = "caebd"
输出: false
"""
"""
思路：按照同样条件拆分字符串，如果两个字符串是扰乱字符串，那么必定存在一种拆分，
使得两个字符串的前串是扰乱字符串，后串同样是扰乱字符串。或者按照对称条件拆分，
前串与另一个的后串是扰乱字符串，后串与另一个的前串是扰乱字符串。DB 则保存的是两个子串是否是扰乱字符串。
"""
__author__ = 'Aiyane'
import profile


class Solution:
    def start(self, s1, s2, l):
        if (s1, s2) in self.map:
            return self.map[(s1, s2)]
        if (s2, s1) in self.map:
            return self.map[(s2, s1)]

        if s1 == s2:
            self.map[(s1, s2)] = True
            return True

        if sorted(s1) != sorted(s2):
            self.map[(s1, s2)] = False
            return False

        i = 1
        while i < l:
            if self.start(s1[:i], s2[:i], i) and self.start(s1[i:], s2[i:], l-i):
                self.map[(s1, s2)] = True
                return True
            if self.start(s1[:i], s2[l-i:], i) and self.start(s1[i:], s2[:l-i], l-i):
                self.map[(s1, s2)] = True
                return True
            i += 1
        self.map[(s1, s2)] = False
        return False
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        self.map = {}
        return self.start(s1, s2, len(s2))

if __name__ == "__main__":
    sol = Solution()
    # profile.run('sol.isScramble("abcdefghij", "efghijcadb")')
    print(sol.isScramble("abcdefghij", "efghijcadb"))
