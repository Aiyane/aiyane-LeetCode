#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 解码方法.py
"""
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:
输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。

示例 2:
输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
"""
"""
思路：a = "12345", b = "4"
a[-1] + b = 54 > 26
所以数目等于 num(a)
如果 a = "754321" b = "4"
a[-1] + b <= 26
数目等于 num(a[:-1]) + num(a)
注意'0'字符
"""
__author__ = 'Aiyane'


class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        v = '3'
        res = [1]
        for i, ch in enumerate(s):
            if ch == '0':
                if int(v) > 2:
                    return 0
                else:
                    return res[-2] * self.numDecodings(s[i+1:])
            if int(v+ch) > 26:
                res.append(res[-1])
            else:
                res.append(res[-1]+res[-2])
            v = ch
        return res[-1]
