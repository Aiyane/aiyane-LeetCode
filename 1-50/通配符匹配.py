#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 通配符匹配.py
"""
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。

示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:
输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。

示例 3:
输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
"""
"""
思路：`*`的重复效果一样，从前开始匹配，先匹配先完成。
"""
__author__ = 'Aiyane'
import profile


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = j = 0
        pj = si = None
        l = len(s)
        lp = len(p)
        if s != p == '':
            return False
        
        while i < l:
            if j < lp and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < lp and p[j] == '*':
                pj = j
                si = i
                j += 1
            elif pj is not None:
                j = pj + 1
                si += 1
                i = si
            else:
                return False
        res = p[j:].strip('*')
        return res == ''


def main():
    sol = Solution()
    print(sol.isMatch("aa", "*"))

if __name__ == '__main__':
    profile.run('main()')