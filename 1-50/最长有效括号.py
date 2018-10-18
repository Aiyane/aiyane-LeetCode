#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 最长有效括号.py
"""
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
"""
"""
思路：使用栈存放位置，一个括号是后括号减前括号，2-1=1。但是有两个符号，所以从-1位置开始，遇到`(`括号重新开始，
遇到多余的`)`重新开始。
"""
__author__ = 'Aiyane'


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # stack存的是位置
        stack = [-1]
        maxlen = 0
        for i, ch in enumerate(s):
            if ch == '(':
                # 从`(`开始
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    # `)`多了，从这里重新开始
                    stack.append(i)
                else:
                    # 如果能匹配
                    maxlen = max(maxlen, i-stack[-1])
        return maxlen


def main():
    sol = Solution()
    print(sol.longestValidParentheses("()"))
    print(sol.longestValidParentheses("()()"))
    print(sol.longestValidParentheses("(()()"))
    print(sol.longestValidParentheses("()(()"))
    print(sol.longestValidParentheses("())(())"))
    print(sol.longestValidParentheses("()())"))
    print(sol.longestValidParentheses("(()"))
    print(sol.longestValidParentheses("()(())"))


if __name__ == '__main__':
    main()
