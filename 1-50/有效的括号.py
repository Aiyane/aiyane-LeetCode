#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
# 有效的括号.py
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

示例 3:
输入: "(]"
输出: false

示例 4:
输入: "([)]"
输出: false

示例 5:
输入: "{[]}"
输出: true
"""
"""
思路: 顺序执行就很快了
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = []
        for ch in s:
            if ch in (')', ']', '}') and not res:
                return False
            elif ch == ']' and res[-1] != '[':
                return False
            elif ch == '}' and res[-1] != '{':
                return False
            elif ch == ')' and res[-1] != '(':
                return False
            elif ch in ('(', '{', '['):
                res.append(ch)
            else:
                res.pop(-1)
        return False if res else True
